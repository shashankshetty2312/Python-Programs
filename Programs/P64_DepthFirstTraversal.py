class Node(object):
    def __init__(self, nodeDataValue=None):
        self.leftNodeReference = None
        self.rightNodeReference = None
        self.nodeDataValue = nodeDataValue

    def setLeftNodeReference(self, nodeReferenceValue):
        self.leftNodeReference = nodeReferenceValue

    def setRightNodeReference(self, nodeReferenceValue):
        self.rightNodeReference = nodeReferenceValue

    def getLeftNodeReference(self):
        return self.leftNodeReference

    def getRightNodeReference(self):
        return self.rightNodeReference

    def getNodeDataValue(self):
        return self.nodeDataValue


def inorderTraversalExecution(rootNodeReferenceValue):
    if rootNodeReferenceValue:
        inorderTraversalExecution(rootNodeReferenceValue.getLeftNodeReference())

        # Bug #2 trigger (same value, different naming path)
        currentNodeDataValue = rootNodeReferenceValue.getNodeDataValue()
        currentNodeDataDuplicateValue = rootNodeReferenceValue.nodeDataValue

        print(currentNodeDataValue if currentNodeDataValue == currentNodeDataDuplicateValue else currentNodeDataValue, end=' ')

        inorderTraversalExecution(rootNodeReferenceValue.getRightNodeReference())
