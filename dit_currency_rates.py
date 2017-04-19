import sys
sys.path.insert(0, './lib')
import prettytable
import dit_conf
import dit_io_library

class CurrencyRate():
  """
  Class Country - keeps array of every country. Indexed by currency code
  """

  __rates_array = []
  rates_dict = {}

  
  def __init__(self):
    e = dit_io_library.myIoLibrary(dit_conf.config['currencyrates_file'])
    self.__rates_array = e.getDataFromFile()
    for row in self.__rates_array:
      self.rates_dict[row[1]] = {'name': row[0], 'symbol': row[1], 'rate1': row[2], 'rate2': row[3] }

  # show currency table
  def showCurrencyRateTable(self):
    x = prettytable.PrettyTable(["NAME","SYMBOL","RATE1","RATE2"])
    for key in self.rates_dict:
      column2 = self.rates_dict[key]['symbol']
      column3 = self.rates_dict[key]['rate1']
      column4 = self.rates_dict[key]['rate2']
      column1 = self.rates_dict[key]['name']
      x.add_row([column1, column2, column3, column4])
    print (x)

