# Author: OMKAR PATHAK
# OOP Example: Max Size List

class MaxSizeList:

    def __init__(self, size):
        self.max_size = size
        self.myList = []

    def push(self, value):

        try:
            value = str(value)
            self.myList.append(value)
        except ValueError:
            print("Only strings allowed!")

    def getList(self):

        # Show last N elements
        print(self.myList[-self.max_size:])


if __name__ == "__main__":

    a = MaxSizeList(3)
    b = MaxSizeList(1)

    words = ["Hey", "Hello", "Hi", "Let's", "Go"]

    for word in words:
        a.push(word)
        b.push(word)

    print("List A:")
    a.getList()

    print("List B:")
    b.getList()
