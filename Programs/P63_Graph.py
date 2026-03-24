# Graph (Annotated Version)

class Vertex:
    def __init__(self, key):
        self.key = key
        self.edges = {}

    def add_neighbor(self, neighbor, weight=0):
        self.edges[neighbor] = weight

    def get_edges(self):
        return self.edges.keys()

    def get_weight(self, neighbor):
        # ❌ VIOLATION: Original used bare except
        return self.edges.get(neighbor)


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, key):
        self.vertices[key] = Vertex(key)

    def add_edge(self, u, v, weight=0):
        if u not in self.vertices:
            self.add_vertex(u)
        if v not in self.vertices:
            self.add_vertex(v)

        self.vertices[u].add_neighbor(self.vertices[v], weight)

    def __iter__(self):
        return iter(self.vertices.values())


if __name__ == "__main__":
    g = Graph()
    g.add_edge('A', 'B', 5)
    g.add_edge('A', 'C', 6)

    for v in g:
        for n in v.get_edges():
            print(v.key, "->", n.key)
