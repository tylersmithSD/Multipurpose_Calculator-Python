#Developer: Tyler Smith
#Date:      11.06.16
#Purpose:   Gui interface for currency object
#           that converts American currency
#           to other foreign currencys.

from tkinter import *          # Import tkinter library 

from currencyObject import *   # Import unitObject library

class currCalc(currencyCalc):  # Clone currencyCalc class     
  pass

class currencyApp(Tk):        
  def __init__(self):   # Constructor for GUI class
    Tk.__init__(self)   # 
    self.addTitle()     # Display title on GUI
    self.addAllLabels() # Display text output on GUI
    self.addAllInputs() # Display text fields where data is in on GUI
    self.addButton()    # Put button on GUI

  # Put title on GUI 
  def addTitle(self):
    Label(self, text = "Currency Calculator", font =
          ("Helvetica", "16", "bold italic")).grid(columnspan = 2)
    Label(self, text = "", font =
          ("Helvetica", "16", "bold italic")).grid(columnspan = 2)

  # Put text output on GUI where data will be displayed next to
  def addAllLabels(self):
    Label(self, text = "    American Dollar(s) :", font =
         ("Helvetica", "14")).grid(row = 4, column = 0)
    Label(self, text = "  ", font =
         ("Helvetica", "16")).grid(row = 7, column = 0)
    Label(self, text = "   Canadian Dollar(s) :", font =
         ("Helvetica", "14")).grid(row = 8, column = 0)
    Label(self, text = "   British Pound(s) :", font =
         ("Helvetica", "14")).grid(row = 9, column = 0)
    Label(self, text = "   Euro(s) :", font =
         ("Helvetica", "14")).grid(row = 10, column = 0) 
    Label(self, text = "   Chinese Yuan(s) :", font =
         ("Helvetica", "14")).grid(row = 11, column = 0)
    Label(self, text = "    Mexican Peso(s) :", font =
         ("Helvetica", "14")).grid(row = 12, column = 0)
    Label(self, text = "  Bitcoin(s) :", font =
         ("Helvetica", "14")).grid(row = 13, column = 0)
    Label(self, text = "  ", font =
         ("Helvetica", "16")).grid(row = 14, column = 0)
    
    # Labels where data can change, but can't be entered in by user
    self.lblCanDollar = Label(self, bg = "#fff", anchor = "w", relief = "groove")
    self.lblCanDollar.grid(row = 8, column = 1, sticky = "we")

    self.lblBritPound = Label(self, bg = "#fff", anchor = "w", relief = "groove")
    self.lblBritPound.grid(row = 9, column = 1, sticky = "we")

    self.lblEuro = Label(self, bg = "#fff", anchor = "w", relief = "groove")
    self.lblEuro.grid(row = 10, column = 1, sticky = "we")

    self.lblChinYuan = Label(self, bg = "#fff", anchor = "w", relief = "groove")
    self.lblChinYuan.grid(row = 11, column = 1, sticky = "we")
    
    self.lblMexPeso = Label(self, bg = "#fff", anchor = "w", relief = "groove")
    self.lblMexPeso.grid(row = 12, column = 1, sticky = "we")

    self.lblBitcoin = Label(self, bg = "#fff", anchor = "w", relief = "groove")
    self.lblBitcoin.grid(row = 13, column = 1, sticky = "we")    
    
  # Put text inputs on screen for user to enter data in
  def addAllInputs(self):
    self.txtUSDollar = Entry(self)             
    self.txtUSDollar.grid(row = 4, column = 1)

  # Put calculate button on GUI
  def addButton(self):
    self.btnCalc = Button(self, text = 'Currency Calculate', font =
         ("Helvetica", "14"))
    self.btnCalc.grid(row = 15, columnspan = 2)
    self.btnCalc["command"] = self.calculate

  # Event that is triggered when calculate button is pushed
  def calculate(self):
    currObject = currCalc(float(self.txtUSDollar.get()))

    # Fill data fields according to what the user entered
    self.lblCanDollar["text"]  = ("%.2f" %currObject.getCanDollar())
    self.lblBritPound["text"]  = ("%.2f" %currObject.getBritPound())
    self.lblEuro["text"]       = ("%.2f" %currObject.getEuro())
    
    self.lblChinYuan["text"]   = ("%.2f" %currObject.getChinYuan())
    self.lblMexPeso["text"]    = ("%.2f" %currObject.getMexPeso())
    self.lblBitcoin["text"]    = ("%.4f" %currObject.getBitcoin()) 

def main():
  myGui = currencyApp()     # Instantiate myGUI object to begin building GUI  
  myGui.mainloop()

#Run main function
if(__name__ == "__main__"):
  main() 

