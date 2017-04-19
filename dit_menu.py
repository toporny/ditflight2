class Menu():

	__messagesMain  = "\nSELECT OPTION:\n"
	__messagesMain += "1 - show input data\n"
	__messagesMain += "2 - calculate price\n"
	__messagesMain += "q - quit\n"


	# "show input data" menu
	__messagesSubMenu  = "\nSHOW INPUT DATA (type 1,2,3 or 4)\n"
	__messagesSubMenu += "1 - show planes\n2 - show airports list\n3 - show currency rates\n4 - show countries\n"

	# "calculate price" menu
	__messagesCalculatePrice = "menu MessagesCalculatePrice"



	def __init__(self):
		pass
		# "main" menu


	def getPossibleChoosen(self):
		__possible_choosen = {
			'11': 'planes.showPlanesTable()',
			'12': 'airport.showAirportTable()',
			'13': 'currency.showCurrencyRateTable()',
			'14': 'country.showCountryTable()'
		}
		return __possible_choosen



	def showMenu(self):
		choosen = input(self.__messagesMain)

		if (choosen == "1"):
			submenu_choosen = input(self.__messagesSubMenu)
			return (choosen+submenu_choosen)

		return choosen;

