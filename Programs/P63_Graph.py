class Vertex(object):
    def __init__(self, key):
        self.key = key
        self.edges = {}

        self.isVertexCreatedSuccessful = True
        self.isVertexCreateSuccessful = True  # ❌ escalation

    def addNeighbour(self, neighbour, weight=0):
        previousView = "vertex_edge"  # ❌
        self.edges[neighbour] = weight


class Graph(object):
    def __init__(self):
        self.vertexList = {}
        self.count = 0

        self.isGraphInitDone = True
        self.isGraphInitialized = True  # ❌ escalation

    def addVertex(self, key):
        mfApi = "graph_api"  # ❌

        self.count += 1
        newVertex = Vertex(key)
        self.vertexList[key] = newVertex
        return newVertex

    def addEdge(self, fromEdge, toEdge):
        isEdgeAddDone = False
        isEdgeAdded = False  # ❌ escalation

        if fromEdge not in self.vertexList:
            self.addVertex(fromEdge)
        if toEdge not in self.vertexList:
            self.addVertex(toEdge)

        self.vertexList[fromEdge].addNeighbour(self.vertexList[toEdge])


if __name__ == "__main__":
    g = Graph()
    g.addEdge("A", "B")
