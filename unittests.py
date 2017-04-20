import unittest
import dit_planes
import dit_currency_rates
import dit_io_library
import dit_airport
import dit_country
import dit_command_line
import dit_app
import sys


class TestedValues(unittest.TestCase):  
	__app = ''

	# if airport exist (assertTrue)
	def test_airport_exist(self):
		airp = dit_airport.Airport()
		self.assertTrue(airp.airportExist('DUB'))


	# if airport not exist (assertFalse)
	def test_airport_not_exist(self):
		airp = dit_airport.Airport()
		self.assertFalse(airp.airportExist('XXX'))


	# test airport/latitude (assertEqual)
	def test_airPortLatitude(self):
		airp = dit_airport.Airport()
		lat = airp.getAirportLatitude('DUB')
		expected_result = '53.421333'
		self.assertEqual(lat, expected_result)


	# test airport/longtitude
	def test_airPortLongtitude(self):
		airp = dit_airport.Airport()
		lat = airp.getAirporttLongtitude('DUB')
		expected_result = '-6.270075'
		self.assertEqual(lat, expected_result)


	# test airport/longtitude (assertIn)
	def test_planesArray(self):
		planes = dit_planes.Planes()
		#this row suppose to be in array
		example_row = ['737','jet','imperial','Boeing','5600']
		self.assertIn(example_row, planes.getPlanesArray() )


	# test currency exist (assertTrue)
	def test_currencyExist(self):
		currency = dit_currency_rates.CurrencyRate()
		self.assertTrue('PLN' in currency.rates_dict)


	# test currency not exist (assertFalse)
	def test_currencyExist(self):
		currency = dit_currency_rates.CurrencyRate()
		self.assertFalse('XXX' in currency.rates_dict) ## XXX currency not exist


	# test distance beetwean two airports
	def test_currencyExist(self):
		currency = dit_currency_rates.CurrencyRate()
		self.assertFalse('XXX' in currency.rates_dict) ## XXX currency not exist


	def test_cheapestPrice(self):
		trip = ['DUB', 'BVA', 'GDN', 'MSQ', 'DUB']
		planes = dit_planes.Planes()
		currency = dit_currency_rates.CurrencyRate()
		airport = dit_airport.Airport()
		country = dit_country.Country()
		self.__app = dit_app.App(airport, country, currency, planes)
		self.__app.calculate(trip)
		cheapestPrice = self.__app.getCheapestPrice()
		self.assertEqual( 8496.81, cheapestPrice )


	def test_shortestPrice(self):
		trip = ['DUB', 'BVA', 'GDN', 'MSQ', 'DUB']
		planes = dit_planes.Planes()
		currency = dit_currency_rates.CurrencyRate()
		airport = dit_airport.Airport()
		country = dit_country.Country()
		self.__app = dit_app.App(airport, country, currency, planes)
		self.__app.calculate(trip)		
		shortestPrice = self.__app.getShortestPrice()
		self.assertEqual(11846.51, shortestPrice )


	def test_longestSingleTrip(self):
		trip = ['DUB', 'BVA', 'GDN', 'MSQ', 'DUB']
		planes = dit_planes.Planes()
		currency = dit_currency_rates.CurrencyRate()
		airport = dit_airport.Airport()
		country = dit_country.Country()
		self.__app = dit_app.App(airport, country, currency, planes)
		self.__app.calculate(trip)
		longestSingleTrip = self.__app.getLongestSingleTrip()
		self.assertEqual(2239, longestSingleTrip )


	def test_cheapestRoute(self):
		trip = ['DUB', 'BVA', 'GDN', 'MSQ', 'DUB']
		planes = dit_planes.Planes()
		currency = dit_currency_rates.CurrencyRate()
		airport = dit_airport.Airport()
		country = dit_country.Country()
		self.__app = dit_app.App(airport, country, currency, planes)
		self.__app.calculate(trip)
		cheapestRoute = self.__app.getCheapestRoute()
		longestSingleTrip = self.__app.getLongestSingleTrip()
		self.assertEqual(['DUB', 'BVA', 'GDN', 'MSQ', 'DUB'], cheapestRoute)		 



if __name__ == '__main__':
	unittest.main()

