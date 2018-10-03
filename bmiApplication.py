#Developer: Tyler Smith
#Date:      11.06.16
#Purpose:   Program is intended to provide an interactive
#           GUI experience for a user to figure out what
#           their body mass index. The program also
#           lets the user know if their BMI is good or bad.

from tkinter import *       # Import tkinter library 

from bmiObject import *     # Import bmiObject library

class bmiClass(BMI):        # Inherit the properties of the rectangle class
  pass

class App(Tk):        
  def __init__(self):   # Constructor for GUI class
    Tk.__init__(self)   # 
    self.addTitle()     # Put BMI Calculator on GUI
    self.addAllLabels() # Put text labels on GUI
    self.addAllInputs() # Put input text fields on GUI
    self.addButton()    # Put calculate button on GUI

  # Put title on GUI displaying Body Mass Index Calculator
  def addTitle(self):
    Label(self, text = "Body Mass Index Calculator", font =
          ("Helvetica", "16", "bold italic")).grid(columnspan = 2)
    Label(self, text = "", font =
          ("Helvetica", "16", "bold italic")).grid(columnspan = 2)

  # Put text output on GUI where data will be displayed next to
  def addAllLabels(self):
    Label(self, text = "   Weight(lbs) :", font =
         ("Helvetica", "14")).grid(row = 2, column = 0) 
    Label(self, text = "   Height(ft) :", font =
         ("Helvetica", "14")).grid(row = 3, column = 0)
    Label(self, text = "   Height(in) :", font =
         ("Helvetica", "14")).grid(row = 4, column = 0)
    Label(self, text = "", font =
         ("Helvetica", "16")).grid(row = 5, column = 0) 
    Label(self, text = "   BMI :", font =
         ("Helvetica", "14")).grid(row = 6, column = 0)
    Label(self, text = "   Status :", font =
         ("Helvetica", "14")).grid(row = 7, column = 0)
    Label(self, text = "", font =
         ("Helvetica", "16")).grid(row = 8, column = 0) 
  

    self.lblBMI = Label(self, bg = "#fff", anchor = "w", relief = "groove")
    self.lblBMI.grid(row = 6, column = 1, sticky = "we")

    self.lblStatus = Label(self, bg = "#fff", anchor = "w", relief = "groove")
    self.lblStatus.grid(row = 7, column = 1, sticky = "we")
    
  # Put text inputs on screen for user to enter data in
  def addAllInputs(self):
    self.txt1 = Entry(self)              # Weight text input
    self.txt1.grid(row = 2, column = 1)

    self.txt2 = Entry(self)              # Height in feet input
    self.txt2.grid(row = 3, column = 1)

    self.txt3 = Entry(self)              # Height in inches input
    self.txt3.grid(row = 4, column = 1)

  # Put calculate button on GUI to calculate BMI and Status
  def addButton(self):
    self.btnCalc = Button(self, text = 'Calculate', font =
         ("Helvetica", "14"))
    self.btnCalc.grid(row = 9, columnspan = 2)
    self.btnCalc["command"] = self.calculate

  # Event that is triggered when calculate button is pushed
  def calculate(self):
    #Calculate BMI and status
    weight = int(self.txt1.get())        # Change weight string into integer 
    feet =   int(self.txt2.get())        # Change height(ft) string into integer
    inches = int(self.txt3.get())        # Change height(in) string into integer
    calculateHeight = ((12 * feet) + inches) # Convert feet to inches to calculate height
    bmi = bmiClass(weight, calculateHeight)  # Create object instance of bmiClass
    self.lblBMI["text"]    = ("%.2f" %bmi.getBMI()) # Assign BMI value to text output
    self.lblStatus["text"] = (bmi.getStatus())      # Assign Status value to text output

        
def main():
  myGui = App()                  # Instantiate myGUI object to begin building GUI  
  myGui.mainloop()

#Run main function
if(__name__ == "__main__"):
  main() 

