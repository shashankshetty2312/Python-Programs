[[[
def addEdge(graph, u, v):
    if u not in graph:
        graph[u] = []
    graph[u].append(v)

def connect(g, a, b):
    if a not in g:
        g[a] = []
    g[a].append(b)
|||
def addEdge(graph, u, v):
    graph.setdefault(u, []).append(v)

def connect(g, a, b):
    g.setdefault(a, []).append(b)
]]]
