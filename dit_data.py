import csv
import os.path
import sys
import prettytable
sys.path.insert(0, './lib')
sys.path.insert(0, './data_csv')


class ditData():

  # constructor

  def __init__(self):

    # initializes all data
    self.__currencyrates_file = 'data_csv/currencyrates.csv'
    self.__countrycurrency_file = 'data_csv/countrycurrency.csv'
    self.__airport_file = 'data_csv/airport.csv'
    self.__aircraft_file = 'data_csv/aircraft.csv'

    self.__airport_data = []
    self.__aircraft_data = []
    self.__currencyRates = []
    self.__countryCurrency = []

    self.__assocCurrencyRates = {}
    self.__assocCountryCurrency = {}


    # Checks if all files exist
    error_array = []

    if (not(os.path.isfile(self.__airport_file))):
      error_array.append(self.__airport_file)

    if (not(os.path.isfile(self.__countrycurrency_file))):
      error_array.append(self.__countrycurrency_file)

    if (not(os.path.isfile(self.__currencyrates_file))):
      error_array.append(self.__currencyrates_file)

    if (not(os.path.isfile(self.__aircraft_file))):
      error_array.append(self.__aircraft_file)

    if (len(error_array)>0):
      print ("Fatal error occured:")
      for n in error_array:
        print (n, 'file does not exist!')
      sys.exit(1)

    # check integrity and gets data from AIRCRAFT csv file
    self.__aircraft_data = self.__getDataFromFile(self.__aircraft_file, 5, True) # True means: "ignore first row"

    # same with AIRCRAFT csv file
    self.__airport_data = self.__getDataFromFile(self.__airport_file, 12)

    # same with CURRENCY csv file
    self.__currencyRates = self.__getDataFromFile(self.__currencyrates_file, 4)

    # same with COUNTRY CURRENCY csv file
    self.__countryCurrency = self.__getDataFromFile(self.__countrycurrency_file, 20)


    # local helpers with indexes
    for row in self.__currencyRates:
      self.__assocCurrencyRates[row[1]] = [row[2], row[3]]  # currency rate for CURRENCY 

    for row in self.__countryCurrency:
      self.__assocCountryCurrency[row[15]] = row[14]  # currency rate for CURRENCY 


  # check integrity and gets data from file
  def __getDataFromFile(self, fileName, columns, passFirstLine = False):
    try:
      file  = open(fileName, "rt", encoding="utf8")
      read = csv.reader(file)
    except IOError as e:
      print ("I/O error with opening file", fileName)
      sys.exit(-1)

    __data = []
    rowcount = 0
    for row in read:
      if (passFirstLine == True):
        rowcount = rowcount + 1
      if (rowcount != 1):
        if (len(row) != columns):
          screen = terminal.get_terminal(conEmu=False)
          screen.set_color(terminal.colors["RED"])  # screen.set_color(terminal.colors["WHITE"],terminal.colors["BLUE"])
          print ("file "+ fileName+" error! line "+str(rowcount)+ '. Has to be exactly '+str(columns)+' columns!')
          screen.reset_colors()
          sys.exit(-1)
        __data.append(row)
    file.close() # close file
    return __data

     
  # gets array of planes
  def getArrayOfPlanes(self):
    return self.__aircraft_data


  # def getOneCurrency(self, currency):
  #   return self.__assocCurrencyRates[currency]


  # gets array of airports
  def getArrayOfAirports(self):
    
    new = []
    error_currency = []
    error_codes = []
    for row in self.__airport_data:
      # check if country exist in __airport_data
      if row[3].upper() in self.__assocCountryCurrency:
        tmp_currency_code = self.__assocCountryCurrency[row[3].upper()]

        # check if currency symbol exists in __assocCurrencyRates
        if (tmp_currency_code in self.__assocCurrencyRates):
          row.append(tmp_currency_code)
          row.append(self.__assocCurrencyRates[tmp_currency_code][0]) # rate1 currency
          row.append(self.__assocCurrencyRates[tmp_currency_code][1]) # rate2 currency
        else:
          error_codes.append(tmp_currency_code)
          row.append(False) # no currency code
          row.append(0) # no currency rate
          row.append(0) # no currency rate
      else:
        row.append(False)
        row.append(0) # no currency rate
        row.append(0) # no currency rate
        error_currency.append(row[3])
      new.append(row)
    
    if (error_currency):
      cleanlist = []
      [cleanlist.append(x) for x in error_currency if x not in cleanlist]
      print ("\nCSV files are inconsistent!! Calculation error may occure. Please provide consistent files.\nI can'f find currency rate for these countries:\n", cleanlist)

    if (error_codes):
      cleanlist = []
      [cleanlist.append(x) for x in error_codes if x not in cleanlist]
      print ("\nCSV files are inconsistent!! Calculation error may occure. Please provide consistent files.\nI can'f find currency codes for these codes\n", cleanlist)

    # print (new)
    # sys.exit(1)

    return new




  # show currency table
  def showCurrencyTable(self):
    x = prettytable.PrettyTable(["NAME","SYMBOL","RATE1","RATE2"])
    for cur in self.__currencyRates:
      x.add_row(cur)
    print (x)


  def showCountryCurrencyTable(self):
    x = prettytable.PrettyTable(["COUNTRY","CODE", "NAME","SYMBOL"])
    ignore_first_row = True
    for row in self.__countryCurrency:
      if (ignore_first_row):
        ignore_first_row = False
        continue
      x.add_row( [row[0][:40], row[2], row[17],row[14] ] )
    print (x)





  # gets array of currency
  def getArrayOfCurrency(self):
    return self.__currencyRates


  # gets array of country Currency
  def getArrayOfcountryCurrency(self):
    return self.__countryCurrency


  # gets array of country Currency
  def getArrayOfcountryCurrency(self):
    return self.__countryCurrency

  
