import netCDF4 as nc
import json
import time as time
import numpy as np
from encode_message import *
import sys
from bitarray import bitarray
import os
import argparse

class bufr_list:
    sequence = list()

    def __init__(self, o):
        self.flatten( o )

    def flatten(self, o):
        for value in o:
            if value['FXXYYY'][0] == '3':
                self.flatten( value['descriptors'] )
            # don't need to worry about operators at this stage (need to check this is 100% true)
            #elif value['FXXYYY'][0] == '2':
            #    print("operator")
            elif value['FXXYYY'][0] == '1':
                nreplications = value['nreplications']
                if value['FXXYYY'][3:6] == '000':
                    assert value['descriptors'][0]['FXXYYY'][0:3] == '031'
                    value['descriptors'][0]['map'] = "const:{}".format(nreplications)
                    self.sequence.append( value['descriptors'][0] )
                    istart = 1
                else:
                    istart = 0
                for rep in range( nreplications ):
                    self.flatten( value['descriptors'][istart:len(value['descriptors'])] )
            elif value['FXXYYY'][0] == '0':
                self.sequence.append( value )
            else:
                assert False

def main( argv ):

    # get arguments
    parser = argparse.ArgumentParser(description='Convert Saildrone NetCDF file to BUFR (selected elements only)')
    parser.add_argument("-i", dest="input_file", required=True, help="Source NetCDF file to convert")
    parser.add_argument("-o", dest="output_file", required=True, help="Destination file to write to")
    parser.add_argument('-m', dest="mapping", required = False, default='saildrone_map.json',
                        help = 'JSON file containing mappings from NetCDF to BUFR template' )
    parser.add_argument('-t', dest="template", required=False, default='bufr_message.json',
                        help='JSON file containing template for BUFR message')

    args = parser.parse_args()
    # load file defining mappings to BUFR for saildrone .nc files
    map_file = args.mapping
    with open( map_file ) as fh:
        mappings = json.load( fh )

    # load message template
    template = args.template
    with open( template ) as fh:
        message = json.load( fh )

    # copy sequences from mapping to message template
    message['header']['section3']['descriptors']['value'] = mappings['descriptors']

    # now load netcdf file
    datafile = args.input_file
    root_data = nc.Dataset( datafile, 'r', format='NETCDF4')

    # get typical time, for this example just set to start of period
    typical_time = root_data.getncattr( 'time_coverage_start' )
    typical_time = time.strptime( typical_time[0:19], "%Y-%m-%dT%H:%M:%S" )

    message['header']['section1']['year']['value']   = typical_time.tm_year
    message['header']['section1']['month']['value']  = typical_time.tm_mon
    message['header']['section1']['day']['value']    = typical_time.tm_mday
    message['header']['section1']['hour']['value']   = typical_time.tm_hour
    message['header']['section1']['minute']['value'] = typical_time.tm_min
    message['header']['section1']['second']['value'] = typical_time.tm_sec

    # convert mappings to list of bufr descriptors
    seq = bufr_list( mappings['descriptors_expanded'] )

    # get number of subsets in file
    nsubsets = len( root_data.dimensions['obs'] )

    subset_data = list()
    subset_replications = list()

    # iterate over subset
    for idx in range( nsubsets ):
        output = list()
        replications = list()
        for elem in seq.sequence:
            # check if we have variable in netcdf file
            if elem['map'] is not None :
                if isinstance(elem['map'], list ):
                    assert len( elem['map'] ) == 2
                    assert elem['transform'] is not None
                    value_path = elem['map'][0].split(':')
                    val1 = np.asscalar(root_data.variables[value_path[1]][0, idx])
                    value_path = elem['map'][1].split(':')
                    val2 = np.asscalar(root_data.variables[value_path[1]][0, idx])
                    val = list(map(eval(elem['transform']), {val1}, {val2} ))[0]
                else:
                    # get value to use
                    value_path = elem['map'].split(':')
                    if value_path[0] == 'var' :
                        if value_path[2] == 'attr':
                            val = root_data.variables[ value_path[1] ].getncattr( value_path[3] )
                        elif value_path[2] == 'value':
                            val = np.asscalar(root_data.variables[value_path[1]][0, idx])
                        else :
                            assert False
                    elif value_path[0] == 'global':
                        assert value_path[1] == 'attr'
                        val = root_data.getncattr( value_path[2] )
                    elif value_path[0] == 'const':
                        val = value_path[1]
                    else:
                        assert False
                     # now check to see if we need to transform it
                    if elem['transform'] is not None :
                        val = list(map(eval(elem['transform']), {val}))[0]
                if elem['FXXYYY'][0:3] == '031' :
                    replications.append( val )
            else:
                # set to missing
                val = None
            if val is not None :
                output.append( val )
            else:
                output.append( None )
        # now append subset and number of replications in subset message template
        message['data']['subsets'].append( output )
        message['data']['replications'].append( replications )

    # set number of subsets in template
    message['header']['section3']['number_subsets']['value'] = nsubsets
    message['data']['number_subsets'] = nsubsets

    # encode message
    bitsOut = encode_message( message )

    # write to file
    file_out = open( args.output_file, 'wb')
    bitarray(bitsOut).tofile(file_out)
    file_out.close()


if __name__ == '__main__':
    main(sys.argv[1:])