As part of the validation process the sequence has been modified, the revised proposal can be found below.

As part of this name has been changed from unmanned surface vehicles to autonomous surface vehicles.

**PROPOSAL**
(Details of proposal)
Add new entry to BUFR Table D
Category 15 – Oceanographic report sequences

Table Reference | Table References | Element Name | Description
-- | -- | -- | --
F XX YYY | F XX YYY | |
3 15 011 | | Met-ocean   observations from autonomous surface vehicles |
 &nbsp; |3 01 150 | (WIGOS   identifier) |
 &nbsp; |0 01 087 | WMO marine   observing platform extended identifier |
 &nbsp; |0 01 036 | Agency   in charge of operating the observing platform |
 &nbsp;|0 01 085 | Observing   platform manufacturer’s model |
 &nbsp;|0 01 086 | Observing   platform manufacturer’s serial number |
 &nbsp;|0 03 001 | Surface   station type |
 &nbsp;|2 08 032 | Change   width of CCITT IA5 field |
 &nbsp;|0 01 079 | Unique   ID for profile | UUID   for report, 32 character hex string
 &nbsp;|2 08 000 | Change   width of CCITT IA5 field |
 &nbsp;|3 01 011 | Year,   month, day |
 &nbsp;|3 01 012 | Hour,   minute |
 &nbsp;|3 01 021 | (Latitude/longitude   (high accuracy)) |
 &nbsp;|0 01 012 | Direction   of motion of moving observing platform |
 &nbsp;|0 01 014 | Platform drift speed (high precision) |
 &nbsp;|0 11 104 | True heading of   aircraft, ship or other mobile platform[DB2] |
 &nbsp;|1 03 000 | Delayed   replication of 3 descriptor |
 &nbsp;|0 31 000 | Short   delayed descriptor replication factor |
 &nbsp;|0 07 031 | Height   of barometer above mean sea level |
 &nbsp;|3 06 038 | Sequence   for representation of standard surface marine meteorological observations   from moored buoys |
 &nbsp;|0 12 161 | Skin   temperature |
 &nbsp;|1 01 000 | Delayed   replication of 1 descriptors |
 &nbsp;|0 31 000 | Short   delayed descriptor replication factor |
 &nbsp;|3 06 034 | (Surface   current) |
 &nbsp;|1 01 000 | Delayed   replication of 1 descriptor |
 &nbsp;|0 31 000 | Short   delayed descriptor replication factor |
 &nbsp;|3 06 039 | (Sequence   for representation of basic wave measurements) |
 &nbsp;|1 01 000 | Delayed   replication of 1 descriptors |
 &nbsp;|0 31 000 | Short   delayed descriptor replication factor |
 &nbsp;|3 06 033 | (Surface   salinity) |
 &nbsp;|1 01 000 | Delayed   replication of 1 descriptor |
 &nbsp;|0 31 000 | Short   delayed descriptor replication factor |
 &nbsp;|3 06 041 | (Depth   and temperature profile (high accuracy/precision)) |
 &nbsp;|1 01 000 | Delayed   replication of 1 descriptors |
 &nbsp;|0 31 000 | Short   delayed descriptor replication factor |
 &nbsp;|3 06 004 | (Depth,   temperature, salinity) |
 &nbsp;|1 01 000 | Delayed   replication of 1 descriptor |
 &nbsp;|0 31 000 | Short   delayed descriptor replication factor |
 &nbsp;|3 06 005 | Sub-surface   current measurements |
 &nbsp;|1 05 000 | Delayed   replication of 5 descriptors |
 &nbsp;|0 31 000 | Short   delayed descriptor replication factor |
 &nbsp;|0 41 001 | pCO2 |
 &nbsp;|0 08 043 | Atmospheric   chemical or physical constituent type |
 &nbsp;|0 15 028 | Mole   fraction of atmospheric constituent / pollutant in dry air |
 &nbsp;|0 08 043 | Atmospheric   chemical or physical constituent type |
 &nbsp;|0 13 080 | Water   pH |
 &nbsp;|1 04 000 | Delayed   replication of 4 descriptors |
 &nbsp;|0 31 000 | Short   delayed descriptor replication factor |
 &nbsp;|0 41 005 | Turbidity |
 &nbsp;|0 41 003 | Dissolved   nitrates |
 &nbsp;|0 22 188 | Dissolved   oxygen |
 &nbsp;|0 41 002 | Fluorescence |
 &nbsp;|1 01 000 | Delayed   replication of 1 descriptor |
 &nbsp;|0 31 000 | Short   delayed descriptor replication factor |
 &nbsp;|3 06 040 | (Sequence   for representation of detailed spectral wave measurements) |
 &nbsp;|1 04 000 | Delayed   replication of 4 descriptors |
 &nbsp;|0 31 000 | Short   delayed descriptor replication factor |
 &nbsp;|0 08 021 | Time   significance |
 &nbsp;|0 04 025 | Time   period or displacement |
 &nbsp;|0 14 017 | Instantaneous   long-wave radiation |
 &nbsp;|0 14 018 | Instantaneous   short-wave radiation |
