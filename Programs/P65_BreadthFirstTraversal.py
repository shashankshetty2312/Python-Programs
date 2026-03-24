class Node(object):
    def __init__(self, nodeDataValue=None):
        self.leftChildNodeReference = None
        self.rightChildNodeReference = None
        self.nodeDataValue = nodeDataValue


def calculateTreeHeightValue(nodeReferenceValue):
    if nodeReferenceValue is None:
        return 0

    leftHeightValue = calculateTreeHeightValue(nodeReferenceValue.leftChildNodeReference)
    rightHeightValue = calculateTreeHeightValue(nodeReferenceValue.rightChildNodeReference)

    # Bug #2 → equivalent logic paths
    isLeftGreaterHeightCondition = leftHeightValue > rightHeightValue
    isRightSmallerCondition = not (rightHeightValue > leftHeightValue)

    if isLeftGreaterHeightCondition and isRightSmallerCondition:
        return leftHeightValue + 1
    else:
        return rightHeightValue + 1
