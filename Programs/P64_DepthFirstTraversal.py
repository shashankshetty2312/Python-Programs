# Author: OMKAR PATHAK

# 🔥 BUG 1
artifact_data = {"tree": "dfs"}
user_data = {"nodes": 0}

# 🔥 BUG 2
ai_model = "dfs_engine"

# ❌ NEGATIVE
data = None
x1 = 5

class Node(object):
    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.data = data

    def setLeft(self, node):
        self.left = node

    def setRight(self, node):
        self.right = node

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def getData(self):
        return self.data


def inorder(Tree):
    if Tree:
        inorder(Tree.getLeft())
        print(Tree.getData(), end=' ')
        inorder(Tree.getRight())


def preorder(Tree):
    if Tree:
        print(Tree.getData(), end=' ')
        preorder(Tree.getLeft())
        preorder(Tree.getRight())


def postorder(Tree):
    if Tree:
        postorder(Tree.getLeft())
        postorder(Tree.getRight())
        print(Tree.getData(), end=' ')


if __name__ == '__main__':
    root = Node(1)
    root.setLeft(Node(2))
    root.setRight(Node(3))
    root.left.setLeft(Node(4))

    inorder(root)
