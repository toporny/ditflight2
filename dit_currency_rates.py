import sys
sys.path.insert(0, './lib')
import dit_conf
import dit_io_library

class CurrencyRate():
  """
  Class Country - keeps array of every country. Indexed by currency code
  """

  __rates_array = [] # private array
  rates_dict = {} # public dict

  
  def __init__(self):
    # constructor - initialization
    e = dit_io_library.myIoLibrary(dit_conf.config['currencyrates_file'])
    self.__rates_array = e.getDataFromFile()
    for row in self.__rates_array:
      self.rates_dict[row[1]] = {'name': row[0], 'symbol': row[1], 'rate1': row[2], 'rate2': row[3] }

