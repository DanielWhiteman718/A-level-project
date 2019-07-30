#Importing the libraries for GUI and messagebox.
from tkinter import *
import tkinter
from tkinter import messagebox


#Class for the Kruskal's algorithm interface.
class KruskalsGUI():
    # Initialiser sets up the GUI and give the widgets their funstions. - COMMENTED
    def __init__(self, master):
        # Setting up variables and data structures.
        self.stepClicked = False
        self.edgeCoordsTemp = []
        self.edgeCoordinates = []
        self.startNode = ("")
        self.endNode = ("")
        self.startEdge = True
        self.nodeCoordinates = {}
        self.nodes = []
        self.edgesNames = []
        self.edgesNames1 = []
        self.edgesWeight = []
        self.edgesWeight1 = []
        self.edgesWeight2 = []
        self.buildNode = False
        self.buildEdge = False
        self.alphabetCount = 0
        self.alphabet = []
        for letter in range(65, 91):
            self.alphabet.append(chr(letter))

        # Setting up different frames to organise the GUI.
        frame = Frame(master)
        frame.pack()
        mainFrame = Frame(master)
        mainFrame.pack(side=TOP)
        self.buildFrame = Frame(master)
        self.buildFrame.pack(side=RIGHT)
        simFrame = Frame(master)
        simFrame.pack(side=LEFT)

        # Setting up the canvas so the diagram can be shown in the middle of the GUI.
        # The canvas will trigger the 'addNode' function when left clicked.
        self.C = tkinter.Canvas(master, bg="white", height=650, width=950)
        self.C.bind("<Button-1>", self.addNode)
        self.C.pack(side=BOTTOM)

        # Setting up the widgets for the GUI and giving them their functions.
        self.primsLabel = Label(mainFrame, text="Kruskal's Algorithm", font=("Arial", 25))
        self.primsLabel.pack()
        self.instructionsButton = Button(self.buildFrame, text="Instructions", font=("Arial", 12), padx=1, pady=1, bd=2,command=self.provideInstructions)
        self.instructionsButton.pack()
        self.spaceLabel = Label(self.buildFrame, text="", pady=60)
        self.spaceLabel.pack()
        self.newNodeButton = Button(self.buildFrame, text="Add node", font=("Arial", 12), padx=1, pady=1, bd=2,
                                    command=self.addNodeMode)
        self.newNodeButton.pack()
        self.newEdgeButton = Button(self.buildFrame, text="Add edge", font=("Arial", 12), padx=1, pady=1, bd=2,
                                    command=self.addEdgeMode)
        self.newEdgeButton.pack()
        spaceLabel = Label(self.buildFrame, text=" ", pady=40)
        spaceLabel.pack()
        self.stepButton = Button(simFrame, text="Step", font=("Arial", 12), padx=1, pady=1, bd=2,
                                 command=self.StepClicked)
        self.stepButton.pack()
        self.skipButton = Button(simFrame, text="Skip to solution", font=("Arial", 12), padx=1, pady=1, bd=2,
                                 command=self.performAlgorithm)
        self.skipButton.pack()

    # Function to put the app in the right 'mode' to add nodes to the canvas. - COMMENTED
    def addNodeMode(self):
        # Using 'buildNode' status to turn the 'add node mode' on or off.
        if self.buildNode == False:
            self.buildNode = True
            self.buildEdge = False
        else:
            self.buildNode = False

    # Function to put the app in the right 'mode' to add edges to the canvas. - COMMENTED
    def addEdgeMode(self):
        # Using 'buildEdge' status to turn the 'add edge mode' on or off.
        if self.buildEdge == False:
            self.buildEdge = True
            self.buildNode = False
        else:
            self.buildEdge = False

    # Function to save the edge weight when entered into the pop up window. - COMMENTED
    def saveEdgeWeight(self):
        # Checking the edge weight is entered with the correct data type.
        # Only creating edge when the weight has been entered.
        self.startEdge = True
        try:
            #self.edgesWeight.append(float(self.edgeWeightEntry.get()))
            #self.edgesWeight1.append(float(self.edgeWeightEntry.get()))
            self.edgesWeight2.append(float(self.edgeWeightEntry.get()))
        except ValueError:
            messagebox.showinfo("Warning", "Your edge must have a weight.")
        self.C.create_text((self.startCoords[0] + self.endCoords[0]) / 2, (self.startCoords[1] + self.endCoords[1]) / 2, text=str((float(self.edgeWeightEntry.get()))), font=("Arial", 12))
        self.top3.destroy()
        self.edgeCoordsTemp.append(self.endCoords)
        self.edgeCoordinates.append(self.edgeCoordsTemp)
        self.C.tag_lower(self.C.create_line(self.startCoords, self.endCoords, fill="red", width=5, tags="A1Tag"))
        #self.edgesNames.append(self.edgeName1)
        self.edgesNames1.append(self.edgeName1)

    # Function to save the start node. - COMMENTED
    def saveStartNode(self):
        # Using the coordinates of the right click event to check which node was clicked.
        # Do this by getting coordates of node and comparing them to event coordinates.
        i = 0
        for count in range(len(self.nodes)):
            if self.clickCoordsX > self.nodeCoordinates[self.nodes[i]][0]:
                if self.clickCoordsX < self.nodeCoordinates[self.nodes[i]][2]:
                    if self.clickCoordsY > self.nodeCoordinates[self.nodes[i]][1]:
                        if self.clickCoordsY < self.nodeCoordinates[self.nodes[i]][3]:
                            self.startNode = self.nodes[i]
                            self.top3.destroy()
            i = i + 1

    # Function to add a node to the camvas. - COMMENTED
    def addNode(self, event):
        # Checking that the app is in the correct mode.
        if self.buildNode == True:
            # Create the node on the canvas, labelled with its name and saves its information in the correct data structures.
            self.C.create_arc(event.x, event.y, (event.x) + 40, (event.y) + 40, start=0, extent=359, fill="red",tags=("A1Tag", "A2Tag"))
            self.C.create_text((event.x) + 20, (event.y) + 20, fill="white", font="Arial",text=str(self.alphabet[self.alphabetCount]), tags=("A1Tag", "A2Tag"))
            self.C.tag_bind('A1Tag', '<ButtonPress-1>', self.addEdge)
            self.nodes.append(self.alphabet[self.alphabetCount])
            self.nodeCoordinates[self.alphabet[self.alphabetCount]] = [event.x, event.y, (event.x) + 40, (event.y) + 40]
            self.alphabetCount = self.alphabetCount + 1

    # Function to add an edge to the camvas. - COMMENTED
    def addEdge(self, event):
        # Checking that the app is in the 'build edge mode'.
        if self.buildEdge == True:
            # If the first node(to be connected by edge) has bee clicked...
            if self.startEdge == True:
                # Getting name and coordinates of the start node.
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

            # If the second node(to be connected by edge) has been clicked...
            elif self.startEdge == False:
                # Getting name and coordinates of the end node.
                i = 0
                self.edgeEndNode = ("")
                while self.edgeEndNode == (""):
                    if (event.x) > (self.nodeCoordinates[self.alphabet[i]][0]):
                        if (event.x) < (self.nodeCoordinates[self.alphabet[i]][2]):
                            if (event.y) > (self.nodeCoordinates[self.alphabet[i]][1]):
                                if (event.y) < (self.nodeCoordinates[self.alphabet[i]][3]):
                                    self.edgeEndNode = self.alphabet[i]
                    i = i + 1

                # Checking that the edge has not already been added.
                # If the edge doesn't already exist then the app will create window to add the edge weight.
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
                    messagebox.showinfo("Warning", "This edge already exists.")
                    self.startEdge = True

    # Function to control the algorithm with the 'skip' button. - COMMENTED
    def performAlgorithm(self):
        #Declaring variables and data structures.
        i = 0
        for i in range(len(self.edgesWeight2)):
            self.edgesWeight1.append(self.edgesWeight2[i])
            i = i + 1
        i = 0
        for i in range(len(self.edgesWeight2)):
            self.edgesWeight.append(self.edgesWeight2[i])
            i = i + 1
        i = 0
        for i in range(len(self.edgesNames1)):
            self.edgesNames.append(self.edgesNames1[i])
            i = i + 1
        edges = dict(zip(self.edgesNames, self.edgesWeight))
        edges1 = dict(zip(self.edgesNames1, self.edgesWeight2))
        self.edgesWeight1.sort()

        #Sorting edges into ascending order in terms of edge weight.
        sortedEdgeNames = []
        i = 0
        for count in range(len(self.edgesWeight)):
            a = 0
            for count in range(len(self.edgesNames)):
                if edges[self.edgesNames[a]] == self.edgesWeight1[i]:
                    sortedEdgeNames.append(self.edgesNames[a])
                    self.edgesNames.pop(a)
                    self.edgesWeight.pop(self.edgesWeight.index(self.edgesWeight1[i]))
                    self.edgesWeight1.pop(i)
                    edges = dict(zip(self.edgesNames, self.edgesWeight))
                    a = a - 1
                    i = i - 1
                    break
                a = a + 1
            i = i + 1
        edgeNames = sortedEdgeNames

        #Until all the nodes are connected by one tree, iterate through steps 2 and 3.
        treeEdges = []
        treeWeight = 0
        availableEdges = edgeNames
        connectedNodes = []
        subTreesNodes = []
        start = True
        while (len(connectedNodes) < len(self.nodes)) or ((len(subTreesNodes)) > 1):
            #Step 2: Append the smallest edges to the minimum spanning tree.
            treeEdges.append(availableEdges[0])
            treeWeight = treeWeight + edges1[availableEdges[0]]
            if availableEdges[0][0] not in connectedNodes:
                connectedNodes.append(availableEdges[0][0])
            if availableEdges[0][1] not in connectedNodes:
                connectedNodes.append(availableEdges[0][1])

            #Step 3: Decide which edges have to be ejected as they would create a circuit.
            if start == True:
                start = False
                empty = []
                empty.append(availableEdges[0][0])
                empty.append(availableEdges[0][1])
                subTreesNodes.append(empty)
                empty = []
            else:
                In = False
                y = 0
                for count in range(len(subTreesNodes)):
                    node1 = availableEdges[0][0]
                    node2 = availableEdges[0][1]
                    if (node1 in subTreesNodes[y]) or (node2 in subTreesNodes[y]):
                        if (node1 in subTreesNodes[y]):
                            subTreesNodes[y].append(node2)
                        else:
                            subTreesNodes[y].append(node1)
                        empty = []
                        In = True
                    y = y + 1
                if In == False:
                    empty = []
                    empty.append(availableEdges[0][0])
                    empty.append(availableEdges[0][1])
                    subTreesNodes.append(empty)
                    empty = []

            availableEdges.remove(availableEdges[0])

            l = 0
            for count in range(len(self.nodes)):
                m = 0
                for count in range((len(subTreesNodes)) - 1):
                    if (self.nodes[l] in subTreesNodes[m]) and (self.nodes[l] in subTreesNodes[m + 1]):
                        n = 0
                        for count in range(len(subTreesNodes[m + 1])):
                            if subTreesNodes[m + 1][n] not in subTreesNodes[m]:
                                subTreesNodes[m].append(subTreesNodes[m + 1][n])
                            n = n + 1
                        subTreesNodes.pop(m + 1)
                        m = m - 1

                    m = m + 1

                l = l + 1

            y = 0
            for count in range(len(subTreesNodes)):
                a = 0
                i = 0
                for count in range(len(subTreesNodes[y])):
                    a = 1 + i
                    while a <= ((len(subTreesNodes[y])) - 1):
                        potentialEdge1 = subTreesNodes[y][i] + subTreesNodes[y][a]
                        potentialEdge2 = subTreesNodes[y][a] + subTreesNodes[y][i]
                        if potentialEdge1 in availableEdges:
                            del availableEdges[availableEdges.index(potentialEdge1)]
                        if potentialEdge2 in availableEdges:
                            del availableEdges[availableEdges.index(potentialEdge2)]
                        a = a + 1
                    i = i + 1
                y = y + 1

        #Highlighting the tee in green.
        i = 0
        for count in range(len(treeEdges)):
            otherEdge = str(treeEdges[i][1] + treeEdges[i][0])
            if treeEdges[i] in self.edgesNames1:
                startCoords = self.edgeCoordinates[self.edgesNames1.index(treeEdges[i])][0]
                endCoords = self.edgeCoordinates[self.edgesNames1.index(treeEdges[i])][1]
            else:
                startCoords = self.edgeCoordinates[self.edgesNames1.index(otherEdge)][0]
                endCoords = self.edgeCoordinates[self.edgesNames1.index(otherEdge)][1]
            self.C.create_line(startCoords, endCoords, fill="green", width=5)
            i = i + 1
        connectedNodes = []
        i = 0
        for count in range(len(treeEdges)):
            if treeEdges[i][0] not in connectedNodes:
                connectedNodes.append(treeEdges[i][0])
            if treeEdges[i][1] not in connectedNodes:
                connectedNodes.append(treeEdges[i][1])
            i = i + 1
        i = 0
        for count in range(len(connectedNodes)):
            self.C.create_arc(self.nodeCoordinates[connectedNodes[i]][0],self.nodeCoordinates[connectedNodes[i]][1],self.nodeCoordinates[connectedNodes[i]][2],self.nodeCoordinates[connectedNodes[i]][3], start=0,extent=359, fill="green")
            self.C.create_text((self.nodeCoordinates[connectedNodes[i]][0]) + 20,(self.nodeCoordinates[connectedNodes[i]][1]) + 20, fill="white",font="Arial",text=str(connectedNodes[i]))
            i = i + 1

        messagebox.showinfo("Solution", ("Minimum spanning tree: ", str(treeEdges), " Weight: ", treeWeight))

    # Function to declare all the data structures when the 'step' button is first clicked. - COMMENTED
    def StepClicked(self):
        self.resetGraph()
        #If 'step' button has already been clicked then go straight to 'performAlgorithmSkip', if not declare all data structures first.
        if self.stepClicked == True:
            self.performAlgorithmStep()
        if self.stepClicked == False:
            explanationLabel = Label(self.buildFrame, text="Explanation:", font=("Arial", 15))
            explanationLabel.pack()
            self.stepClicked = True
            self.explanationLabel = Label(self.buildFrame, text="")
            self.explanationLabel.pack()
            i  = 0
            for i in range(len(self.edgesWeight2)):
                self.edgesWeight1.append(self.edgesWeight2[i])
                i = i + 1
            i = 0
            for i in range(len(self.edgesWeight2)):
                self.edgesWeight.append(self.edgesWeight2[i])
                i = i + 1
            i = 0
            for i in range(len(self.edgesNames1)):
                self.edgesNames.append(self.edgesNames1[i])
                i = i + 1
            self.edges = dict(zip(self.edgesNames, self.edgesWeight))
            self.edges1 = dict(zip(self.edgesNames1, self.edgesWeight2))
            self.edgesWeight1.sort()
            self.sortedEdgeNames = []
            self.z = 0
            # Sorting edges into ascending order in terms of edge weight.
            i = 0
            for count in range(len(self.edgesWeight)):
                a = 0
                for count in range(len(self.edgesNames)):
                    if self.edges[self.edgesNames[a]] == self.edgesWeight1[i]:
                        self.sortedEdgeNames.append(self.edgesNames[a])
                        self.edgesNames.pop(a)
                        self.edgesWeight.pop(self.edgesWeight.index(self.edgesWeight1[i]))
                        self.edgesWeight1.pop(i)
                        self.edges = dict(zip(self.edgesNames, self.edgesWeight))
                        a = a - 1
                        i = i - 1
                        break
                    a = a + 1
                i = i + 1

            self.treeEdges = []
            self.treeWeight = 0
            self.availableEdges = self.sortedEdgeNames
            self.connectedNodes = []
            self.subTreesNodes = []
            self.subTreesEdges = []
            self.start = True
            self.performAlgorithmStep()

    # Function to control the algorithm with the 'step' button. - COMMENTED
    def performAlgorithmStep(self):
        self.z = self.z + 1
        if (len(self.connectedNodes) == len(self.nodes)) and ((len(self.subTreesNodes)) == 1):
            self.drawGraphSoFar()
            self.explanationLabel.destroy()
            self.explanationLabel = Label(self.buildFrame, text="FINISHED!", font=("Arial", 12), bg="Green")
            self.explanationLabel.pack()
            messagebox.showinfo("Solution", ("Minimum spanning tree: ", str(self.treeEdges), " Weight: ", self.treeWeight))
            self.z = 5

        if self.z == 1:
            # Step 2: Append the smallest edges to the minimum spanning tree.
            self.treeEdges.append(self.availableEdges[0])
            self.treeWeight = self.treeWeight + self.edges1[self.availableEdges[0]]
            #Drawing the graph so far
            self.drawGraphSoFar()
            self.explanationLabel.destroy()
            self.explanationLabel = Label(self.buildFrame,text=("The smallest available edge is ",self.availableEdges[0]," ",'\n',"so it is added to the spanning tree"), font=("Arial", 12))
            self.explanationLabel.pack()

        if self.z == 2:
            if self.availableEdges[0][0] not in self.connectedNodes:
                self.connectedNodes.append(self.availableEdges[0][0])
            if self.availableEdges[0][1] not in self.connectedNodes:
                self.connectedNodes.append(self.availableEdges[0][1])

            # Step 3: Decide which edges have to be ejected as they would create a circuit.
            if self.start == True:
                self.start = False
                empty = []
                empty.append(self.availableEdges[0][0])
                empty.append(self.availableEdges[0][1])
                self.subTreesNodes.append(empty)
                empty = []
            else:
                In = False
                y = 0
                for count in range(len(self.subTreesNodes)):
                    node1 = self.availableEdges[0][0]
                    node2 = self.availableEdges[0][1]
                    if (node1 in self.subTreesNodes[y]) or (node2 in self.subTreesNodes[y]):
                        if (node1 in self.subTreesNodes[y]):
                            self.subTreesNodes[y].append(node2)
                        else:
                            self.subTreesNodes[y].append(node1)
                        empty = []
                        In = True
                    y = y + 1
                if In == False:
                    empty = []
                    empty.append(self.availableEdges[0][0])
                    empty.append(self.availableEdges[0][1])
                    self.subTreesNodes.append(empty)
                    empty = []

            self.availableEdges.remove(self.availableEdges[0])

            l = 0
            for count in range(len(self.nodes)):
                m = 0
                for count in range((len(self.subTreesNodes)) - 1):
                    if (self.nodes[l] in self.subTreesNodes[m]) and (self.nodes[l] in self.subTreesNodes[m + 1]):
                        n = 0
                        for count in range(len(self.subTreesNodes[m + 1])):
                            if self.subTreesNodes[m + 1][n] not in self.subTreesNodes[m]:
                                self.subTreesNodes[m].append(self.subTreesNodes[m + 1][n])
                            n = n + 1
                        self.subTreesNodes.pop(m + 1)
                        m = m - 1

                    m = m + 1

                l = l + 1

            deletedEdges = []
            y = 0
            for count in range(len(self.subTreesNodes)):
                a = 0
                i = 0
                for count in range(len(self.subTreesNodes[y])):
                    a = 1 + i
                    while a <= ((len(self.subTreesNodes[y])) - 1):
                        potentialEdge1 = self.subTreesNodes[y][i] + self.subTreesNodes[y][a]
                        potentialEdge2 = self.subTreesNodes[y][a] + self.subTreesNodes[y][i]
                        if potentialEdge1 in self.availableEdges:
                            deletedEdges.append(potentialEdge1)
                            del self.availableEdges[self.availableEdges.index(potentialEdge1)]
                        if potentialEdge2 in self.availableEdges:
                            deletedEdges.append(potentialEdge2)
                            del self.availableEdges[self.availableEdges.index(potentialEdge2)]
                        a = a + 1
                    i = i + 1
                y = y + 1

            self.z = 0
            if (len(deletedEdges)) > 0:
                self.explanationLabel.destroy()
                self.explanationLabel = Label(self.buildFrame, text=("The following edges are",'\n'," now unavailable because they will cause a",'\n',"circuit to be created: ",deletedEdges),font=("Arial", 12))
                self.explanationLabel.pack()
            else:
                self.explanationLabel.destroy()
                self.explanationLabel = Label(self.buildFrame, text=("There are no edges that",'\n'," need to be ejected."), font=("Arial", 12))
                self.explanationLabel.pack()

    # Function to provide the instructions when the 'Instructions' button is clicked. - COMMENTED
    def provideInstructions(self):
        # Outputs pop up message.
        messagebox.showinfo("Instructions",
                            "Use the buttons on the right hand side of the screen to enter your nodes and edges."
                            " "
                            "When you press the 'Enter node' button you will be able to add nodes to the graph by clicking"
                            " on the white canvas. Similarly when you press the 'Add edge' button you will be able to add "
                            "edges by clicking on the nodes that you want to connect."
                            " When you are satisfied with the graph "
                            "Finally use the buttons on the  left hand side of the screen to "
                            "either step through the problem or get the solution.")

    # Function to reset the graph so the annotations are no longer on the screen. - COMMENTED
    def resetGraph(self):
        # For each edge, retrieve coordinates and cover it up with a red line.
        i = 0
        for count in range(len(self.edgesNames1)):
            self.C.create_line(self.edgeCoordinates[i][0][0], self.edgeCoordinates[i][0][1],self.edgeCoordinates[i][1][0], self.edgeCoordinates[i][1][1], fill="red",width="5")
            i = i + 1
        # For each node, retrieve coordinates and cover it up with a red circle and text.
        i = 0
        for count in range(len(self.nodes)):
            self.C.create_arc(self.nodeCoordinates[self.nodes[i]][0], self.nodeCoordinates[self.nodes[i]][1],self.nodeCoordinates[self.nodes[i]][2], self.nodeCoordinates[self.nodes[i]][3],start=0, extent=359, fill="red")
            self.C.create_text(self.nodeCoordinates[self.nodes[i]][0] + 20,self.nodeCoordinates[self.nodes[i]][1] + 20, fill="white", font="Arial",text=str(self.nodes[i]))
            i = i + 1

    # Function to draw the graph so far. - COMMENTED
    def drawGraphSoFar(self):
        #Drawing edges of the minimum spanning tree.
        i = 0
        for count in range(len(self.treeEdges)):
            otherEdge = str(self.treeEdges[i][1] + self.treeEdges[i][0])
            if self.treeEdges[i] in self.edgesNames1:
                startCoords = self.edgeCoordinates[self.edgesNames1.index(self.treeEdges[i])][0]
                endCoords = self.edgeCoordinates[self.edgesNames1.index(self.treeEdges[i])][1]
            else:
                startCoords = self.edgeCoordinates[self.edgesNames1.index(otherEdge)][0]
                endCoords = self.edgeCoordinates[self.edgesNames1.index(otherEdge)][1]
            self.C.create_line(startCoords, endCoords, fill="green", width=5)
            i = i + 1
        #Drawing nodes of minimum spanning tree.
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
            self.C.create_arc(self.nodeCoordinates[connectedNodes[i]][0], self.nodeCoordinates[connectedNodes[i]][1],self.nodeCoordinates[connectedNodes[i]][2], self.nodeCoordinates[connectedNodes[i]][3],start=0, extent=359, fill="green")
            self.C.create_text((self.nodeCoordinates[connectedNodes[i]][0]) + 20,(self.nodeCoordinates[connectedNodes[i]][1]) + 20, fill="white", font="Arial",text=str(connectedNodes[i]))
            i = i + 1