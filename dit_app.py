import sys
import math
import itertools

# http://alltic.home.pl/maps/?airports=DUB,ALC,ARW,WAW,GDN

class App():
	"""
	Class App - keeps all calculations method
	"""

	__appData = {}
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

		self.__oAirport = oAirport

		for row in oAirport.airport_dict:
			#print (airport.airport_dict[row]['airportCountry'])
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



	def __getCountryCode(self, oCountry, country_name):
		if (country_name in oCountry.countries_dict_by_name):
			return oCountry.countries_dict_by_name[country_name]['currency_code']
		else:
			#print (country_name) # error with relation files
			return False


	def __getCurrencyRate1(self, oCurrency, currency_code):
		if (currency_code in oCurrency.rates_dict):
			return oCurrency.rates_dict[currency_code]['rate1']
		else:
			# print (currency_code) # error with relation files
			return False


	def __getPetrolPrice(self, airPortCodeName):
		""" returns airport price per liter """
		# print (self.__appData[name])
		# sys.exit(1)
		return self.__appData[airPortCodeName]['currency_rate1']



	def __calculateOneDistance(self, airport1_code, airport2_code):

		lat1  = float ( self.__oAirport.getAirportLatitude(airport1_code) )
		long1 = float ( self.__oAirport.getAirporttLongtitude(airport1_code) )
		lat2  = float ( self.__oAirport.getAirportLatitude(airport2_code) ) 
		long2 = float ( self.__oAirport.getAirporttLongtitude(airport2_code) )

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



	def __create_possible_flight_list(self, data_for_permutation, first_element, last_element):
		self.__possible_flight_list = [] # new variable has name travel_points
		for l in list(data_for_permutation):
			row = [first_element] + list(l) + [last_element]
			self.__possible_flight_list.append(row)
			print (row)


	def __create_airport_price_matrix(self):
		self.__airport_price_matrix = []
		#print ('__airport_price_matrix')
		for l in self.__possible_flight_list:
			row = [];
			for element in list(l):
				row.append(self.__getPetrolPrice(element))
			print (row)
			self.__airport_price_matrix.append(row)


	def __create_distance_matrix(self):
		self.__distance_matrix = []
		# for i in __possible_flight_list:
		for i in range(0, len(self.__possible_flight_list)):
			row = [0] * (self.__elements_counter);
			for l in range(1, self.__elements_counter):
				airport_start = self.__possible_flight_list[i][l-1]
				airport_destination = self.__possible_flight_list[i][l]
				row[l] = self.__calculateOneDistance(airport_start, airport_destination)
			row.append(max(row))
			row.append(sum(row))
			print (row)
			self.__distance_matrix.append(row)


	def __calculate_total_price_matrix(self):
		self.__total_price_matrix = []
		# for i in __possible_flight_list:
		for i in range(0, len(self.__possible_flight_list)):
			row = [0] * self.__elements_counter;
			for l in range(1, self.__elements_counter):
				airport_price = self.__airport_price_matrix[i][l-1]
				distance = self.__distance_matrix[i][l]
				row[l-1] = round(distance * float(airport_price) * 5, 2)   # *5 means => 5 liters/km
			row.append(round(sum(row), 2)) # last column has total price tripe
			print (row)
			self.__total_price_matrix.append(row)
		return self.__total_price_matrix




	def calculate(self):
		#travel_points =['DUB', 'GDN', 'GLO', 'LTN', 'CVT', 'DUB']
		travel_points =['DUB', 'GDN', 'BVA', 'WAW', 'DUB']


		# a =  self.calculateOneDistance('DUB', 'GDN')
		# print (a)
		# sys.exit(1)

		self.__elements_counter = len(travel_points)
		first_element = travel_points.pop(0) # remove first element
		last_element = travel_points.pop()
		# after removing first_element travel_points has 3 elements = ['GDN','BVA','WAW']
		data_for_permutation = itertools.permutations(travel_points)
		# __data_for_permutation now equals = 
		# ('GDN', 'BVA', 'WAW'),
		# ('GDN', 'WAW', 'BVA'),
		# ('BVA', 'GDN', 'WAW'),
		# ('BVA', 'WAW', 'GDN'),
		# ('WAW', 'GDN', 'BVA'),
		# ('WAW', 'BVA', 'GDN')	

		# now I have to add starting and (the same as starting) landing point for __data_for_permutation
		

		self.__create_possible_flight_list(data_for_permutation, first_element, last_element )


		#print ('__possible_flight_list')


		
		#print (elements_counter)


		#print ("-----------")
		# __possible_flight_list now looks like this :
		# [ ['DUB', 'GDN', 'BVA', 'WAW', 'DUB'],
		#   ['DUB', 'GDN', 'WAW', 'BVA', 'DUB'],
		#   ['DUB', 'BVA', 'GDN', 'WAW', 'DUB'],
		#   ['DUB', 'BVA', 'WAW', 'GDN', 'DUB'],
		#   ['DUB', 'WAW', 'GDN', 'BVA', 'DUB'],
		#   ['DUB', 'WAW', 'BVA', 'GDN', 'DUB'] ]


		# lets create price matrix (price per liter in every airport)
		self.__create_airport_price_matrix()

		#print (len(list(__data_for_permutation)))
		#sys.exit(1)

		# price matrix looks like this:
		# ['1',    '0.2417',   '1',       '0.2417',  '1'],
		# ['1',    '0.2417',   '0.2417',  '1',       '1'],
		# ['1',    '1',        '0.2417',  '0.2417',  '1'],
		# ['1',    '1',        '0.2417',  '0.2417',  '1'],
		# ['1',    '0.2417',   '0.2417',  '1',       '1'],
		# ['1',    '0.2417',   '1',       '0.2417',  '1']

		# as project description PDF said:
		# "The cost in of fuel in airports where the local currency is not euros is assumed to be
		# the exchange rate from the local currency to euro. e.g. in you travel from London
		# to Dublin and the exchange rate is GBP1 = e1.4029 and you purchase 1000 litres
		# of fuel it will cost e1402."
		#
		# in our case we have DUB there where currency is 1 euro and 1 liter cost 1 euro
		# another airport is GDN airport and PLN currency. 1 PLN cost 0.2417 euro that means 
		# (according to PDF project specyfication 1 liter is more that 4times cheaper.)



		# now I need to have distance matrix for every possible trips
		self.__create_distance_matrix()



		#sys.exit(1)

		#print (len(list(__data_for_permutation)))
		#sys.exit(1)

		# now "__distance_matrix" for every step (beetwean airports) looks like this:
		# note: one before last element = longest_single_trip
		# last element is a sum of all trip

		# [0, 1616, 1244, 1354, 1825, 1825, 7864]
		# [0, 1616, 297, 1354, 729, 1616, 5612]
		# [0, 729, 1244, 297, 1825, 1825, 5920]
		# [0, 729, 1354, 297, 1616, 1616, 5612]
		# [0, 1825, 297, 1244, 729, 1825, 5920]
		# [0, 1825, 1354, 1244, 1616, 1825, 7864]

		# now I need to calculate price for every aiport
		# ASSUMPTION 1:
		#   because any CSV data file doesn't say how much petrol plane consumes 
		#   I assumed every plane consumes aprox 5 liters/1 km
		# ASSUMPTION 2:
		#   in every airport I buy as much (no more, no less) as I need to get destination airport.
		#   For example: for 1000km trip I need to buy 5200 liters
		# ASSUMPTION 2:
		#   in every airport I buy as much (no more, no less) as I need to get destination airport.
		#   For example: for 1000km trip I need to buy 5200 liters


		self.__calculate_total_price_matrix()

		# and price of every airport matrix look like this:
		# note: last column is a total price for sum of trip
		# [8080.0, 1503.37, 6770.0, 2205.51, 0, 18558.88]
		# [8080.0, 358.92, 1636.31, 3645.0, 0, 13720.23]
		# [3645.0, 6220.0, 358.92, 2205.51, 0, 12429.43]
		# [3645.0, 6770.0, 358.92, 1952.94, 0, 12726.86]
		# [9125.0, 358.92, 1503.37, 3645.0, 0, 14632.29]
		# [9125.0, 1636.31, 6220.0, 1952.94, 0, 18934.25]
		# 
		# considering that we have that trip example trip for this midpoints (first row on __total_price_matrix):
		# ['DUB', 'GDN', 'BVA', 'WAW', 'DUB'],
		# this is explanation of row one of __total_price_matrix
		# 8080.0 <- I need to buy fuel for 8080.0€ because distance DUB->GDN = 1616km * 1€/litr * 5liters/km= 8080
		# 1503.37 <- I need to buy fuel for 1503.37€ because distance GDN->BVA = 1244km * 0.2417€/litr * 5liters/km = 1503.37
		# 6770.0 <- I need to buy fuel for 6770.0€ because distance BVA->WAW = 1354km * 1€/litr * 5liters/km = 6770.0
		# 2205.51 <- I need to buy fuel for 2205.51€ because distance WAW->DUB = 1825km * 0.2417€/litr * 5liters/km = 2205.51
		# 0 <- I dont hahe to buy any petrol here because this is my destination point
		# 18558.88 this is total cost 8080 + 1503.37 + 6770 + 2205.51 = 18558.88

		# and now we have to find most economic route:

		self.__cheapest_trip_index = 0
		#self.__chepest_price = 0
		for i in range(0, len(self.__total_price_matrix)-1):
			if (self.__total_price_matrix[i][-1] < self.__total_price_matrix[self.__cheapest_trip_index][-1]):
				self.__cheapest_trip_index = i
		#self.__chepest_price = self.__total_price_matrix[self.__cheapest_trip_index][-1]

		# and now we have to find shortest route:
		self.__shortest_trip_index = 0
		total_distance = 0
		for i in range(0, len(self.__distance_matrix)-1):
		 	if (self.__distance_matrix[i][-1] < self.__distance_matrix[self.__shortest_trip_index][-1]):
		 		self.__shortest_trip_index = i
		# total_distance = self.__distance_matrix[self.__shortest_trip_index][-1]
		
		# return {'final_price':       self.__chepest_price,
		# 		'economic_route':      self.__possible_flight_list[self.__cheapest_trip_index],
		# 		'cheapest_trip_index': self.__cheapest_trip_index,
		# 		'shortest_trip_index': self.__shortest_trip_index,
		# 		'longest_single_trip': self.__distance_matrix[self.__cheapest_trip_index][-2],
		# 		'shortest_route':      self.__possible_flight_list[self.__shortest_trip_index],
		# 		}


	def getCheapestPrice(self):
		return self.__total_price_matrix[self.__cheapest_trip_index][-1]


	def getCheapestRoute(self):
		return self.__possible_flight_list[self.__cheapest_trip_index]


	def getShortestPrice(self):
		return self.__total_price_matrix[self.__shortest_trip_index][-1]


	def getShortestRoute(self):
		return self.__possible_flight_list[self.__shortest_trip_index]


	def getLongestSingleTrip(self):
		return self.__distance_matrix[self.__cheapest_trip_index][-2]






	# longest_single_trip


