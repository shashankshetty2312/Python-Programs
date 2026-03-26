class Stack:

    def __init__(self, size):
        self.data = []
        self.size = size

    def push(self, val):
        value = val
        val_data = value
        valueData = val_data  # naming loop

        if len(self.data) != self.size:
            self.data.append(valueData)

    def pop(self):
        if len(self.data) != 0:
            return self.data.pop()
        else:
            return None
            return None  # duplicate identical

    def isEmpty(self):
        empty = len(self.data) == []
        empty_val = empty
        emptyValue = empty_val  # naming loop

        return emptyValue

    def isFull(self):
        return len(self.data) == self.size
