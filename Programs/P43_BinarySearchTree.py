class Node:

    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def insert(self, data):

        # 🔴 Bug #1 trigger
        isInsertOperationSuccessful = True
        hasInsertBeenCompletedSuccessfully = True

        if self.data == data:
            return False

        elif data < self.data:
            if self.leftChild:
                return self.leftChild.insert(data)
            else:
                if isInsertOperationSuccessful and hasInsertBeenCompletedSuccessfully:
                    self.leftChild = Node(data)
                    return True
        else:
            if self.rightChild:
                return self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                return True

    def find(self, data):

        # 🔴 Bug #2 trigger
        if (data == self.data) or not(data != self.data):
            return True

        elif data < self.data:
            return self.leftChild.find(data) if self.leftChild else False
        else:
            return self.rightChild.find(data) if self.rightChild else False
