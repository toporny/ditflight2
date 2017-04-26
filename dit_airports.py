import prettytable

class Airports():
  """
  Class Planes - keeps array of every plane
  """

  __airports = []

  
  def __init__(self, arrayOfAirPorts):
    for row in arrayOfAirPorts:
      tmp = Airport(row)
      self.__airports.append(tmp)

  

  def getAirportDataBySymbol(self, symbol):
    for row in self.__airports:
      if (row.getAirportCode() == symbol):
        return row
    raise ValueError('getAirportDataBySymbol exception error. Unknown symbol')


  def getAirportsSymbol(self):
    airport_symbols = []
    for airport in self.__airports:
      airport_symbols.append(airport.getAirportCode())
    return airport_symbols



  def showAirportsTable(self):
    x = prettytable.PrettyTable(["ID","NAME","CITY","COUNTRY","CODE"])
    for airport in self.__airports:
      row = []
      row.append(airport.getAirportId())
      row.append(airport.getAirportName()[:20])
      row.append(airport.getAirportCity()[:15])
      row.append(airport.getAirportCountry()[:13])
      row.append(airport.getAirportCode()[:5])
      x.add_row(row)
    print (x)



class Airport():
  
  def __init__(self, dataArray):
    self.__airportId          = dataArray[0]
    self.__airportName        = dataArray[1]
    self.__airportCity        = dataArray[2]
    self.__airportCountry     = dataArray[3]
    self.__airportCode        = dataArray[4]
    self.__airportCode2       = dataArray[5]
    self.__airportLatitude    = dataArray[6]
    self.__airporttLongtitude = dataArray[7]
    self.__airportIdontKnow1  = dataArray[8]
    self.__airportIdontKnow2  = dataArray[9]
    self.__airportIdontKnow3  = dataArray[10]
    self.__airportTimezone    = dataArray[11]
    self.__currencyCode       = dataArray[12] # generated based currencyrates.csv ,countrycurrency.csv
    self.__currencyRate1      = dataArray[13] # generated based currencyrates.csv ,countrycurrency.csv
    self.__currencyRate2      = dataArray[14] # generated based currencyrates.csv ,countrycurrency.csv





  def getAirportId(self):
    return self.__airportId
    
  def getAirportName(self):
    return self.__airportName
    
  def getAirportCity(self):
    return self.__airportCity
    
  def getAirportCountry(self):
    return self.__airportCountry
    
  def getAirportCode(self):
    return self.__airportCode
    
  def getAirportLatitude(self):
    return self.__airportLatitude
    
  def getAirporttLongtitude(self):
    return self.__airporttLongtitude

  def getCurrencyCode(self):
    return self.__currencyCode
    
  def getCurrencyRate1(self):
    return self.__currencyRate1

  def getCurrencyRate2(self):
    return self.__currencyRate2

    
