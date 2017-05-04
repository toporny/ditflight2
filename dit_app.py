import math
import itertools

class App():
	"""
	Class App - keeps all calculations method
	"""

	# private dict
	__appData = {}
	# private variables and array
	__elements_counter = 0
	__cheapest_trip_index = 0
	__shortest_trip_index = 0
	__chepest_price = 0
	__shortest_price = 0
	__aTravelPointsString = []
	__possible_flight_list = []
	__distance_matrix = []
	__total_price_matrix = []

	def __init__(self, oAirport, oCountry, oCurrency, oPlanes):

		self.oAirport = oAirport
		self.oPlanes = oPlanes

		for row in oAirport.airport_dict:
			airport_name = oAirport.airport_dict[row]['airportName']
			city         = oAirport.airport_dict[row]['airportCity']
			country      = oAirport.airport_dict[row]['airportCountry']
			code         = oAirport.airport_dict[row]['airportCode']
			pos_lat      = oAirport.airport_dict[row]['airportLatitude']
			pos_long     = oAirport.airport_dict[row]['airporttLongtitude']
			country_code = self.__getCountryCode(oCountry, country)
			
			if (country_code == False):
				continue

			currency_rate1 = self.__getCurrencyRate1(oCurrency, country_code)
			if (currency_rate1 == False):
				continue

			self.__appData[code] = {'airport_name':airport_name,
				'city':city,
				'country': country,
				'code': code,
				'pos_lat': pos_lat,
				'pos_long': pos_long,
				'country_code': country_code,
				'currency_rate1': currency_rate1
				}


	# get country code (objectCountry, country name)
	def __getCountryCode(self, oCountry, country_name):
		if (country_name in oCountry.countries_dict_by_name):
			return oCountry.countries_dict_by_name[country_name]['currency_code']
		else:
			#print ('Error __getCountryCode ',country_name)
			return False


	# get currency rate
	def __getCurrencyRate1(self, oCurrency, currency_code):
		if (currency_code in oCurrency.rates_dict):
			return oCurrency.rates_dict[currency_code]['rate1']
		else:
			#print ('Error __getCurrencyRate1 ',currency_code)
			return False


	# returns price for 1 liter for airport
	def __getPetrolPrice(self, airPortCodeName):
		return self.__appData[airPortCodeName]['currency_rate1']

	
	def __calculateOneDistance(self, airport1_code, airport2_code):

		lat1  = float ( self.oAirport.getAirportLatitude(airport1_code) )
		long1 = float ( self.oAirport.getAirporttLongtitude(airport1_code) )
		lat2  = float ( self.oAirport.getAirportLatitude(airport2_code) ) 
		long2 = float ( self.oAirport.getAirporttLongtitude(airport2_code) )

		if (lat1 == lat2) and (long1 == long2):
			return 0
		
		# Convert latitude and longtitude to radians
		degress_to_radians = math.pi/180.0
		phi = 90 - lat2

		# phi = 90 - latitude
		phi1 = (90.0 - lat1)*degress_to_radians
		phi2 = (90.0 - lat2)*degress_to_radians

		# theta = longtitude
		theta1 = long1 * degress_to_radians
		theta2 = long2 * degress_to_radians

		# Compute spherical distance from spherical coordinates
		cos = (math.sin(phi1)*math.sin(phi2)*math.cos(theta1 - theta2) + math.cos(phi1)*math.cos(phi2))
		arc = math.acos(cos)

		# multiply arc by the radius of the earth
		return round(6371*arc)



	# make possible flight list
	def __make_possible_flight_list(self, data_for_permutation, first_element, last_element):
		#print ("possible_fligh matrix")
		self.__possible_flight_list = []
		for l in list(data_for_permutation):
			row = [first_element] + list(l) + [last_element]
			self.__possible_flight_list.append(row)
			#print (row)


	# make airport price matrix
	def __make_airport_price_matrix(self):
		#print ("price airport matrix")
		self.__airport_price_matrix = []
		for l in self.__possible_flight_list:
			row = [];
			for element in list(l):
				row.append(self.__getPetrolPrice(element))
			self.__airport_price_matrix.append(row)
			#print (row)


	# make distance matrix
	def __make_distance_matrix(self):
		self.__distance_matrix = []
		#print ("price distance matrix")
		for i in range(0, len(self.__possible_flight_list)):
			row = [0] * (self.__elements_counter);
			for l in range(1, self.__elements_counter):
				airport_start = self.__possible_flight_list[i][l-1]
				airport_destination = self.__possible_flight_list[i][l]
				row[l] = self.__calculateOneDistance(airport_start, airport_destination)
			tmp_sum = sum(row)
			row.append(max(row))
			row.append(tmp_sum)
			#print (row)
			self.__distance_matrix.append(row)


	# make total price matrix
	def __calculate_total_price_matrix(self):
		#print ("total price matrix")
		self.__total_price_matrix = []
		for i in range(0, len(self.__possible_flight_list)):
			row = [0] * self.__elements_counter;
			for l in range(1, self.__elements_counter):
				airport_price = self.__airport_price_matrix[i][l-1]
				distance = self.__distance_matrix[i][l]

				# IMPORTANT ASSUMPTION: every plane consumes 4 liters per/km
				row[l-1] = round(distance * float(airport_price) * 4, 2)
			row.append(round(sum(row), 2)) # last column has total price tripe
			self.__total_price_matrix.append(row)
			#print (row)
		return self.__total_price_matrix



	# main alghoritm
	def calculate(self, travel_points):

		self.__elements_counter = len(travel_points)
		first_element = travel_points.pop(0) # remove first element
		last_element = travel_points.pop() # temporary remove last element as well
		travel_points = list(set(travel_points))
		data_for_permutation = itertools.permutations(travel_points)

		# create_possible_flight_list:
		self.__make_possible_flight_list(data_for_permutation, first_element, last_element )

		# lets create price matrix (price per liter in every airport)
		self.__make_airport_price_matrix()

		# now I need to have distance matrix for every possible trips
		self.__make_distance_matrix()

		# calculate total price prof every possible trip
		self.__calculate_total_price_matrix()

		# and now we have to find most economic route:
		self.__cheapest_trip_index = 0
		for i in range(0, len(self.__total_price_matrix)-1):
			if (self.__total_price_matrix[i][-1] < self.__total_price_matrix[self.__cheapest_trip_index][-1]):
				self.__cheapest_trip_index = i

		# and now we have to find shortest route:
		self.__shortest_trip_index = 0
		total_distance = 0
		for i in range(0, len(self.__distance_matrix)-1):
		 	if (self.__distance_matrix[i][-1] < self.__distance_matrix[self.__shortest_trip_index][-1]):
		 		self.__shortest_trip_index = i



	def getCheapestPrice(self):
		return round(self.__total_price_matrix[self.__cheapest_trip_index][-1])


	def getCheapestRoute(self):
		return self.__possible_flight_list[self.__cheapest_trip_index]


	def getCheapestRouteString(self):
		re = 'Cheapest:\n\n'
		counter = 1
		for i in self.__possible_flight_list[self.__cheapest_trip_index]:
			re = re + str(counter) +'. '+ i + "\n"
			counter = counter + 1 
		return re


	def getShortestPrice(self):
		return round(self.__total_price_matrix[self.__shortest_trip_index][-1])


	def getShortestRoute(self):
		return self.__possible_flight_list[self.__shortest_trip_index]


	def getShortestRouteString(self):
		re = 'Shortest:\n\n'
		counter = 1
		for i in self.__possible_flight_list[self.__shortest_trip_index]:
			re = re + str(counter) +'. '+ i + "\n"
			counter = counter + 1 
		return re


	def getLongestSingleTrip(self):
		return self.__distance_matrix[self.__cheapest_trip_index][-2]


	def getShortestKmSummary(self):
		return self.__distance_matrix[self.__shortest_trip_index][-1]

	
	def getCheapestKmSummary(self):
		return self.__distance_matrix[self.__cheapest_trip_index][-1]


	def __arrayToString(self, myArray):
		s = ''
		for i in range(0,len(myArray)-1):
		    s=s+myArray[i]+','
		s=s[:-1]
		return s


	# only for unit test - it can be deleted later on
	def getDataForUnitTest(self):
		return self.__appData

