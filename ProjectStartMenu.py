#Line to allowing the start menu module to use the Dijkstra's module.
from ProjectDijkstras import *

#Line to allowing the start menu module to use the Prim's module.
from ProjectPrims import *

#Line to allowing the start menu module to use the Kruskal's module.
from ProjectKruskals import *


#Importing the libraries for GUI and messagebox.
from tkinter import *
import tkinter
from tkinter import messagebox


#Class for the start menu interface.
class StartMenu():
    # Initialiser sets up the GUI and give the buttons their funstions.
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        # Setting up the Welcome messages
        self.welcomeLabel1 = Label(frame, text="Welcome to D1 simulations!", font=("Arial", 25), padx=1, pady=1, bd=2)
        self.welcomeLabel1.pack(side=TOP)
        self.welcomeLabel2 = Label(frame, text="Please select an algorithm to simulate.", font=("Arial", 16), padx=1,pady=1, bd=2)
        self.welcomeLabel2.pack(side=TOP)
        # Setting up the buttons to open the window of the desired algorithm
        self.kruskalsButton = Button(frame, text="Kruskal's", font=("Arial", 12), command=self.openkruskals, padx=1,pady=1, bd=2)
        self.kruskalsButton.pack(side=BOTTOM)
        self.primsButton = Button(frame, text="Prim's", font=("Arial", 12), command=self.openPrims, padx=1, pady=1,bd=2)
        self.primsButton.pack(side=BOTTOM)
        self.dijkstrasButton = Button(frame, text="Dijkstra's", font=("Arial", 12), command=self.openDijkstras, padx=1,pady=1, bd=2)
        self.dijkstrasButton.pack(side=BOTTOM)

    # Function that opens the Dijkstra's algorithm window when the button is clicked.
    def openDijkstras(self):
        # Declaring the new window as 'top2' and passing it into the 'DijkstrasGUI' class.
        top2 = Toplevel()
        DijkstrasGUI(top2)

    # Function that opens the Prim's algorithm window when the button is clicked.
    def openPrims(self):
        # Declaring the new window as 'top2' and passing it into the 'PrimsGUI' class.
        top2 = Toplevel()
        PrimsGUI(top2)

    # Function that opens the Kruskal's algorithm window when the button is clicked.
    def openkruskals(self):
        # Declaring the new window as 'top2' and passing it into the 'KruskalsGUI' class.
        top2 = Toplevel()
        KruskalsGUI(top2)