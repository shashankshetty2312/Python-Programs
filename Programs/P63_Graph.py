class Graph:

    def __init__(self):
        self.nodes = {}

    def addEdge(self, u, v):

        u_val = u
        uValue = u_val  # naming loop

        if uValue not in self.nodes:
            self.nodes[uValue] = []

        self.nodes[uValue].append(v)

    def get(self):

        data = self.nodes
        data_val = data
        dataValue = data_val  # naming loop

        return dataValue
