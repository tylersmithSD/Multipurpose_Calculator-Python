#Developer: Tyler Smith
#Date:      11.06.16
#Purpose:   Gui application where the user can
#           enter in amount of feet and it is
#           converted to different types of
#           measurements used.

from tkinter import *          # Import tkinter library 

from unitObject import *       # Import unitObject library

class unitConv(unitConverter): # Clone the Unit converter class       
  pass

class unitApp(Tk):        
  def __init__(self):   # Constructor for GUI class
    Tk.__init__(self)   # 
    self.addTitle()     # Display title on GUI
    self.addAllLabels() # Display text output on GUI
    self.addAllInputs() # Display text fields where data is in on GUI
    self.addButton()    # Put button on GUI

  # Put title on GUI displaying 
  def addTitle(self):
    Label(self, text = "Measuring Unit Converter", font =
          ("Helvetica", "16", "bold italic")).grid(columnspan = 2)
    Label(self, text = "", font =
          ("Helvetica", "16", "bold italic")).grid(columnspan = 2)

  # Put text output on GUI where data will be displayed next to
  def addAllLabels(self):
    Label(self, text = "       Feet :", font =
         ("Helvetica", "14")).grid(row = 4, column = 0)
    Label(self, text = "  ", font =
         ("Helvetica", "16")).grid(row = 5, column = 0)
    Label(self, text = "   Mile(s) :", font =
         ("Helvetica", "14")).grid(row = 6, column = 0)
    Label(self, text = "   Yard(s) :", font =
         ("Helvetica", "14")).grid(row = 7, column = 0)
    Label(self, text = "   Inches :", font =
         ("Helvetica", "14")).grid(row = 8, column = 0) 
    Label(self, text = "  ", font =
         ("Helvetica", "16")).grid(row = 9, column = 0)
    Label(self, text = "   Micrometer(s):", font =
         ("Helvetica", "14")).grid(row = 10, column = 0)
    Label(self, text = "      Millimeter(s):", font =
         ("Helvetica", "14")).grid(row = 11, column = 0)
    Label(self, text = "    Centimeter(s):", font =
         ("Helvetica", "14")).grid(row = 12, column = 0)
    Label(self, text = "      Kilometer(s):", font =
         ("Helvetica", "14")).grid(row = 13, column = 0)
    Label(self, text = "  ", font =
         ("Helvetica", "16")).grid(row = 14, column = 0)
  
    # Labels where data can change, but can't be entered in by user
    self.lblMiles = Label(self, bg = "#fff", anchor = "w", relief = "groove")
    self.lblMiles.grid(row = 6, column = 1, sticky = "we")

    self.lblYards = Label(self, bg = "#fff", anchor = "w", relief = "groove")
    self.lblYards.grid(row = 7, column = 1, sticky = "we")

    self.lblInches = Label(self, bg = "#fff", anchor = "w", relief = "groove")
    self.lblInches.grid(row = 8, column = 1, sticky = "we")

    self.lblMicrometers = Label(self, bg = "#fff", anchor = "w", relief = "groove")
    self.lblMicrometers.grid(row = 10, column = 1, sticky = "we")

    self.lblMillimeters = Label(self, bg = "#fff", anchor = "w", relief = "groove")
    self.lblMillimeters.grid(row = 11, column = 1, sticky = "we")
    
    self.lblCentimeters = Label(self, bg = "#fff", anchor = "w", relief = "groove")
    self.lblCentimeters.grid(row = 12, column = 1, sticky = "we")

    self.lblKilometers = Label(self, bg = "#fff", anchor = "w", relief = "groove")
    self.lblKilometers.grid(row = 13, column = 1, sticky = "we")    
    
  # Put text inputs on screen for user to enter data in
  def addAllInputs(self):
    self.txtFeet = Entry(self)             
    self.txtFeet.grid(row = 4, column = 1)

  # Put calculate button on GUI
  def addButton(self):
    self.btnCalc = Button(self, text = 'Convert', font =
         ("Helvetica", "14"))
    self.btnCalc.grid(row = 15, columnspan = 2)
    self.btnCalc["command"] = self.calculate

  # Event that is triggered when calculate button is pushed
  def calculate(self):
    
    unitObject = unitConv(float(self.txtFeet.get()))

    # Fill data fields according to what the user entered
    self.lblMiles["text"]    = ("%.2f" %unitObject.getMiles())
    self.lblYards["text"]    = ("%.2f" %unitObject.getYards())
    self.lblInches["text"]   = ("%.2f" %unitObject.getInches())
    
    self.lblMicrometers["text"]    = ("%.2f" %unitObject.getMicrometers())
    self.lblMillimeters["text"]    = ("%.2f" %unitObject.getMillimeters())
    self.lblCentimeters["text"]    = ("%.2f" %unitObject.getCentimeters())
    self.lblKilometers["text"]     = ("%.2f" %unitObject.getKilometers()) 

        
def main():
  myGui = unitApp()       # Instantiate myGUI object to begin building GUI  
  myGui.mainloop()

#Run main function
if(__name__ == "__main__"):
  main() 

