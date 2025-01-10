import tkinter as tk
from tkinter import font as tkFont
import random


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("900x900+100+100")
        self.outputFont = tkFont.Font(family="Arial", size=70, slant="italic")
        self.buttonFont = tkFont.Font(family="Arial", size=50)
        
        self.rowconfigure(0,weight=100)
        self.rowconfigure(1,weight=100)
        self.rowconfigure(2,weight=100)
        self.rowconfigure(3,weight=100)
        self.rowconfigure(4,weight=100)
        self.rowconfigure(5,weight=100)
        self.columnconfigure(0,weight=100)
        self.columnconfigure(1,weight=100)
        self.columnconfigure(2,weight=100)
        

        self.outputLabel = tk.Label(self,text="Placeholder",font=self.outputFont)
        self.outputLabel.grid(row=0,column=0,sticky="NSEW",columnspan=3)
        
        self.button1 = tk.Button(self,text="1",bg="light grey",fg="black",font=self.buttonFont, command = lambda: self.digitPressed(1))
        self.button1.grid(row=1,column=0,sticky="NSEW")
        
        self.button2 = tk.Button(self,text="2",bg="light grey",fg="black",font=self.buttonFont, command = lambda: self.digitPressed(2))
        self.button2.grid(row=1,column=1,sticky="NSEW")
        
        self.button3 = tk.Button(self,text="3",bg="light grey",fg="black",font=self.buttonFont, command = lambda: self.digitPressed(3))
        self.button3.grid(row=1,column=2,sticky="NSEW")
        
        self.button4 = tk.Button(self,text="4",bg="light grey",fg="black",font=self.buttonFont, command = lambda: self.digitPressed(4))
        self.button4.grid(row=2,column=0,sticky="NSEW")
        
        self.button5 = tk.Button(self,text="5",bg="light grey",fg="black",font=self.buttonFont, command = lambda: self.digitPressed(5))
        self.button5.grid(row=2,column=1,sticky="NSEW")
        
        self.button6 = tk.Button(self,text="6",bg="light grey",fg="black",font=self.buttonFont, command = lambda: self.digitPressed(6))
        self.button6.grid(row=2,column=2,sticky="NSEW")
        
        self.button7 = tk.Button(self,text="7",bg="light grey",fg="black",font=self.buttonFont, command = lambda: self.digitPressed(7))
        self.button7.grid(row=3,column=0,sticky="NSEW")
        
        self.button8 = tk.Button(self,text="8",bg="light grey",fg="black",font=self.buttonFont, command = lambda: self.digitPressed(8))
        self.button8.grid(row=3,column=1,sticky="NSEW")
        
        self.button9 = tk.Button(self,text="9",bg="light grey",fg="black",font=self.buttonFont, command = lambda: self.digitPressed(9))
        self.button9.grid(row=3,column=2,sticky="NSEW")
        
        self.button0 = tk.Button(self,text="0",bg="light grey",fg="black",font=self.buttonFont, command = lambda: self.digitPressed(0))
        self.button0.grid(row=4,column=1,sticky="NSEW")
        
        self.buttonAdd = tk.Button(self,text="+",bg="green",fg="black",font=self.buttonFont, command = self.addPressed)
        self.buttonAdd.grid(row=5,column=0,sticky="NSEW")
        
        self.buttonEquals = tk.Button(self,text="=",bg="white",fg="black",font=self.buttonFont, command = self.equalsPressed)
        self.buttonEquals.grid(row=5,column=1,sticky="NSEW")
        
        self.buttonMinus = tk.Button(self,text="-",bg="red",fg="black",font=self.buttonFont, command = self.minusPressed)
        self.buttonMinus.grid(row=5,column=2,sticky="NSEW")
        
        self.currentNumber = ""
        self.total = 0
        self.operation = "add"
        
       
        
        self.mainloop()
        
        
    
        
    def digitPressed(self,num):
        
        self.currentNumber += str(num)
        self.outputLabel.config(text=self.currentNumber)
        
    def addPressed(self):
        self.operation = "add"
        equalsPressed()
        self.currentNumber = ""
    
    def minusPressed(self):
        self.operation = "minus"
        equalsPressed()
        self.currentNumber = ""
    
    def equalsPressed(self):
        if(self.operation == "add"):
            self.total += int(self.currentNumber)
            
        elif(self.operation == "minus"):
            self.total -= int(self.currentNumber)
        
app = App()
