#Developer: Tyler Smith
#Date:      11.06.16
#Purpose:   Unit Converter class where the user can
#           enter in amount of feet and it is
#           converted to different types of
#           measurements used.


class unitConverter(object):
  def __init__(self, feet):        # Constructor of the class that gets ran when
    object.__init__(self)          # an object gets instantiated with reference to
    self.__setMiles(feet)          # this class.
    self.__setYards(feet)          # Go through all variables
    self.__setInches(feet)         # setting their values based on
    self.__setCentimeters()        # what data the user passes through
    self.__setMillimeters()        # when object is instantiated
    self.__setMicrometers()
    self.__setKilometers()
    
  def __setMiles(self, feet):      # Set Miles value
    self.__miles = (feet / 5280)

  def getMiles(self):              # Get Miles value
    return self.__miles

  def __setYards(self, feet):      # Set Yards value
    self.__yards = (feet / 3)

  def getYards(self):              # Get Yards value
    return self.__yards                               

  def __setInches(self, feet):     # Set Inches value
    self.__inches = (feet * 12)

  def getInches(self):             # Get Inches value
    return self.__inches

  def __setCentimeters(self):      # Set Centimeters value
    self.__centimeters = (self.getInches() * 2.54)

  def getCentimeters(self):        # Get Centimeters value
    return self.__centimeters

  def __setMillimeters(self):      # Set Millimeters value
    self.__millimeters = (self.getCentimeters() * 10)

  def getMillimeters(self):        # Get Millimeters value
    return self.__millimeters

  def __setMicrometers(self):      # Set Micrometers value
    self.__micrometers = (self.getMillimeters() * 1000)

  def getMicrometers(self):        # Get Micrometers value
    return self.__micrometers

  def __setKilometers(self):       # Set Kilometers value
    self.__kilometers = (self.getCentimeters() / 100000)

  def getKilometers(self):         # Get Kilometers value
    return self.__kilometers
    
