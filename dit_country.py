import sys
sys.path.insert(0, './lib')
import dit_conf
import dit_io_library

class Country():
  """
  Class Planes - keeps array of every country
  """

  __countries_array = [] # private array
  countries_dict_by_currency = {} # public dict
  countries_dict_by_name = {} # public dict


  # constructor
  def __init__(self):
    e = dit_io_library.myIoLibrary(dit_conf.config['countrycurrency_file'])
    self.__countries_array = e.getDataFromFile()

    for row in self.__countries_array:
      self.countries_dict_by_currency[row[14]] = {'name': row[0], 'currency_code': row[14] }
      self.countries_dict_by_name[row[0]] = {'name': row[0], 'currency_code': row[14] }


  # returns whole dictionary of countries indexed by currency code
  def getCountryDict(self):
    return self.countries_dict_by_currency

