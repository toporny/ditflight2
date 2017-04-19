import sys
import csv
import os.path


class myIoLibrary():

  __fileName = ''
  __columns = 0
  __passFirstLine = False
  __data = []


  # constructor
  def __init__(self, fileNameParams):
    self.__fileName = fileNameParams[0]
    self.__columns = fileNameParams[1]
    self.__passFirstLine = fileNameParams[2]


  # check integrity and gets data from file
  def getDataFromFile(self):

    # check if file exist
    if (not(os.path.isfile(self.__fileName))):
      print ("File does not exist:", self.__fileName)
      sys.exit(-1)

    # check different possible type of reading error
    try:
      file  = open(self.__fileName, "rt", encoding="utf8")
      read = csv.reader(file)
    except IOError as e:
      print ("I/O error with opening file", self.__fileName)
      sys.exit(-1)

    self.__data = []
    rowcount = 0

    # check if csv file has exactly amount of columns
    for row in read:
      if (self.__passFirstLine == True):
        rowcount = rowcount + 1
      if (rowcount != 1):
        if (len(row) != self.__columns):
          print ("file "+ self.__fileName+" error! line "+str(rowcount)+ '. Has to be exactly '+str(self.__columns)+' columns!')
          sys.exit(-1)
        self.__data.append(row)
    file.close()
    return self.__data



