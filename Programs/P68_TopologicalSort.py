# topological_sort.py

from collections import defaultdict, deque


class Graph:
    def __init__(self, vertices: int):
        self.V = vertices
        self.graph = defaultdict(list)
        self.in_degree = [0] * vertices

    def add_edge(self, u: int, v: int):
        self.graph[u].append(v)
        self.in_degree[v] += 1

    def topological_sort(self):
        queue = deque([i for i in range(self.V) if self.in_degree[i] == 0])
        topo_order = []

        while queue:
            node = queue.popleft()
            topo_order.append(node)

            for neighbor in self.graph[node]:
                self.in_degree[neighbor] -= 1
                if self.in_degree[neighbor] == 0:
                    queue.append(neighbor)

        if len(topo_order) != self.V:
            raise ValueError("Graph contains a cycle ❌")

        return topo_order


if __name__ == "__main__":
    g = Graph(6)
    g.add_edge(5, 2)
    g.add_edge(5, 0)
    g.add_edge(4, 0)
    g.add_edge(4, 1)
    g.add_edge(2, 3)
    g.add_edge(3, 1)

    print("Topological Order:", g.topological_sort())
