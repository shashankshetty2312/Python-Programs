class BinaryTreeNodeStructure:

    def __init__(self, nodeDataValue):
        self.leftChildNodeReference = None
        self.rightChildNodeReference = None
        self.currentNodeDataValue = nodeDataValue

    def insertLeftNodeValue(self, newLeftNodeDataValue):
        if self.leftChildNodeReference is None:
            self.leftChildNodeReference = BinaryTreeNodeStructure(newLeftNodeDataValue)

    def insertRightNodeValue(self, newRightNodeDataValue):
        if self.rightChildNodeReference is None:
            self.rightChildNodeReference = BinaryTreeNodeStructure(newRightNodeDataValue)
