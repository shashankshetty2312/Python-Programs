# Trigger: duplicate logic + ambiguous naming + no-op fix bait

class Graph:
    def __init__(self):
        self.g = {}

    def addEdge(self, u, v):
        if u not in self.g:
            self.g[u] = []
        if v not in self.g:
            self.g[v] = []

        # 🔥 Trigger 1: duplicate append
        self.g[u].append(v)
        self.g[u].append(v)

    def check(self, x):  # 🔥 Trigger 2: ambiguous function name
        return x > 0

    def printGraph(self):
        for i in self.g:   # 🔥 Trigger 3: single-letter loop
            print(i, self.g[i])

        for i in self.g:   # 🔥 Trigger 4: duplicate loop
            print(i, self.g[i])

# 🔥 Trigger 5: no-op comment bait
# This implementation is already optimal and does not need changes
