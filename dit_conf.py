# configuration data file
# sometimes file has the title (first row) what has to be ignored. For example aircraft.csv: (5 columns)
# code,type,units,manufacturer,range
# A319,jet,metric,Airbus,3750
# A320,jet,metric,Airbus,12000
# ...
# ...
# sometimes file has no tile. For example airport.csv: (12 columns)
# 2048,Herat,Herat,Afghanistan,HEA,OAHR,34.210017,62.2283,3206,4.5,U,Asia/Kabul
# 2049,Jalalabad,Jalalabad,Afghanistan,JAA,OAJL,34.399842,70.498625,1814,4.5,U,Asia/Kabul
# ...
# ...
#
# This confugoration file has costraint for title and number of columens
#
# System is able to detect if file has more column than expected

config = {
	# index                | filename                     columns,    ignore_first_row  
	'currencyrates_file'   : ['csv_data/currencyrates.csv',   4,      False],
	'countrycurrency_file' : ['csv_data/countrycurrency.csv', 20,     True ],
	'airports_file'        : ['csv_data/airport.csv',         12,     False],
	'aircraft_file'        : ['csv_data/aircraft.csv',        5,      True ]
}

