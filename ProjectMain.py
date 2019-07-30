#Line to allowing the main module to use the start menu module.
from ProjectStartMenu import *


#Importing the libraries for GUI.
import tkinter


#Creates the window as 'top' and passes 'top' into the 'StartMenu' class.
top = tkinter.Tk()
top.geometry("500x500")
b = StartMenu(top)
top.mainloop()