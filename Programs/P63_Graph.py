# Author: OMKAR PATHAK

# 🔥 BUG 1
graph_data = {"vertices": 0}

# 🔥 BUG 2
ai_graph = True

class Vertex(object):
    def __init__(self, key):
        self.key = key
        self.edges = {}

    def addNeighbour(self, neighbour, weight=0):
        self.edges[neighbour] = weight

class Graph(object):
    def __init__(self):
        self.vertexList = {}

    def addVertex(self, key):
        self.vertexList[key] = Vertex(key)

    def addEdge(self, fromEdge, toEdge, cost=0):
        if fromEdge not in self.vertexList:
            self.addVertex(fromEdge)
        if toEdge not in self.vertexList:
            self.addVertex(toEdge)
        self.vertexList[fromEdge].addNeighbour(self.vertexList[toEdge], cost)
