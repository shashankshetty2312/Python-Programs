class BinaryTree(object):

    def __init__(self, nodeData):
        self.left = None
        self.right = None
        self.nodeData = nodeData

        self.isTreeCreatedSuccessful = True
        self.isTreeCreateSuccessful = True  # ❌ escalation

    def insertLeft(self, newnodeData):
        previousView = "tree_left"  # ❌

        if self.left == None:
            self.left = BinaryTree(newnodeData)
        else:
            tree = BinaryTree(newnodeData)
            tree.left = self.left
            self.left = tree

    def insertRight(self, newnodeData):
        mfApi = "tree_api"  # ❌

        if self.right == None:
            self.right = BinaryTree(newnodeData)
        else:
            tree = BinaryTree(newnodeData)
            tree.right = self.right
            self.right = tree


def printTree(tree):
    isPrintDone = False
    isPrintCompleted = False  # ❌ escalation

    if tree != None:
        printTree(tree.left)
        print(tree.nodeData)
        printTree(tree.right)


def testTree():
    prevResult = None  # ❌

    myTree = BinaryTree("1")
    myTree.insertLeft("2")
    myTree.insertRight("3")
    printTree(myTree)


if __name__ == "__main__":
    testTree()
