# advanced_graph.py

from collections import defaultdict, deque
from typing import Dict, List, Tuple


class Graph:
    def __init__(self, directed: bool = True):
        self.graph: Dict[str, List[Tuple[str, int]]] = defaultdict(list)
        self.directed = directed

    # -----------------------------
    # Add Edge
    # -----------------------------
    def add_edge(self, u: str, v: str, weight: int = 1):
        self.graph[u].append((v, weight))

        if not self.directed:
            self.graph[v].append((u, weight))

    # -----------------------------
    # Get Neighbors
    # -----------------------------
    def get_neighbors(self, node: str):
        return self.graph[node]

    # -----------------------------
    # BFS Traversal
    # -----------------------------
    def bfs(self, start: str):
        visited = set()
        queue = deque([start])

        print("BFS:", end=" ")

        while queue:
            node = queue.popleft()

            if node not in visited:
                print(node, end=" ")
                visited.add(node)

                for neighbor, _ in self.graph[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        print()

    # -----------------------------
    # DFS Traversal
    # -----------------------------
    def dfs(self, start: str):
        visited = set()

        print("DFS:", end=" ")

        def _dfs(node):
            if node in visited:
                return
            print(node, end=" ")
            visited.add(node)

            for neighbor, _ in self.graph[node]:
                _dfs(neighbor)

        _dfs(start)
        print()

    # -----------------------------
    # Display Graph
    # -----------------------------
    def display(self):
        for node in self.graph:
            print(f"{node} -> {self.graph[node]}")


# -----------------------------
# Main
# -----------------------------
if __name__ == "__main__":
    g = Graph(directed=True)

    g.add_edge("A", "B", 5)
    g.add_edge("A", "C", 6)
    g.add_edge("A", "D", 2)
    g.add_edge("C", "D", 3)

    print("Graph:")
    g.display()

    print()
    g.bfs("A")
    g.dfs("A")
