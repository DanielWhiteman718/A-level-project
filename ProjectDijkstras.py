#Importing the libraries for GUI and messagebox.
from tkinter import *
import tkinter
from tkinter import messagebox


#Class for the dijkstra's algorithm interface.
class DijkstrasGUI():
    #Initialiser sets up the GUI and give the widgets their funstions. - COMMMENTED
    def __init__(self, master):
        #Setting up variables and data structures.
        self.startNodeTrue = False
        self.endNodeTrue = False
        self.alphabetCount = 0
        self.labelCoordinates = []
        self.boxCoordinates = []
        self.stepClicked = False
        self.alphabet = []
        self.edgeCoordsTemp = []
        self.edgeCoordinates = []
        for letter in range(65, 91):
            self.alphabet.append(chr(letter))
        self.startEdge = True
        self.buildNode = False
        self.buildEdge = False
        self.buildOrNah = False
        self.nodes = []
        self.edgesNames = []
        self.edgesWeight = []
        self.nodeCoordinates = {}

        #Setting up different frames to organise the GUI.
        self.mainFrame = Frame(master)
        self.mainFrame.pack(side=TOP)
        self.buildFrame = Frame(master)
        self.buildFrame.pack(side=RIGHT)
        simFrame = Frame(master)
        simFrame.pack(side=LEFT)

        #Setting up the canvas so the diagram can be shown in the middle of the GUI.
        #The canvas will trigger the 'addNode' function when left clicked.
        self.C = tkinter.Canvas(master, bg="white", height=650, width=950)
        self.C.bind("<Button-1>", self.addNode)
        self.C.pack(side = BOTTOM)

        #Setting up the widgets for the GUI and giving them their functions.
        self.dijkstrasLabel = Label(self.mainFrame, text="Dijkstra's Algorithm", font=("Arial", 25))
        self.dijkstrasLabel.pack()
        self.instructionsButton = Button(self.buildFrame, text="Instructions", font=("Arial", 12), padx=1, pady=1, bd=2,command=self.provideInstructions)
        self.instructionsButton.pack()
        self.spaceLabel = Label(self.buildFrame, text="", pady=60)
        self.spaceLabel.pack()
        self.newNodeButton = Button(self.buildFrame, text="Add node", font=("Arial", 12), padx = 1, pady = 1, bd = 2, command=self.addNodeMode)
        self.newNodeButton.pack()
        self.spaceLabel = Label(self.buildFrame,text="",pady=10)
        self.spaceLabel.pack()
        self.newEdgeButton = Button(self.buildFrame, text="Add edge", font=("Arial", 12), padx = 1, pady = 1, bd = 2, command=self.addEdgeMode)
        self.newEdgeButton.pack()
        self.spaceLabel2 = Label(self.buildFrame,text="",pady=40)
        self.spaceLabel2.pack()
        self.stepButton = Button(simFrame, text="Step", font=("Arial", 12), padx = 1, pady = 1, bd = 2, command=self.StepClicked)
        self.stepButton.pack()
        self.L1 = Label(self.mainFrame, text=(""),font=("Arial", 10))
        self.L1.pack(side=RIGHT)
        self.skipButton = Button(simFrame, text="Skip to solution", font=("Arial", 12), padx = 1, pady = 1, bd = 2, command=self.performAlgorithmSkip)
        self.skipButton.pack()

    #Function to put the app in the right 'mode' to add nodes to the canvas. - COMMMENTED
    def addNodeMode(self):
        #Using 'buildNode' status to turn the 'add node mode' on or off.
        if self.buildNode == False:
            self.buildNode = True
            self.buildEdge = False
        else:
            self.buildNode = False

    #Function to put the app in the right 'mode' to add edges to the canvas. - COMMMENTED
    def addEdgeMode(self):
        #Using 'buildEdge' status to turn the 'add edge mode' on or off.
        if self.buildEdge == False:
            self.buildEdge = True
            self.buildNode = False
        else:
            self.buildEdge = False

    #Function to save the edge weight when entered into the pop up window. - COMMMENTED
    def saveEdgeWeight(self):
        #Checking the edge weight is entered with the correct data type.
        #Only creating edge when the weight has been entered.
        self.startEdge = True
        try:
            self.edgesWeight.append(float(self.edgeWeightEntry.get()))
        except ValueError:
            messagebox.showinfo("Warning","Your edge must have a weight.")
        self.C.create_text((self.startCoords[0] + self.endCoords[0]) / 2, (self.startCoords[1] + self.endCoords[1]) / 2, text=str((float(self.edgeWeightEntry.get()))), font=("Arial", 12))
        self.top3.destroy()
        self.edgeCoordsTemp.append(self.endCoords)
        self.edgeCoordinates.append(self.edgeCoordsTemp)
        self.C.tag_lower(self.C.create_line(self.startCoords, self.endCoords, fill="red", width=5, tags="A1Tag"))
        self.edgesNames.append(self.edgeName1)

    #Function to add an edge to the canvas. - COMMMENTED
    def addEdge(self, event):
        #Checking that the app is in the 'build edge mode'.
        if self.buildEdge == True:
            #If the first node(to be connected by edge) has bee clicked...
            if self.startEdge == True:
                #Getting name and coordinates of the start node.
                self.edgeCoordsTemp = []
                i = 0
                self.edgeStartNode = ("")
                while self.edgeStartNode == (""):
                    if (event.x) > (self.nodeCoordinates[self.alphabet[i]][0]):
                        if (event.x) < (self.nodeCoordinates[self.alphabet[i]][2]):
                            if (event.y) > (self.nodeCoordinates[self.alphabet[i]][1]):
                                if (event.y) < (self.nodeCoordinates[self.alphabet[i]][3]):
                                    self.edgeStartNode = self.alphabet[i]
                    i = i + 1
                self.startCoords = [event.x, event.y]
                self.edgeCoordsTemp.append(self.startCoords)
                self.startEdge = False

            #If the second node(to be connected by edge) has been clicked...
            elif self.startEdge == False:
                #Getting name and coordinates of the end node.
                i = 0
                self.edgeEndNode = ("")
                while self.edgeEndNode == (""):
                    if (event.x) > (self.nodeCoordinates[self.alphabet[i]][0]):
                        if (event.x) < (self.nodeCoordinates[self.alphabet[i]][2]):
                            if (event.y) > (self.nodeCoordinates[self.alphabet[i]][1]):
                                if (event.y) < (self.nodeCoordinates[self.alphabet[i]][3]):
                                    self.edgeEndNode = self.alphabet[i]
                    i = i + 1

                #Checking that the edge has not already been added.
                #If the edge doesn't already exist then the app will create window to add the edge weight.
                self.edgeName1 = ''.join((self.edgeStartNode, self.edgeEndNode))
                self.edgeName2 = ''.join((self.edgeEndNode, self.edgeStartNode))
                if (self.edgeName1 not in self.edgesNames) and (self.edgeName2 not in self.edgesNames):
                    self.endCoords = [event.x, event.y]
                    self.startEdge = True
                    ###############################################
                    self.top3 = tkinter.Tk()
                    self.edgeEntryLabel = Label(self.top3, text="Enter the edge weight")
                    self.edgeEntryLabel.pack()
                    self.edgeWeightEntry = Entry(self.top3, bd=1)
                    self.edgeWeightEntry.pack()
                    self.edgeWeightButton = Button(self.top3, text="Enter", bd=2, command=self.saveEdgeWeight)
                    self.edgeWeightButton.pack()
                    self.top3.geometry("200x100")
                    self.top3.mainloop()
                else:
                    messagebox.showinfo("Warning","This edge already exists.")
                    self.startEdge = True

    #Function to show node options when right clicked by the user. - COMMMENTED
    def rightClickOptions(self, event):
        #Creates a window with different options as buttons.
        self.top3 = tkinter.Tk()
        self.rightClickLabel = Label(self.top3, text="Options")
        self.rightClickLabel.pack()
        self.rightClickButton1 = Button(self.top3, text="Make start node", command=self.saveStartNode)
        self.rightClickButton1.pack()
        self.rightClickButton2 = Button(self.top3, text="Make end node", command = self.saveEndNode)
        self.rightClickButton2.pack()
        self.clickCoordsX = event.x
        self.clickCoordsY = event.y
        self.top3.mainloop()

    #Function to add a node to the camvas. - COMMMENTED
    def addNode(self, event):
        #Checking that the app is in the correct mode.
        if self.buildNode == True:
            #Create the node on the canvas, labelled with its name and saves its information in the correct data structures.
            #Creates boxes under the node for the permanent and temporary labels.
            #Saves coordinates of positions where annotations can be put such as permanent and temporary labels.
            labelCoordsTemp = []
            labelCoordsPermanent = []
            labelCoordsComb = []
            box1 = []
            box2 = []
            boxComb = []
            self.C.create_arc(event.x,event.y,(event.x)+40,(event.y)+40, start=0, extent=359, fill="red", tags=("A1Tag","A2Tag"))
            self.C.create_text((event.x)+20,(event.y)+20, fill="white", font="Arial", text=str(self.alphabet[self.alphabetCount]), tags=("A1Tag","A2Tag"))
            self.C.create_rectangle(event.x,(event.y)+60,(event.x)+30,(event.y)+80,fill="white")
            box1.append([event.x, (event.y)+60, (event.x) + 30, (event.y) + 80])
            self.C.create_rectangle((event.x)+30,(event.y)+60,(event.x)+60,(event.y)+80,fill="white")
            box2.append([(event.x) + 30, (event.y) + 60, (event.x) + 60, (event.y) + 80])
            self.C.create_text((event.x)+15,(event.y)+70,fill="black",font="Arial",text=str(0))
            self.C.create_text((event.x)+45,(event.y)+70,fill="black",font="Arial",text=str(0))
            self.C.tag_bind('A1Tag', '<ButtonPress-1>', self.addEdge)
            self.C.tag_bind('A2Tag', '<ButtonPress-3>', self.rightClickOptions)
            self.nodes.append(self.alphabet[self.alphabetCount])
            self.nodeCoordinates[self.alphabet[self.alphabetCount]] = [event.x,event.y,(event.x)+40,(event.y)+40]
            self.alphabetCount = self.alphabetCount + 1
            boxComb.append(box1)
            boxComb.append(box2)
            self.boxCoordinates.append(boxComb)
            labelCoordsTemp.append((event.x)+15)
            labelCoordsTemp.append((event.y)+70)
            labelCoordsPermanent.append((event.x)+45)
            labelCoordsPermanent.append((event.y)+70)
            labelCoordsComb.append(labelCoordsTemp)
            labelCoordsComb.append(labelCoordsPermanent)
            self.labelCoordinates.append(labelCoordsComb)

    #Function to save the start node. - COMMMENTED
    def saveStartNode(self):
        #Using the coordinates of the right click event to check which node was clicked.
        #Do this by getting coordates of node and comparing them to event coordinates.
        i = 0
        for count in range(len(self.nodes)):
            if self.clickCoordsX > self.nodeCoordinates[self.nodes[i]][0]:
                if self.clickCoordsX < self.nodeCoordinates[self.nodes[i]][2]:
                    if self.clickCoordsY > self.nodeCoordinates[self.nodes[i]][1]:
                        if self.clickCoordsY < self.nodeCoordinates[self.nodes[i]][3]:
                            self.startNode = self.nodes[i]
                            self.startNodeTrue = True
                            self.top3.destroy()
            i = i + 1

    #Function to save the end node. - COMMMENTED
    def saveEndNode(self):
        #Using the coordinates of the right click event to check which node was clicked.
        #Do this by getting coordates of node and comparing them to event coordinates.
        i = 0
        for count in range(len(self.nodes)):
            if self.clickCoordsX > self.nodeCoordinates[self.nodes[i]][0]:
                if self.clickCoordsX < self.nodeCoordinates[self.nodes[i]][2]:
                    if self.clickCoordsY > self.nodeCoordinates[self.nodes[i]][1]:
                        if self.clickCoordsY < self.nodeCoordinates[self.nodes[i]][3]:
                            self.endNode = self.nodes[i]
                            self.endNodeTrue = True
                            self.top3.destroy()
            i = i + 1

    #Function to control the algorithm with the 'skip' button. - COMMMENTED
    def performAlgorithmSkip(self):
        #Checking that the user has picked a start node and an end node.
        if (self.startNodeTrue == True) and (self.endNodeTrue == True):
            #declares the necessary data structures.
            nodeLabels = []
            i = 0
            for count in range(len(self.nodes)):
                nodeLabels.append([0, 0])
                i = i + 1
            labelCoordsDict = dict(zip(self.nodes,self.labelCoordinates))
            boxCoordsDict = dict(zip(self.nodes,self.boxCoordinates))
            nodeValues = dict(zip(self.nodes, nodeLabels))
            edgeValues = dict(zip(self.edgesNames, self.edgesWeight))
            temporaryLabelled = []
            permanentLabelled = []

            #Updates the labels of the start node.
            nodeValues[self.startNode][0] = 1
            subjectNode = self.startNode
            self.C.create_rectangle(boxCoordsDict[self.startNode][0],fill="white")
            self.C.create_text(labelCoordsDict[self.startNode][0],text=str(nodeValues[self.startNode][0]))
            permanentLabelled.append(self.startNode)

            #Main loop for Dijkstra's algorithm.
            a = 2
            while len(permanentLabelled) < len(self.nodes):
                #For each edge connected to subject node, split it up into individual nodes and updates the labels if necessary.
                i = 0
                for count in range(len(self.edgesNames)):
                    splitEdgeNames = [self.edgesNames[i][0], self.edgesNames[i][1]]

                    if subjectNode in splitEdgeNames:
                        subjectIndex = splitEdgeNames.index(subjectNode)
                        if subjectIndex == 0:
                            otherNode = splitEdgeNames[1]
                        else:
                            otherNode = splitEdgeNames[0]
                        if otherNode not in permanentLabelled:
                            newLabel = nodeValues[subjectNode][1] + edgeValues[self.edgesNames[i]]
                            if nodeValues[otherNode][1] == 0:
                                nodeValues[otherNode][1] = newLabel
                                self.C.create_rectangle(boxCoordsDict[otherNode][1], fill="white")
                                self.C.create_text(labelCoordsDict[otherNode][1],text=str(nodeValues[otherNode][1]))

                                temporaryLabelled.append(otherNode)
                            else:
                                if newLabel < nodeValues[otherNode][1]:
                                    nodeValues[otherNode][1] = newLabel
                                    self.C.create_rectangle(boxCoordsDict[otherNode][1], fill="white")
                                    self.C.create_text(labelCoordsDict[otherNode][1], text=str(nodeValues[otherNode][1]))
                    i = i + 1

                #Decides which node gets a permanent label.
                i = 0
                permanentContendersLabels = []
                for count in range(len(temporaryLabelled)):
                    permanentContendersLabels.append(nodeValues[temporaryLabelled[i]][1])
                    i = i + 1
                permanentContendersLabels.sort()

                i = 0
                for count in range(len(self.nodes)):
                    if nodeValues[self.nodes[i]][1] == permanentContendersLabels[0]:
                        if self.nodes[i] in temporaryLabelled:
                            newPermanentNode = self.nodes[i]
                    i = i + 1

                nodeValues[newPermanentNode][0] = a
                self.C.create_rectangle(boxCoordsDict[newPermanentNode][0], fill="white")#del
                self.C.create_text(labelCoordsDict[newPermanentNode][0], text=str(nodeValues[newPermanentNode][0]))#del
                subjectNode = newPermanentNode
                a = a + 1
                permanentLabelled.append(newPermanentNode)
                temporaryLabelled.remove(newPermanentNode)


            #Finds the route by subtracting back through the graph until you get back to the start node.
            route = [self.endNode]
            subjectNode = self.endNode
            while subjectNode != self.startNode:
                i = 0
                for count in range(len(self.edgesNames)):
                    splitEdgeNames = [self.edgesNames[i][0], self.edgesNames[i][1]]

                    if subjectNode in splitEdgeNames:

                        subjectIndex = splitEdgeNames.index(subjectNode)
                        if subjectIndex == 0:
                            otherNode = splitEdgeNames[1]
                        else:
                            otherNode = splitEdgeNames[0]

                        if (nodeValues[subjectNode][1]) - (edgeValues[self.edgesNames[i]]) == nodeValues[otherNode][1]:
                            route.append(otherNode)
                            subjectNode = otherNode
                    i = i + 1
            route = route[::-1]



            # Finds the route by subtracting back through the graph until you get back to the start node.
            i = 0
            edges = []
            for count in range((len(route)) - 1):
                start = route[i]
                end = route[i + 1]
                edge = start + end
                edges.append(edge)
                i = i + 1

            edgeCoordsDict = dict(zip(self.edgesNames, self.edgeCoordinates))
            i = 0
            for count in range(len(edges)):
                if edges[i] in edgeCoordsDict:
                    startCoords = edgeCoordsDict[edges[i]][0]
                    endCoords = edgeCoordsDict[edges[i]][1]
                else:
                    startCoords = edgeCoordsDict[edges[i][1] + edges[i][0]][0]
                    endCoords = edgeCoordsDict[edges[i][1] + edges[i][0]][1]
                self.C.create_line(startCoords, endCoords, fill="green", width=5)
                i = i + 1

            i = 0
            for count in range(len(route)):
                self.C.create_arc(self.nodeCoordinates[route[i]][0], self.nodeCoordinates[route[i]][1], self.nodeCoordinates[route[i]][2], self.nodeCoordinates[route[i]][3], start=0, extent=359, fill="green")
                self.C.create_text((self.nodeCoordinates[route[i]][0])+20, (self.nodeCoordinates[route[i]][1])+20, fill="white", font="Arial",text=str(route[i]))
                i = i + 1
            i = 0
            for count in range(len(self.nodes)):
                self.C.create_rectangle(boxCoordsDict[self.nodes[i]][1], fill="white")
                self.C.create_text(labelCoordsDict[self.nodes[i]][1], text=str(nodeValues[self.nodes[i]][1]))
                self.C.create_rectangle(boxCoordsDict[self.nodes[i]][0], fill="white")
                self.C.create_text(labelCoordsDict[self.nodes[i]][0], text=str(nodeValues[self.nodes[i]][0]))
                i = i + 1
            messagebox.showinfo("Solution", ("The shortest possible route from ", self.startNode, " to ", self.endNode, " has a weight of ", nodeValues[self.endNode][1], " and takes the route: ", route))
        else:
            messagebox.showinfo("Warning","You must select both a start and end node before running the algorithm.")

    #Function to declare all the data structures when the 'step' button is first clicked. - COMMMENTED
    def StepClicked(self):
        #Checking the user has picked a start and end node.
        if (self.startNodeTrue == True) and (self.endNodeTrue == True):
            #If 'step' button has already been clicked then go straight to 'performAlgorithmSkip', if not declare all data structures first.
            if self.stepClicked == True:
                self.performAlgorithmStep()
            if (self.stepClicked == False):
                explanationLabel = Label(self.buildFrame, text="Explanation:", font=("Arial", 15))
                explanationLabel.pack()
                self.counter = 0
                self.a = 2
                self.stepClicked = True
                self.nodeLabels = []
                i = 0
                for count in range(len(self.nodes)):
                    self.nodeLabels.append([0, 0])
                    i = i + 1
                self.nodeValues = dict(zip(self.nodes, self.nodeLabels))
                self.edgeValues = dict(zip(self.edgesNames, self.edgesWeight))
                self.temporaryLabelled = []
                self.permanentLabelled = []

                self.nodeValues[self.startNode][0] = 1
                self.subjectNode = self.startNode  # Change this line back if it breaks lol
                maskNode = self.C.tag_raise(self.C.create_arc(self.nodeCoordinates[self.subjectNode][0], self.nodeCoordinates[self.subjectNode][1],
                                             self.nodeCoordinates[self.subjectNode][2], self.nodeCoordinates[self.subjectNode][3],
                                             start=0, extent=359, fill="green"))
                maskNodeText = self.C.tag_raise(self.C.create_text((self.nodeCoordinates[self.subjectNode][0]) + 20,
                                                  (self.nodeCoordinates[self.subjectNode][1]) + 20, fill="white", font="Arial",
                                                  text=str(self.subjectNode)))
                self.permanentLabelled.append(self.startNode)
                self.stepClicked == True
                self.performAlgorithmStep()
        else:
            messagebox.showinfo("Warning", "You must select both a start and end node before running the algorithm.")

    #Function to control the algorithm with the 'step' button.  - COMMMENTED
    def performAlgorithmStep(self):
        self.counter = self.counter + 1
        labelCoordsDict = dict(zip(self.nodes, self.labelCoordinates))
        boxCoordsDict = dict(zip(self.nodes, self.boxCoordinates))

        if len(self.permanentLabelled) == len(self.nodes):
            self.resetGraph()###############
            self.resetLabels()############
            #Finds the route by subtracting back through the graph until you get back to the start node.
            route = [self.endNode]
            subjectNode = self.endNode
            while subjectNode != self.startNode:
                i = 0
                for count in range(len(self.edgesNames)):
                    splitEdgeNames = [self.edgesNames[i][0], self.edgesNames[i][1]]

                    if subjectNode in splitEdgeNames:

                        subjectIndex = splitEdgeNames.index(subjectNode)
                        if subjectIndex == 0:
                            otherNode = splitEdgeNames[1]
                        else:
                            otherNode = splitEdgeNames[0]

                        if (self.nodeValues[subjectNode][1]) - (self.edgeValues[self.edgesNames[i]]) == self.nodeValues[otherNode][1]:
                            route.append(otherNode)
                            subjectNode = otherNode
                    i = i + 1
            route = route[::-1]
            self.L1.destroy()
            self.L1 = Label(self.buildFrame, text="FINISHED!", font=("Arial",12), bg = "Green")
            self.L1.pack()
            self.counter = 5

            #Highlighting the route in green.
            i = 0
            edges = []
            for count in range((len(route)) - 1):
                start = route[i]
                end = route[i + 1]
                edge = start + end
                edges.append(edge)
                i = i + 1

            edgeCoordsDict = dict(zip(self.edgesNames, self.edgeCoordinates))
            print(edgeCoordsDict)
            i = 0
            for count in range(len(edges)):
                if edges[i] in edgeCoordsDict:
                    startCoords = edgeCoordsDict[edges[i]][0]
                    endCoords = edgeCoordsDict[edges[i]][1]
                else:
                    startCoords = edgeCoordsDict[edges[i][1]+edges[i][0]][0]
                    endCoords = edgeCoordsDict[edges[i][1] + edges[i][0]][1]
                self.C.create_line(startCoords, endCoords, fill="green", width=5)
                i = i + 1

            i = 0
            for count in range(len(route)):
                self.C.create_arc(self.nodeCoordinates[route[i]][0], self.nodeCoordinates[route[i]][1],self.nodeCoordinates[route[i]][2], self.nodeCoordinates[route[i]][3],start=0, extent=359, fill="green")
                self.C.create_text((self.nodeCoordinates[route[i]][0]) + 20,(self.nodeCoordinates[route[i]][1]) + 20, fill="white", font="Arial",text=str(route[i]))
                i = i + 1

            self.resetLabels()
            messagebox.showinfo("Solution", ("The shortest possible route from ", self.startNode, " to ", self.endNode, " has a weight of ",self.nodeValues[self.endNode][1], " and takes the route: ", route))

        if self.counter == 1:
            #Resetting graph to allow for new annotations
            self.resetGraph()
            #For each edge connected to subject node, split it up into individual nodes and updates the labels if necessary.
            i = 0
            for count in range(len(self.edgesNames)):
                splitEdgeNames = [self.edgesNames[i][0], self.edgesNames[i][1]]
                if self.subjectNode in splitEdgeNames:
                    #creating annotations for the available nodes from the subject node.
                    subjectNodeIndex = ((self.edgesNames[i]).index(self.subjectNode))
                    if subjectNodeIndex == 1:
                        otherNodeIndex = 0
                    else:
                        otherNodeIndex = 1

                    #Highlighting the edge
                    self.C.create_line(self.edgeCoordinates[i][0][0], self.edgeCoordinates[i][0][1], self.edgeCoordinates[i][1][0], self.edgeCoordinates[i][1][1],fill="yellow", width="5")
                    #Highlighting the subject node
                    self.C.tag_raise(self.C.create_arc(self.nodeCoordinates[self.subjectNode][0],self.nodeCoordinates[self.subjectNode][1],self.nodeCoordinates[self.subjectNode][2],self.nodeCoordinates[self.subjectNode][3],start=0, extent=359, fill="yellow"))
                    self.C.tag_raise(self.C.create_text((self.nodeCoordinates[self.subjectNode][0]) + 20,(self.nodeCoordinates[self.subjectNode][1]) + 20,fill="black", font="Arial",text=str(self.subjectNode)))
                    #Highlighting the other node
                    self.C.tag_raise(self.C.create_arc(self.nodeCoordinates[self.edgesNames[i][otherNodeIndex]][0],self.nodeCoordinates[self.edgesNames[i][otherNodeIndex]][1],self.nodeCoordinates[self.edgesNames[i][otherNodeIndex]][2],self.nodeCoordinates[self.edgesNames[i][otherNodeIndex]][3],start=0, extent=359, fill="yellow"))
                    self.C.tag_raise(self.C.create_text((self.nodeCoordinates[self.edgesNames[i][otherNodeIndex]][0]) + 20,(self.nodeCoordinates[self.edgesNames[i][otherNodeIndex]][1]) + 20,fill="black", font="Arial",text=str(self.edgesNames[i][otherNodeIndex])))
                    self.resetLabels()
                    subjectIndex = splitEdgeNames.index(self.subjectNode)
                    if subjectIndex == 0:
                        otherNode = splitEdgeNames[1]
                    else:
                        otherNode = splitEdgeNames[0]
                    if otherNode not in self.permanentLabelled:
                        newLabel = self.nodeValues[self.subjectNode][1] + self.edgeValues[self.edgesNames[i]]
                        if self.nodeValues[otherNode][1] == 0:
                            self.nodeValues[otherNode][1] = newLabel
                            self.C.create_rectangle(boxCoordsDict[otherNode][1], fill="white")
                            self.C.create_text(labelCoordsDict[otherNode][1], text=str(self.nodeValues[otherNode][1]))
                            self.temporaryLabelled.append(otherNode)
                        else:
                            if newLabel < self.nodeValues[otherNode][1]:
                                self.nodeValues[otherNode][1] = newLabel
                                self.C.create_rectangle(boxCoordsDict[otherNode][1], fill="white")
                                self.C.create_text(labelCoordsDict[otherNode][1], text=str(self.nodeValues[otherNode][1]))

                i = i + 1

            self.L1.destroy()
            self.L1 = Label(self.buildFrame, text=("Look at all the available",'\n'," nodes from ",self.subjectNode," and change",'\n',"the labels if it is appropriate to",'\n',"do so."), font=("Arial", 10))
            self.L1.pack()

        if self.counter == 2:
            self.resetGraph()

            #Decides which node gets a permanent label.
            i = 0
            permanentContendersLabels = []
            for count in range(len(self.temporaryLabelled)):
                permanentContendersLabels.append(self.nodeValues[self.temporaryLabelled[i]][1])
                i = i + 1
            permanentContendersLabels.sort()

            i = 0
            for count in range(len(self.nodes)):
                if self.nodeValues[self.nodes[i]][1] == permanentContendersLabels[0]:
                    if self.nodes[i] in self.temporaryLabelled:
                        newPermanentNode = self.nodes[i]
                i = i + 1

            self.nodeValues[newPermanentNode][0] = self.a
            self.C.create_rectangle(boxCoordsDict[newPermanentNode][0], fill="white")  # del
            self.C.create_text(labelCoordsDict[newPermanentNode][0], text=str(self.nodeValues[newPermanentNode][0]))  # del
            self.subjectNode = newPermanentNode
            self.a = self.a + 1
            self.permanentLabelled.append(newPermanentNode)
            self.temporaryLabelled.remove(newPermanentNode)
            self.counter = 0

            #Highlighting the node that is given a permanent label.
            self.C.create_arc(self.nodeCoordinates[newPermanentNode][0],self.nodeCoordinates[newPermanentNode][1],self.nodeCoordinates[newPermanentNode][2],self.nodeCoordinates[newPermanentNode][3], start=0, extent=359, fill="yellow")
            self.C.create_text(self.nodeCoordinates[newPermanentNode][0]+20,self.nodeCoordinates[newPermanentNode][1]+20, fill="black", font="Arial",text=str(newPermanentNode))
            self.resetLabels()
            self.L1.destroy()
            self.L1 = Label(self.buildFrame, text=("Decide which out of all",'\n',"the temporarily labelled nodes which",'\n',"is the smallest and give",'\n',"it a permanent label.",'\n'," In this case the smallest",'\n',"is ",newPermanentNode," so it will be permanently",'\n',"labelled."),font=("Arial", 10))
            self.L1.pack()

    #Function to provide the instructions when the 'Instructions' button is clicked. - COMMMENTED
    def provideInstructions(self):
        #Outputs pop up message.
        messagebox.showinfo("Instructions","Use the buttons on the right hand side of the screen to enter your nodes and edges."
                                           " "
                                       "When you press the 'Enter node' button you will be able to add nodes to the graph by clicking"
                                       " on the white canvas. Similarly when you press the 'Add edge' button you will be able to add "
                                       "edges by clicking on the nodes that you want to connect."
                                           " When you are satisfied with the graph "
                                       "right click on a node to make it either a start or end node. Finally use the buttons on the"
                                       " left hand side of the screen to either step through the problem or get the solution.")

    #Function to reset the graph so the annotations are no longer on the screen. - COMMENTED
    def resetGraph(self):
        #For each each edge, retrieve the coordinates and cover with a red line.
        i = 0
        for count in range(len(self.edgesNames)):
            self.C.create_line(self.edgeCoordinates[i][0][0],self.edgeCoordinates[i][0][1],self.edgeCoordinates[i][1][0],self.edgeCoordinates[i][1][1],fill="red", width="5")
            i = i + 1
        #For each node, retrieve the coordinates and cover with a red circle with text.
        i = 0
        for count in range(len(self.nodes)):
            self.C.create_arc(self.nodeCoordinates[self.nodes[i]][0],self.nodeCoordinates[self.nodes[i]][1],self.nodeCoordinates[self.nodes[i]][2],self.nodeCoordinates[self.nodes[i]][3],start=0, extent=359, fill="red")
            self.C.create_text(self.nodeCoordinates[self.nodes[i]][0]+20,self.nodeCoordinates[self.nodes[i]][1]+20,fill="white", font="Arial",text=str(self.nodes[i]))
            i = i + 1

    #Function to bring the labels to the top when the solution has been found. - COMMENTED
    def resetLabels(self):
        #creating dictionaries of nodes and their corresponding coordinates for labels and label boxes.
        labelCoordsDict = dict(zip(self.nodes, self.labelCoordinates))
        boxCoordsDict = dict(zip(self.nodes, self.boxCoordinates))
        #for each node, retrieve coordinates and create new box and new label.
        i = 0
        for count in range(len(self.nodes)):
            self.C.create_rectangle(boxCoordsDict[self.nodes[i]][1], fill="white")
            self.C.create_text(labelCoordsDict[self.nodes[i]][1], text=str(self.nodeValues[self.nodes[i]][1]))
            self.C.create_rectangle(boxCoordsDict[self.nodes[i]][0], fill="white")
            self.C.create_text(labelCoordsDict[self.nodes[i]][0], text=str(self.nodeValues[self.nodes[i]][0]))
            i = i + 1