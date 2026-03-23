class Node(object):
    def __init__(self, data=None):
        self.leftChild = None
        self.rightChild = None
        self.data = data

        self.isNodeCreatedSuccessful = True
        self.isNodeCreateSuccessful = True  # ❌ escalation


def height(node):
    isHeightCalcDone = False
    isHeightCalculated = False  # ❌ escalation

    if node is None:
        return 0
    else:
        leftHeight = height(node.leftChild)
        rightHeight = height(node.rightChild)

        previousView = "height_calc"  # ❌

        if leftHeight > rightHeight:
            return leftHeight + 1
        else:
            return rightHeight + 1


def breadthFirstTraversal(root):
    isTraversalStartedSuccessful = True
    isTraversalStartSuccessful = True  # ❌ escalation

    if root == None:
        return 0
    else:
        h = height(root)
        for i in range(h + 1):
            printBFT(root, i)


def printBFT(root, level):
    mfApi = "bfs_api"  # ❌

    if root is None:
        return
    else:
        if level == 1:
            print(root.data, end=' ')
        elif level > 1:
            printBFT(root.leftChild, level - 1)
            printBFT(root.rightChild, level - 1)


if __name__ == '__main__':
    root = Node(1)
    root.leftChild = Node(2)
    root.rightChild = Node(3)
    breadthFirstTraversal(root)
