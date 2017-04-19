import sys
sys.path.insert(0, './lib')
import prettytable
import dit_conf
import dit_io_library

class Airport():
	"""
	Class Planes - keeps array of every plane
	"""

	__airport_array = []
	airport_dict = {}

  
	def __init__(self):
		e = dit_io_library.myIoLibrary(dit_conf.config['airports_file'])
		self.__airport_array = e.getDataFromFile()
		for row in self.__airport_array:
			tmp_dic = {
				'airportName':row[1],
				'airportCity':row[2],
				'airportCountry':row[3],
				'airportCode':row[4],
				'airportLatitude':row[6],
				'airporttLongtitude':row[7]
			}
			self.airport_dict[row[4]] = tmp_dic

		#print (self.airport_dict)



	def getAirportLatitude(self, airPortCode):
		return self.airport_dict[airPortCode]['airportLatitude']


	def getAirporttLongtitude(self, airPortCode):
		return self.airport_dict[airPortCode]['airporttLongtitude']


	def getAirportName(self, airPortCode):
		return self.airport_dict[airPortCode]['airportName']


	def getAirportCountry(self, airPortCode):
		return self.airport_dict[airPortCode]['airportCountry']

# 668,Lech Walesa,Gdansk,Poland,GDN,EPGD,54.377569,18.466222,489,1,E,Europe/Warsaw

	# show currency table
	def showAirportTable(self):
		x = prettytable.PrettyTable(["AIRPORT_CODE", "NAME", "CITY", "COUNTRY", "LAT", "LONG"])
		for key in self.airport_dict:
			column1 = self.airport_dict[key]['airportCode']
			column2 = self.airport_dict[key]['airportName'][:20] # limit 20
			column3 = self.airport_dict[key]['airportCity'][:20] # limit 20
			column4 = self.airport_dict[key]['airportCountry'][:20] # limit 22
			column5 = self.airport_dict[key]['airportLatitude']
			column6 = self.airport_dict[key]['airporttLongtitude']
			x.add_row([column1, column2, column3, column4, column5, column6])
		print (x)

