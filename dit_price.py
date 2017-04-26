import math
import sys
import itertools


class Price():

	def __init__(self, app):
		# initializes all data
		self.__app = app
		self.__aTravelPoints = []



	def __checkInputData(self, sAairports):
		""" checks input format data """
		""" expected format data is: DUB,GDA,LON """

		good_data_format = True
		self.__aTravelPoints = []

		# make upper case for whole string
		sAairports = sAairports.upper();
		
		# remove spaces from whole string "DUB, GDA , WAW" => "DUB,GDA,WAW"
		sAairports = sAairports.replace(" ", "")

		# split to array with 3chars code
		splitted = sAairports.split(',')

		# test if it is at least two airports and max 5
		if ((len(splitted) <= 1) or (len(splitted) > 6)):
			print ("please type minimum two airports codename and maximum 6 !!!")
			good_data_format = False

		# test if every code has exactly three chars
		for x in splitted:
			if (len(x) != 3):
				print ("Wrong airport code (",x,").Every airport code should have exactly 3 chars !!!")
				good_data_format = False

		# test if input data array has duplicated values?
		# cleanlist = []
		# [cleanlist.append(x) for x in splitted if x not in cleanlist]
		# if (len(cleanlist) != len(splitted)):
		# 	print ("Every airport code has to be unique")
		# 	return False

		#or codes can not be placed one by one
		old = ''
		for x in splitted:
			if (x == old):
				print ("The same airport codes can't be placed one by one!")
				good_data_format = False
			old = x;


		# test if every airpot exist in datbase
		for code in splitted:
			code_airport_check = False
			if (code in self.__app.airports.getAirportsSymbol()):
				code_airport_check = True
			if (code_airport_check == False):
				print ("I can't find airport code (",code,") in database !!!")
				good_data_format = False

		# if everything is ok store points in self.__aTravelPoints array
		if (good_data_format != False):
			self.__aTravelPoints = splitted

		#return array or false
		return good_data_format



	def __calculateDistance(self, lat1_string, long1_string, lat2_string, long2_string):
		
		lat1  = float (lat1_string)
		long1 = float (long1_string)
		lat2  = float (lat2_string)
		long2 = float (long2_string)

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

		# Remember to multiply arc by the radius of the earth
		return round(arc*6371)


	def __calculateTotalDistance(self, stopsArray):
		""" calculate Total distance beetwean stops """

		totalDistance = 0;
		# extend stopsArray for return way (zero index position)
		stopsArray.append(stopsArray[0])

		index = 0
		while (index < len(stopsArray)-1):
			lat1  = self.__app.airports.getAirportDataBySymbol(stopsArray[index]).getAirportLatitude()
			long1 = self.__app.airports.getAirportDataBySymbol(stopsArray[index]).getAirporttLongtitude()
			lat2  = self.__app.airports.getAirportDataBySymbol(stopsArray[index+1]).getAirportLatitude()
			long2 = self.__app.airports.getAirportDataBySymbol(stopsArray[index+1]).getAirporttLongtitude()
			totalDistance = totalDistance + self.__calculateDistance(lat1, long1, lat2, long2)
			index = index + 1

		# print (stopsArray[len(stopsArray)-1])
		# lat1  = self.__app.airports.getAirportDataBySymbol(stopsArray[index+1]).getAirportLatitude()
		# long1 = self.__app.airports.getAirportDataBySymbol(stopsArray[index+1]).getAirporttLongtitude()
		# lat2  = self.__app.airports.getAirportDataBySymbol(stopsArray[0]).getAirportLatitude()
		# long2 = self.__app.airports.getAirportDataBySymbol(stopsArray[0]).getAirporttLongtitude()
		# totalDistance = totalDistance + self.__calculateDistance(lat1, long1, lat2, long2)
		
		# print (totalDistance)

		# sys.exit(1)
		# print (stopsArray)
		# print (totalDistance)
		return totalDistance






	def __calculatePrice(self):
		""" calculates the distance and price by sAairports array as a param """
		if (isinstance(self.__aTravelPoints, list) and (len(self.__aTravelPoints)>1)):
			pass # means ok
		else:
			raise ValueError('__calculatePrice() exception error. (self__aTravelPoints) has to be set in this place.')


		print (self.__aTravelPoints)
		sys.exit(1)
		# create matrix of permutation (all possible directions through all airports)

		list_before_first_element = self.__aTravelPoints
		
		#totalDistance  = self.__calculateTotalDistance(self.__aTravelPoints)

		#sys.exit(1)

		first_element = list_before_first_element.pop(0)
		my_permutations = itertools.permutations(list_before_first_element)

		# prepare array with all possible route (permutation calculation)
		#all_possible_directions = []

		result = []
		for l in list(my_permutations):
			final_list = [first_element]+list(l)
			totalDistance  = self.__calculateTotalDistance(final_list)
			result.append([final_list,totalDistance])
			#print ('final_list',final_list)
			#print ('totalDistance',totalDistance)
			#all_possible_directions.append(final_list)
		#print (all_possible_directions)

		# find shortest way
		final_way = result[0][0]
		final_distance = result[0][1]
		for way in result:
			if (way[1]<final_distance):
				final_way = way[0]
				final_distance = way[1]

				# print ("shortest way")
				# print ([final_way,final_distance])



	def getAirportsAndCalculate(self):

		# debug mode
#		self.__calculatePrice();
#		return 

		# self.__checkInputData('DUB, GDN, BVA, WAW, ORK, BZG')
		self.__aTravelPoints = ['DUB','GDN','BVA','WAW','ORK','BZG']
		self.__calculatePrice()

		sys.exit(1)
		
		success = False
		while (not success):
			print ("\nType airports separated by comma (max 5) or blank to exit.")
			print ("For example: DUB,GDA,BVA")
			sAairports = input()
			if (self.__checkInputData(sAairports)):
				print ("do calculation...")
				break
			else:
				print ("repeat insert data...")
		return
