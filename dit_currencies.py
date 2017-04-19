import sys
sys.path.insert(0, './lib')
import prettytable
import dit_conf
import dit_io_library

class CurrencyRate():
  """
  Class Planes - keeps array of every plane
  """

  __currencies_array = []
  currencies_dict = {}

  
  def __init__(self):
    e = dit_io_library.myIoLibrary(dit_conf.config['currencyrates_file'])
    self.__currencies_array = e.getDataFromFile()
    for row in self.__currencies_array:
      self.currencies_dict[row[1]] = {'name': row[0], 'symbol': row[1], 'rate1': row[2], 'rate2': row[3] }


  def getCurrencyDict(self):
    return self.currencies_dict


  # show currency table
  def showCurrencyTable(self):
    x = prettytable.PrettyTable(["NAME","SYMBOL","RATE1","RATE2"])
    for key in self.currencies_dict:
      column2 = self.currencies_dict[key]['symbol']
      column3 = self.currencies_dict[key]['rate1']
      column4 = self.currencies_dict[key]['rate2']
      column1 = self.currencies_dict[key]['name']
      x.add_row([column1, column2, column3, column4])
    print (x)

