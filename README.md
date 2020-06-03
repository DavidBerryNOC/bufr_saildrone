Code to convert NetCDF file to BUFR based on mappings defined in JSON files.

Usage:

    python3 nc2bufr.py -i <input_file> -o <output_file> -t <bufr_template> -m <mappings>
    
Where:

    <input_file> is the NetCDF data file to read from
    <output_file> is the destination file to write the BUFR message to
    <bufr_template> is a JSON representation of a BUFR 4 message
    <mappings> is a JSON file containing the mappings from the NetCDF file to the BUFR message to encode
    
Sample files are provided. 
- INPUT_DATA contains the example NetCDF files
- OUTPUT_DATA contains those examples encoded to BUFR and then decoded to text
- bufr_message.json is the example template file
- saildrone_map.json is the example mapping from the NetCDF file to BUFR  