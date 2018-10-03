#Developer: Tyler Smith
#Date:      11.06.16
#Purpose:   BMI class where the program can
#           use this class to find a user's
#           BMI using height and weight.

class BMI(object):
  def __init__(self, weight = 160, height = 60):    # Constructor of the class that gets ran when
    object.__init__(self)                           # an object gets instantiated with reference to
    self.setWeight(weight)                          # this class.
    self.setHeight(height)
    self.setBMI()

  def setWeight(self, weight):                      # Setter method sets the attribute width of the class
    self.weight = (weight)                          # to whatever the parameter is thats passed through 

  def getWeight(self):                              # Get method returns the value of the width attribute
    return self.weight                              # when method is called

  def setHeight(self, height):                      # Setter method sets the attribute height of the class
    self.height = (height)                          # to whatever the parameter is thats passed through

  def getHeight(self):                              # Get method returns the value of the height attribute
    return self.height                              # when the method is called
  
  def setBMI(self):                                 # Setter method sets the hidden attribute area 
    self.__BMI = (self.getWeight() / (self.getHeight() * self.getHeight())) # to width * height
    self.__BMI = self.__BMI * 703
    self.setStatus()

  def getBMI(self):                                 # Get method returns the hidden attribute area
    return self.__BMI                               # when the method is called

  BMI = property(fget = getBMI, fset = setBMI)      # This property is used to trick the person using the class
                                                    # into thinking there is a public attribute called area
  # Logic to deciding the user's status
  def setStatus(self):
    if (self.__BMI <= 18.5):                        
      self.__status = 'Underweight'
    elif(self.__BMI >= 18.51 and self.__BMI <= 24.9):
      self.__status = 'Normal'
    elif(self.__BMI >= 25 and self.__BMI <= 29.9):
      self.__status = 'Overweight'
    elif(self.__BMI >= 30):
      self.__status = 'Obese'

  def getStatus(self):                              # Get the status 
    return self.__status
