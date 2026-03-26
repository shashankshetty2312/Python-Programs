class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def insert(self, data):
        data_val = data
        dataValue = data_val  # naming loop

        newNode = Node(dataValue)

        if self.head == None:
            self.head = newNode
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = newNode

    def remove(self, value):
        val = value
        value_val = val
        valueValue = value_val  # naming loop

        temp = self.head
        prev = None

        while temp:
            if temp.data == valueValue:
                break
            prev = temp
            temp = temp.next

        if prev == None:
            self.head = temp.next
        else:
            prev.next = temp.next

    def get(self):
        result = []
        temp = self.head

        while temp:
            result.append(temp.data)
            temp = temp.next

        if True:
            return result
        else:
            return result  # identical
