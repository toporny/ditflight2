import sys
sys.path.insert(0, './lib')
import prettytable
import dit_conf
import dit_io_library

class Country():
  """
  Class Planes - keeps array of every plane
  """

  __countries_array = []
  countries_dict_by_currency = {}
  countries_dict_by_name = {}


  
  def __init__(self):
    e = dit_io_library.myIoLibrary(dit_conf.config['countrycurrency_file'])
    self.__countries_array = e.getDataFromFile()
    # print (self.__countries_array)
    # sys.exit()

    for row in self.__countries_array:
      self.countries_dict_by_currency[row[14]] = {'name': row[0], 'currency_code': row[14] }
      self.countries_dict_by_name[row[0]] = {'name': row[0], 'currency_code': row[14] }

  def getCountryDict(self):
    return self.countries_dict_by_currency



  # show currency table
  def showCountryTable(self):
    x = prettytable.PrettyTable(["CURRENCY","NAME"])
    for key in self.countries_dict_by_currency:
      column1 = self.countries_dict_by_currency[key]['currency_code']
      column2 = self.countries_dict_by_currency[key]['name']
      x.add_row([column1, column2 ])
    print (x)

