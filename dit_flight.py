import sys
sys.path.insert(0, './lib')
import dit_data
import dit_menu
import dit_price
import dit_airports
import dit_planes



# this is main class. Keeps everything inside
class ditFlight():
  
  def __init__(self):
    self.data = dit_data.ditData()
    self.planes = dit_planes.Planes(self.data.getArrayOfPlanes())
    self.airports = dit_airports.Airports(self.data.getArrayOfAirports())
    self.price = dit_price.Price(self)
    self.menu = dit_menu.Menu(self)


