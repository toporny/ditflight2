import sys

def CommandLine():


	if (len(sys.argv) == 1):
		print ("missing command line parameters. For help, type:")
		print ("python main.py --help")
		sys.exit(0)

	if (len(sys.argv) == 2):
		if (sys.argv[1] == "--help"):
			print ("DIT flight 1.0 by Przemyslaw Rzeznik D16127504@mydit.ie")
			print ("usage:  python main.py [airport codes separate by comma]")
			print ("example:python main.py DUB,GDN,WAW,ORK,BVA")
			print ("")
			print ("possible options:")
			print ("--show-aircrafts  :  to show input data")
			print ("--show-airports   :  to show currency data")
			print ("--show-countries  :  to show country data")
			print ("--show-rates      :  to show currency rates data")

			print ("to show possible features, type:")
			print ("python main.py --help")
			sys.exit(0)

	return_val = False

	if (sys.argv[1] == "--show-aircrafts"):
		return_val = 'planes.showPlanesTable()'

	elif (sys.argv[1] == "--show-airports"):
		return_val ='airport.showAirportTable()'

	elif (sys.argv[1] == "--show-currency"):
		return_val ='currency.showCurrencyRateTable()'
	
	elif (sys.argv[1] == "--show-countries"):
		return_val ='country.showCountryTable()'

	elif ("," in sys.argv[1]):
		airports = sys.argv[1].upper().split(',')
		airports.append(airports[0])
		return_val = airports
		print (return_val)



	if (return_val == False):
		print ("Unknown options")
		sys.exit(1)

	return return_val
