#Developer: Tyler Smith
#Date:      11.06.16
#Purpose:   Currency calculator class allows the user
#           to enter in American Dollars and convert
#           to other foreign currency.

class currencyCalc(object):
  def __init__(self, USDollar):          # Constructor of the class that gets ran when
    object.__init__(USDollar)            # an object gets instantiated with reference to
    self.__setCanDollar(USDollar)        # this class.
    self.__setBritPound(USDollar)        # Go through all variables
    self.__setEuro(USDollar)             # setting their values based on
    self.__setChinYuan(USDollar)         # what data the user passes through
    self.__setMexPeso(USDollar)          # when object is instantiated
    self.__setBitcoin(USDollar)
    
  def __setCanDollar(self, USDollar):    # Set Canadian dollar value
    self.__canDollar = (USDollar * 1.33) #

  def getCanDollar(self):                # Get Canadian dollar value
    return self.__canDollar              #
  
  def __setBritPound(self, USDollar):    # Set British dollar value
    self.__britPound = (USDollar * 0.81) #

  def getBritPound(self):                # Get British dollar value
    return self.__britPound              #               

  def __setEuro(self, USDollar):         # Set Euro dollar value
    self.__euro = (USDollar * 0.91)      # 

  def getEuro(self):                     # Get Euro dollar value
    return self.__euro                   #
 
  def __setChinYuan(self, USDollar):     # Set Chinese dollar value
    self.__chinYuan = (USDollar * 6.78)  #

  def getChinYuan(self):                 # Get Chinese dollar value
    return self.__chinYuan               #
  
  def __setMexPeso(self, USDollar):      # Set Mexican dollar value
    self.__mexPeso = (USDollar * 18.45)  #

  def getMexPeso(self):                  # Get Mexican dollar value
    return self.__mexPeso                #

  def __setBitcoin(self, USDollar):      # Set Bitcoin dollar value
    self.__bitcoin = (USDollar * 0.0014) #

  def getBitcoin(self):                  # Get Bitcoin dollar value
    return self.__bitcoin                #
    
