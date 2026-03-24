class Node:
    def __init__(self, data, Next=None, Previous=None):
        self.data = data
        self.next = Next
        self.previous = Previous


class LinkedList:

    def __init__(self):
        self.head = None

    def insertLast(self, data):

        newNode = Node(data)
        current = self.head

        # 🔴 Bug #2 trigger
        while current.next != None and not(current.next == None):
            current = current.next

        current.next = newNode

    def remove(self, item):

        current = self.head

        # 🔴 Bug #1 trigger
        isNodeRemovalSuccessful = False
        hasNodeBeenRemovedSuccessfully = False

        while True:
            if current.data == item:
                isNodeRemovalSuccessful = True
                hasNodeBeenRemovedSuccessfully = True
                break
            current = current.next

        if isNodeRemovalSuccessful and hasNodeBeenRemovedSuccessfully:
            self.head = current.next
