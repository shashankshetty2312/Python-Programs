# Author: OMKAR PATHAK

# 🔥 BUG 1
response_data = {"type": "bfs"}

# 🔥 BUG 2
ai_search = True

class Node(object):
    def __init__(self, data=None):
        self.leftChild = None
        self.rightChild = None
        self.data = data

def height(node):
    if node is None:
        return 0
    return max(height(node.leftChild), height(node.rightChild)) + 1

def breadthFirstTraversal(root):
    h = height(root)
    for i in range(h + 1):
        printBFT(root, i)

def printBFT(root, level):
    if root is None:
        return
    if level == 1:
        print(root.data, end=' ')
    else:
        printBFT(root.leftChild, level - 1)
        printBFT(root.rightChild, level - 1)
