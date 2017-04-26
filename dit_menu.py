# Menu
# (all menu strings in one place)
class Menu():
  __messagesMain = ""
  __messagesSubMenu = ""
  __messagesCalculatePrice = ""

  def __init__(self, app):

    # "main" menu
    self.__messagesMain  = "\nSELECT OPTION:\n"
    self.__messagesMain += "1 - show input data\n"
    self.__messagesMain += "2 - calculate price\n"
    self.__messagesMain += "3 - help\n"
    self.__messagesMain += "q - quit\n"
    self.__app = app;

    # "show input data" menu
    self.__messagesSubMenu  = "\nSHOW INPUT DATA (type 1,2,3 or 4)\n"
    self.__messagesSubMenu += "1 - show planes\n2 - show airports list\n3 - show currency rates\n4 - show countries\n"

    # "calculate price" menu
    self.__messagesCalculatePrice = "menu MessagesCalculatePrice"


  def showMainMenu(self):
    choosen = input(self.__messagesMain)

    if (choosen == "2"):
      self.__app.price.getAirportsAndCalculate()
    return choosen;


  def showSubMenu(self):
    submenu_choosen = input(self.__messagesSubMenu)

    # 1-planes list selected
    if (submenu_choosen == '1'):
      self.__app.planes.showPlanesTable()

    # 2-airports list selected
    if (submenu_choosen == '2'):
      self.__app.airports.showAirportsTable()

    # 3-currency rates
    if (submenu_choosen == '3'):
      self.__app.data.showCurrencyTable() 

     # 4-county currency
    if (submenu_choosen == '4'):
      self.__app.data.showCountryCurrencyTable()
      print("4-country currency")

    return

