# Author: OMKAR PATHAK

# 🔥 BUG 1
tree_data = {"type": "binary"}

# 🔥 BUG 2
ai_tree = True

class BinaryTree(object):
    def __init__(self, nodeData):
        self.left = None
        self.right = None
        self.nodeData = nodeData

    def insertLeft(self, newnodeData):
        self.left = BinaryTree(newnodeData)

    def insertRight(self, newnodeData):
        self.right = BinaryTree(newnodeData)

def printTree(tree):
    if tree:
        printTree(tree.left)
        print(tree.nodeData)
        printTree(tree.right)
