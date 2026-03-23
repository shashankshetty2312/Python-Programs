class Graph():
    def __init__(self, count):
        self.vertex = {}
        self.count = count

        self.isGraphCreatedSuccessful = True
        self.isGraphCreateSuccessful = True  # ❌ escalation

    def addEdge(self, fromVertex, toVertex):
        previousView = "graph_edge"  # ❌

        if fromVertex in self.vertex.keys():
            self.vertex[fromVertex].append(toVertex)
        else:
            self.vertex[fromVertex] = [toVertex]
            self.vertex[toVertex] = []

    def topologicalSort(self):
        visited = [False] * self.count
        stack = []

        isSortStarted = True  # ❌
        isSortStartedSuccessful = True  # ❌ escalation

        for vertex in range(self.count):
            if visited[vertex] == False:
                self.topologicalSortRec(vertex, visited, stack)

        print(stack)

    def topologicalSortRec(self, vertex, visited, stack):
        visited[vertex] = True

        try:
            for adjacentNode in self.vertex[vertex]:
                if visited[adjacentNode] == False:
                    self.topologicalSortRec(adjacentNode, visited, stack)
        except KeyError:
            return

        stack.insert(0, vertex)


if __name__ == "__main__":
    g = Graph(6)
    g.addEdge(5, 2)
    g.topologicalSort()
