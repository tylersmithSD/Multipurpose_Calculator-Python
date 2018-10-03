#Developer: Tyler Smith
#Date:      11.06.16
#Purpose:   Program is intended to provide an interactive
#           GUI experience for a user to have three options
#           of which program they want to use on the main
#           popup. The three programs that the user can use
#           are the BMI calculator, Measuring unit converter,
#           and the currency calculator. 

from tkinter import *         # Import tkinter library 

from bmiApplication import *  # Import GUI from bmiProgram

class bmiApp(App):            # Refer to class so bmi GUI can run
  pass                        # when user presses button

from unitApplication import * # Import GUI from unitApplication

class unitApp(unitApp):       # Refer to class so unitApp GUI can run
  pass                        # when user presses button

from currencyApplication import * # Import GUI from currencyApplication

class currencyApp(currencyApp):   # Refer to class so currencyApp GUI can run
  pass                            # when user presses button

class mainApp(Tk):        
  def __init__(self):   # Constructor for GUI class
    Tk.__init__(self)   # 
    self.addTitle()     # Put BMI Calculator on GUI
    self.addButtons()   # Put calculate button on GUI

  # Put title on GUI
  def addTitle(self):
    Label(self, text = "Calculator / Converter Options", font =
          ("Helvetica", "16", "bold italic")).grid(columnspan = 2)
    Label(self, text = "", font =
          ("Helvetica", "16", "bold italic")).grid(columnspan = 2)

  # Put calculate button on GUI to calculate BMI and Status
  def addButtons(self):
    self.btnCalc = Button(self, text = 'BMI Calculator', font =
         ("Helvetica", "14"))
    self.btnCalc.grid(row = 2, columnspan = 2)                      # BMI Calculator button
    self.btnCalc["command"] = self.bmiTrigger

    Label(self, text = "", font =                                 
         ("Helvetica", "16", "bold italic")).grid(columnspan = 2)   # Big Space between each button 

    self.btnCalc = Button(self, text = 'Measuring Unit Converter', font =
                         ("Helvetica", "14"))
    self.btnCalc.grid(row = 4, columnspan = 2)                      # Measuring Unit Converter button
    self.btnCalc["command"] = self.unitTrigger    

    Label(self, text = "", font =                                
          ("Helvetica", "16", "bold italic")).grid(columnspan = 2)  # Big Space between each button 

    self.btnCalc = Button(self, text = 'Currency Calculator', font =
                         ("Helvetica", "14"))                       # Currency Calculator button
    self.btnCalc.grid(row = 6, columnspan = 2)
    self.btnCalc["command"] = self.currencyTrigger

    Label(self, text = "", font =
          ("Helvetica", "16", "bold italic")).grid(columnspan = 2)  # Big space after last button

  def bmiTrigger(self):                        # When BMI button is clicked, BMI application
    bmiApplicationRun  = bmiApp()              # will be ran and GUI will be displayed

  def unitTrigger(self):                       # When Unit button is clicked, Unit application
    unitApplicationRun = unitApp()             # will be ran and GUI will be displayed

  def currencyTrigger(self):                   # When Currency button is clicked, Currency application
    currencyApplicationRun = currencyApp()     # will be ran and GUI will be displayed
    
        
def main():
  mainGui = mainApp()                  # Instantiate myGUI object to begin building GUI  
  mainGui.mainloop()

#Run main function
if(__name__ == "__main__"):
  main() 

