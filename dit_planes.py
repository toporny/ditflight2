import sys
sys.path.insert(0, './lib')
import prettytable
import dit_conf
import dit_io_library

class Planes():

  """
  Class Planes - keeps array of every plane
  """
  __planes_array = []
  __planes_objects = []



  def __init__(self):
    __p = dit_io_library.myIoLibrary(dit_conf.config['aircraft_file'])
    self.__planes_array = __p.getDataFromFile()
    for row in self.__planes_array:
      self.__planes_objects.append(self.Aircraft(row))


  def showPlanesTable(self):
    """
    shows all planes inside nice table
    """    
    x = prettytable.PrettyTable(['CODE','TYPE','MANUFACTURER','RANGE(km)'])
    for aircraft in self.__planes_objects:
      row = []
      row.append(aircraft.getCode())
      row.append(aircraft.getType())
      row.append(aircraft.getManufacturer())
      row.append(aircraft.getRangeKm())
      x.add_row(row)
    print (x)



  def showAvailablePlanes(self, maxRange):
    """
    shows available planes for range
    """
    x = prettytable.PrettyTable(['CODE','TYPE','MANUFACTURER','RANGE(km)'])
    for aircraft in self.__planes_objects:
      if (int(aircraft.getRangeKm()) > maxRange):
        row = []
        row.append(aircraft.getCode())
        row.append(aircraft.getType())
        row.append(aircraft.getManufacturer())
        row.append(aircraft.getRangeKm())
        x.add_row(row)
    print (x)



  class Aircraft():
    """
    Class Plane and all converting methods mile<=>km
    """
    def __init__(self, dataArray):
      self.__code = dataArray[0]
      self.__type = dataArray[1]
      self.__units = dataArray[2]
      self.__manufacturer = dataArray[3]
      self.__range = dataArray[4]

    
    def getCode(self):
      return self.__code

    
    def getType(self):
      return self.__type

    
    def getUnits(self):
      return self.__units

    
    def getManufacturer(self):
      return self.__manufacturer


      
    def getRangeMile(self):
      """
      Recognizes units and returns mile range for plane
      """
      if (self.__units == 'imperial'):
        return self.__range
      elif (self.__range == 'metric'):
        return round(int(self.__range)/1.60934)      # 1 mile = 1.6093 km
      else:
        print ("Fatal error. Plane unit not specified.")
        sys.exit(-1)


    def getRangeKm(self):
      """
      Recognizes units and returns km range for plane
      """
      if (self.__units == 'metric'):
        return self.__range
      elif (self.__units == 'imperial'):
        return round(int(self.__range)*1.60934)      # 1 mile = 1.6093 km
      else:
        print ("Fatal error. Plane unit not specified.")
        sys.exit(-1)

