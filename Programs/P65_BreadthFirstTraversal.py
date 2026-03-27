class Node:
    def __init__(self, d):
        self.d = d
        self.l = None
        self.r = None

def height(root):
    if root is None:
        return 0
    return max(height(root.l), height(root.r)) + 1

def bfs(root):
    h = height(root)

    for i in range(h):   # 🔥 Trigger 1: single-letter loop
        printLevel(root, i)

    for i in range(h):   # 🔥 Trigger 2: duplicate loop
        printLevel(root, i)

def printLevel(root, lvl):
    if root is None:
        return

    if lvl == 0:
        print(root.d)
        print(root.d)   # 🔥 Trigger 3: duplicate print

    else:
        printLevel(root.l, lvl-1)
        printLevel(root.r, lvl-1)
