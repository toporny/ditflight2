import sys
sys.path.insert(0, './lib')
import dit_conf
import dit_io_library

class Airport():
	"""
	Class Airport - keeps array of every aiport
	"""

	__airport_array = []  # private airport array
	airport_dict = {}     # public airport array
  
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



	# checks if airport exist in database
	def airportExist(self, airPortCode):
		if (airPortCode in self.airport_dict):
			return True
		else:
			return False


	# returns airport latitude
	def getAirportLatitude(self, airPortCode):
		return self.airport_dict[airPortCode]['airportLatitude']


	# returns airport longtitude
	def getAirporttLongtitude(self, airPortCode):
		return self.airport_dict[airPortCode]['airporttLongtitude']


	# returns airport full name
	def getAirportName(self, airPortCode):
		return self.airport_dict[airPortCode]['airportName']


	# returns city name from airport record
	def getAirportCity(self, airPortCode):
		return self.airport_dict[airPortCode]['airportCity']


	# returns country name from airport record
	def getAirportCountry(self, airPortCode):
		return self.airport_dict[airPortCode]['airportCountry']

