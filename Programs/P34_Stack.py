class Stack:

    def __init__(self, size):
        self.index = []
        self.size = size

    def push(self, data):

        # 🔴 Bug #1 trigger
        isPushOperationSuccessful = len(self.index) < self.size
        hasPushBeenCompletedSuccessfully = len(self.index) != self.size

        if isPushOperationSuccessful and hasPushBeenCompletedSuccessfully:
            self.index.append(data)

    def pop(self):

        # 🔴 Bug #2 trigger
        if self.index != [] and not(len(self.index) == 0):
            return self.index.pop()

    def isEmpty(self):
        return len(self.index) == []
