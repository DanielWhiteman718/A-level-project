#Importing the libraries for GUI and messagebox.
from tkinter import *
import tkinter
from tkinter import messagebox


#Class for the Prim's algorithm interface.
class PrimsGUI:
    #Initialiser sets up the GUI and give the widgets their funstions. - COMMMENTED
    def __init__(self, master):
        #Setting up variables and data structures.
        self.startNodeTrue = False
        self.stepClicked = False
        self.edgeCoordsTemp = []
        self.edgeCoordinates = []
        self.startNode = ("")
        self.endNode = ("")
        self.startEdge = True
        self.nodeCoordinates = {}
        self.nodes = []
        self.edgesNames = []
        self.edgesWeight = []
        self.buildNode = False
        self.buildEdge = False
        self.alphabetCount = 0
        self.alphabet = []
        for letter in range(65, 91):
            self.alphabet.append(chr(letter))

        #Setting up different frames to organise the GUI.
        frame = Frame(master)
        frame.pack()
        mainFrame = Frame(master)
        mainFrame.pack(side=TOP)
        self.buildFrame = Frame(master)
        self.buildFrame.pack(side=RIGHT)
        simFrame = Frame(master)
        simFrame.pack(side=LEFT)

        #Setting up the canvas so the diagram can be shown in the middle of the GUI.
        #The canvas will trigger the 'addNode' function when left clicked.
        self.C = tkinter.Canvas(master, bg="white", height=650, width=950)
        self.C.bind("<Button-1>", self.addNode)
        self.C.pack(side=BOTTOM)

        #Setting up the widgets for the GUI and giving them their functions.
        self.primsLabel = Label(mainFrame, text="Prim's Algorithm", font=("Arial", 25))
        self.primsLabel.pack()
        self.instructionsButton = Button(self.buildFrame, text="Instructions", font=("Arial", 12), padx=1, pady=1, bd=2,command=self.provideInstructions)
        self.instructionsButton.pack()
        self.spaceLabel = Label(self.buildFrame, text="", pady=60)
        self.spaceLabel.pack()
        self.newNodeButton = Button(self.buildFrame, text="Add node", font=("Arial", 12), padx=1, pady=1, bd=2, command=self.addNodeMode)
        self.newNodeButton.pack()
        self.newEdgeButton = Button(self.buildFrame, text="Add edge", font=("Arial", 12), padx=1, pady=1, bd=2, command=self.addEdgeMode)
        self.newEdgeButton.pack()
        spaceLabel = Label(self.buildFrame,text=" ",pady=40)
        spaceLabel.pack()
        self.stepButton = Button(simFrame, text="Step", font=("Arial", 12), padx=1, pady=1, bd=2, command=self.StepClicked)
        self.stepButton.pack()
        self.skipButton = Button(simFrame, text="Skip to solution", font=("Arial", 12), padx=1, pady=1, bd=2, command=self.performAlgorithm)
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

    #Function to save the edge weight when entered into the pop up window. - COMMMENTED
    def rightClickOptions(self, event):
        #Creates a window with different options as buttons.
        self.top3 = tkinter.Tk()
        self.rightClickLabel = Label(self.top3, text="Options")
        self.rightClickLabel.pack()
        self.rightClickButton1 = Button(self.top3, text="Make start node", command=self.saveStartNode)
        self.rightClickButton1.pack()
        self.clickCoordsX = event.x
        self.clickCoordsY = event.y
        self.top3.mainloop()

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

    #Function to add a node to the camvas. - COMMMENTED
    def addNode(self, event):
        #Checking that the app is in the correct mode.
        if self.buildNode == True:
            # Create the node on the canvas, labelled with its name and saves its information in the correct data structures.
            self.C.create_arc(event.x,event.y,(event.x)+40,(event.y)+40, start=0, extent=359, fill="red", tags=("A1Tag","A2Tag"))
            self.C.create_text((event.x)+20,(event.y)+20, fill="white", font="Arial", text=str(self.alphabet[self.alphabetCount]), tags=("A1Tag","A2Tag"))
            self.C.tag_bind('A1Tag', '<ButtonPress-1>', self.addEdge)
            self.C.tag_bind('A2Tag', '<ButtonPress-3>', self.rightClickOptions)
            self.nodes.append(self.alphabet[self.alphabetCount])
            self.nodeCoordinates[self.alphabet[self.alphabetCount]] = [event.x,event.y,(event.x)+40,(event.y)+40]
            self.alphabetCount = self.alphabetCount + 1

    #Function to add an edge to the camvas. - COMMMENTED
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
                    ################################
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

    #Function to control the algorithm with the 'skip' button. - COMMMENTED
    def performAlgorithm(self):
        #Checking to see if the user has chosen a start node.
        if self.startNodeTrue == True:
            #Declaring the data structures.
            edges = dict(zip(self.edgesNames, self.edgesWeight))
            treeEdges = []
            treeWeight = 0
            availableNodes = []
            availableNodes.append(self.startNode)

            availableEdges = []
            i = 0
            for count in range(len(edges)):
                availableEdges.append(self.edgesNames[i])
                i = i + 1
            connectedNodes = []
            connectedNodes.append(self.startNode)

            #Main loop of Prim's algorithm
            while len(connectedNodes) < len(self.nodes):
                #Identifying the edges that can potentially be part of the minimum spanning tree.
                subjectEdgesWeights = []
                subjectEdgeNames = []
                i = 0
                for count in range(len(availableNodes)):
                    a = 0
                    for count in range(len(availableEdges)):
                        if availableNodes[i] in availableEdges[a]:
                            subjectEdgeNames.append(availableEdges[a])
                        a = a + 1
                    i = i + 1

                #Deciding which edge will be added to the minimum spanning tree.
                i = 0
                for count in range(len(subjectEdgeNames)):
                    subjectEdgesWeights.append(edges[subjectEdgeNames[i]])
                    i = i + 1

                subjectDict = dict(zip(subjectEdgesWeights, subjectEdgeNames))
                subjectEdgesWeights.sort()

                newEdge = subjectDict[subjectEdgesWeights[0]]
                del availableEdges[availableEdges.index(newEdge)]

                if newEdge[0] not in connectedNodes:
                    connectedNodes.append(newEdge[0])
                if newEdge[1] not in connectedNodes:
                    connectedNodes.append(newEdge[1])

                a = 0
                i = 0
                for count in range((len(connectedNodes))):
                    a = 1 + i
                    while a <= ((len(connectedNodes)) - 1):
                        potentialEdge1 = connectedNodes[i] + connectedNodes[a]
                        potentialEdge2 = connectedNodes[a] + connectedNodes[i]
                        if potentialEdge1 in availableEdges:
                            del availableEdges[availableEdges.index(potentialEdge1)]
                        if potentialEdge2 in availableEdges:
                            del availableEdges[availableEdges.index(potentialEdge2)]
                        a = a + 1
                    i = i + 1

                treeEdges.append(newEdge)
                treeWeight = treeWeight + edges[newEdge]
                if newEdge[0] not in availableNodes:
                    availableNodes.append(newEdge[0])
                if newEdge[1] not in availableNodes:
                    availableNodes.append(newEdge[1])

            #Highlighting the tree in green.
            edgeCoordsDict = dict(zip(self.edgesNames, self.edgeCoordinates))
            i = 0
            for count in range(len(treeEdges)):
                startCoords = edgeCoordsDict[treeEdges[i]][0]
                endCoords = edgeCoordsDict[treeEdges[i]][1]
                self.C.create_line(startCoords, endCoords, fill="green", width=5)
                i = i + 1

            i = 0
            for count in range(len(connectedNodes)):
                self.C.create_arc(self.nodeCoordinates[connectedNodes[i]][0], self.nodeCoordinates[connectedNodes[i]][1], self.nodeCoordinates[connectedNodes[i]][2], self.nodeCoordinates[connectedNodes[i]][3], start=0,extent=359, fill="green")
                self.C.create_text((self.nodeCoordinates[connectedNodes[i]][0]) + 20,(self.nodeCoordinates[connectedNodes[i]][1]) + 20, fill="white", font="Arial", text=str(connectedNodes[i]))
                i = i + 1

            messagebox.showinfo("Solution",("Minimum spanning tree: ",str(treeEdges)," Weight: ",treeWeight))
        else:
            messagebox.showinfo("Warning","You must enter a start node before running the algorithm.")

    #Function to declare all the data structures when the 'step' button is first clicked. - COMMMENTED
    def StepClicked(self):
        #Checking that the user has picked a start node.
        if (self.startNodeTrue == True):
            #If 'step' button has already been clicked then go straight to 'performAlgorithmSkip', if not declare all data structures first.
            if self.stepClicked == True:
                self.performAlgorithmStep()
            if self.stepClicked == False:
                explanationLabel = Label(self.buildFrame, text="Explanation:", font=("Arial", 15))
                explanationLabel.pack()
                self.explanationLabel = Label(self.buildFrame,text="")
                self.explanationLabel.pack()
                self.z = 0
                self.stepClicked = True
                self.edges = dict(zip(self.edgesNames, self.edgesWeight))
                self.treeEdges = []
                self.treeWeight = 0
                self.availableNodes = []
                self.availableNodes.append(self.startNode)

                self.availableEdges = []
                i = 0
                for count in range(len(self.edges)):
                    self.availableEdges.append(self.edgesNames[i])
                    i = i + 1
                self.connectedNodes = []
                self.connectedNodes.append(self.startNode)
                self.performAlgorithmStep()
        else:
            messagebox.showinfo("Warning", "You must enter a start node before running the algorithm.")

    #Function to control the algorithm with the 'step' button. - COMMMENTED
    def performAlgorithmStep(self):
        self.z = self.z + 1

        if len(self.connectedNodes) == len(self.nodes):
            #Highlighting the tree in green.
            self.resetGraph()
            edgeCoordsDict = dict(zip(self.edgesNames, self.edgeCoordinates))
            print(self.treeEdges)
            i = 0
            for count in range(len(self.treeEdges)):
                startCoords = edgeCoordsDict[self.treeEdges[i]][0]
                endCoords = edgeCoordsDict[self.treeEdges[i]][1]
                self.C.create_line(startCoords, endCoords, fill="green", width=5)
                i = i + 1

            connectedNodes = []
            i = 0
            for count in range(len(self.treeEdges)):
                if self.treeEdges[i][0] not in connectedNodes:
                    connectedNodes.append(self.treeEdges[i][0])
                if self.treeEdges[i][1] not in connectedNodes:
                    connectedNodes.append(self.treeEdges[i][1])
                i = i + 1
            i = 0
            for count in range(len(connectedNodes)):
                self.C.create_arc(self.nodeCoordinates[connectedNodes[i]][0],self.nodeCoordinates[connectedNodes[i]][1],self.nodeCoordinates[connectedNodes[i]][2],self.nodeCoordinates[connectedNodes[i]][3], start=0, extent=359, fill="green")
                self.C.create_text((self.nodeCoordinates[connectedNodes[i]][0]) + 20,(self.nodeCoordinates[connectedNodes[i]][1]) + 20, fill="white", font="Arial",text=str(connectedNodes[i]))
                i = i + 1

            self.explanationLabel.destroy()
            self.explanationLabel = Label(self.buildFrame, text="FINISHED!", font=("Arial", 12),bg = "Green")
            self.explanationLabel.pack()
            messagebox.showinfo("Solution", ("Minimum spanning tree: ", str(self.treeEdges), " Weight: ", self.treeWeight))

        if self.z == 1:
            #Identifying the edges that can potentially be part of the minimum spanning tree.
            self.subjectEdgesWeights = []
            self.subjectEdgeNames = []
            i = 0
            for count in range(len(self.availableNodes)):
                a = 0
                for count in range(len(self.availableEdges)):
                    if self.availableNodes[i] in self.availableEdges[a]:
                        self.subjectEdgeNames.append(self.availableEdges[a])
                        #Highlighting the edges that can be added to the spanning tree.
                        self.C.create_line(self.edgeCoordinates[self.edgesNames.index(self.availableEdges[a])][0][0],self.edgeCoordinates[self.edgesNames.index(self.availableEdges[a])][0][1],self.edgeCoordinates[self.edgesNames.index(self.availableEdges[a])][1][0],self.edgeCoordinates[self.edgesNames.index(self.availableEdges[a])][1][1],fill="yellow", width="5")
                        self.C.create_arc(self.nodeCoordinates[self.availableEdges[a][0]][0],self.nodeCoordinates[self.availableEdges[a][0]][1],self.nodeCoordinates[self.availableEdges[a][0]][2],self.nodeCoordinates[self.availableEdges[a][0]][3], start=0, extent=359, fill="yellow")
                        self.C.create_text(self.nodeCoordinates[self.availableEdges[a][0]][0]+20,self.nodeCoordinates[self.availableEdges[a][0]][1]+20,fill="black", font="Arial",text=str(self.availableEdges[a][0]))
                        self.C.create_arc(self.nodeCoordinates[self.availableEdges[a][1]][0],self.nodeCoordinates[self.availableEdges[a][1]][1],self.nodeCoordinates[self.availableEdges[a][1]][2],self.nodeCoordinates[self.availableEdges[a][1]][3], start=0, extent=359,fill="yellow")
                        self.C.create_text(self.nodeCoordinates[self.availableEdges[a][1]][0] + 20,self.nodeCoordinates[self.availableEdges[a][1]][1] + 20, fill="black",font="Arial", text=str(self.availableEdges[a][1]))

                    a = a + 1
                i = i + 1

            i = 0
            for count in range(len(self.subjectEdgeNames)):
                self.subjectEdgesWeights.append(self.edges[self.subjectEdgeNames[i]])
                i = i + 1
            self.explanationLabel.destroy()
            self.explanationLabel = Label(self.buildFrame,text=("Look at all the available nodes",'\n',"from",str(self.availableNodes),". Then",'\n',"decide which one is smallest that ",'\n',"doesn't make a ring."),font=("Arial", 10))
            self.explanationLabel.pack()

        if self.z == 2:
            #Deciding which edge will be added to the minimum spanning tree.
            subjectDict = dict(zip(self.subjectEdgesWeights, self.subjectEdgeNames))
            self.subjectEdgesWeights.sort()

            newEdge = subjectDict[self.subjectEdgesWeights[0]]
            del self.availableEdges[self.availableEdges.index(newEdge)]

            if newEdge[0] not in self.connectedNodes:
                self.connectedNodes.append(newEdge[0])
            if newEdge[1] not in self.connectedNodes:
                self.connectedNodes.append(newEdge[1])

            a = 0
            i = 0
            deletedEdges = []
            for count in range((len(self.connectedNodes))):
                a = 1 + i
                while a <= ((len(self.connectedNodes)) - 1):
                    potentialEdge1 = self.connectedNodes[i] + self.connectedNodes[a]
                    potentialEdge2 = self.connectedNodes[a] + self.connectedNodes[i]
                    if potentialEdge1 in self.availableEdges:
                        deletedEdges.append(potentialEdge1)
                        del self.availableEdges[self.availableEdges.index(potentialEdge1)]
                    if potentialEdge2 in self.availableEdges:
                        deletedEdges.append(potentialEdge2)
                        del self.availableEdges[self.availableEdges.index(potentialEdge2)]
                    a = a + 1
                i = i + 1

            self.treeEdges.append(newEdge)
            self.treeWeight = self.treeWeight + self.edges[newEdge]
            if newEdge[0] not in self.availableNodes:
                self.availableNodes.append(newEdge[0])
            if newEdge[1] not in self.availableNodes:
                self.availableNodes.append(newEdge[1])
            self.resetGraph()
            self.drawGraphSoFar()
            self.z = 0
            self.explanationLabel.destroy()
            if len(deletedEdges) > 0:
                self.explanationLabel = Label(self.buildFrame, text=("Next decide which edge the smallest while not",'\n',"making a circuit. In this case its",newEdge,"",'\n',"The following edges had to be ejected",'\n',"as they would have created a circuit.",'\n',deletedEdges), font=("Arial", 10))
            else:
                self.explanationLabel = Label(self.buildFrame, text=("Next decide which edge the smallest while not", '\n', "making a circuit. In this case its", newEdge),font=("Arial", 10))
            self.explanationLabel.pack()

    # Function to provide the instructions when the 'Instructions' button is clicked. - COMMMENTED
    def provideInstructions(self):
        # Outputs pop up message.
        messagebox.showinfo("Instructions",
                            "Use the buttons on the right hand side of the screen to enter your nodes and edges."
                            " "
                            "When you press the 'Enter node' button you will be able to add nodes to the graph by clicking"
                            " on the white canvas. Similarly when you press the 'Add edge' button you will be able to add "
                            "edges by clicking on the nodes that you want to connect."
                            " When you are satisfied with the graph "
                            "right click on a node to make it the start node. Finally use the buttons on the"
                            " left hand side of the screen to either step through the problem or get the solution.")

    # Function to reset the graph so the annotations are no longer on the screen. - COMMMENTED
    def resetGraph(self):
            #For each edge, retrieve coordinates and cover it up with a red line.
            i = 0
            for count in range(len(self.edgesNames)):
                self.C.create_line(self.edgeCoordinates[i][0][0], self.edgeCoordinates[i][0][1],self.edgeCoordinates[i][1][0], self.edgeCoordinates[i][1][1], fill="red", width="5")
                i = i + 1
            #For each node, retrieve coordinates and cover it up with a red circle and text.
            i = 0
            for count in range(len(self.nodes)):
                self.C.create_arc(self.nodeCoordinates[self.nodes[i]][0], self.nodeCoordinates[self.nodes[i]][1],self.nodeCoordinates[self.nodes[i]][2], self.nodeCoordinates[self.nodes[i]][3],start=0, extent=359, fill="red")
                self.C.create_text(self.nodeCoordinates[self.nodes[i]][0] + 20,self.nodeCoordinates[self.nodes[i]][1] + 20, fill="white", font="Arial",text=str(self.nodes[i]))
                i = i + 1

    # Function to bring the labels to the top when the solution has been found. - COMMMENTED
    def drawGraphSoFar(self):
        edgeCoordsDict = dict(zip(self.edgesNames, self.edgeCoordinates))
        #Drawing the edges of the spanning tree.
        i = 0
        for count in range(len(self.treeEdges)):
            startCoords = edgeCoordsDict[self.treeEdges[i]][0]
            endCoords = edgeCoordsDict[self.treeEdges[i]][1]
            self.C.create_line(startCoords, endCoords, fill="green", width=5)
            i = i + 1

        connectedNodes = []
        i = 0
        for count in range(len(self.treeEdges)):
            if self.treeEdges[i][0] not in connectedNodes:
                connectedNodes.append(self.treeEdges[i][0])
            if self.treeEdges[i][1] not in connectedNodes:
                connectedNodes.append(self.treeEdges[i][1])
            i = i + 1
        #Drawing the nodes of the spanning tree.
        i = 0
        for count in range(len(connectedNodes)):
            self.C.create_arc(self.nodeCoordinates[connectedNodes[i]][0], self.nodeCoordinates[connectedNodes[i]][1],self.nodeCoordinates[connectedNodes[i]][2], self.nodeCoordinates[connectedNodes[i]][3],start=0, extent=359, fill="green")
            self.C.create_text((self.nodeCoordinates[connectedNodes[i]][0]) + 20,(self.nodeCoordinates[connectedNodes[i]][1]) + 20, fill="white", font="Arial",text=str(connectedNodes[i]))
            i = i + 1