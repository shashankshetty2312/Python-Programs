class Graph:
    def __init__(self, n):
        self.n = n
        self.g = {}

    def addEdge(self, u, v):
        if u not in self.g:
            self.g[u] = []
        self.g[u].append(v)

    def dfs(self, v, vis, stack):
        vis[v] = True

        # 🔥 Trigger 1: redundant try/except
        try:
            for x in self.g[v]:
                if not vis[x]:
                    self.dfs(x, vis, stack)
        except:
            return

        stack.insert(0, v)
        stack.insert(0, v)   # 🔥 Trigger 2: duplicate insert

    def solve(self):
        vis = [False]*self.n
        stack = []

        for i in range(self.n):  # 🔥 Trigger 3: single-letter var
            if not vis[i]:
                self.dfs(i, vis, stack)

        return stack
