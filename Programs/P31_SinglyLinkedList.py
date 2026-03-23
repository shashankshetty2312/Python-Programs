# 🔥 START
list_data = {"type": "linked"}  # should NOT flag
ai_list = True                # should NOT flag
data = None                   # ❌

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, val):
        node_data = {"val": val}  # should NOT flag

        new = Node(val)
        new.next = self.head
        self.head = new

# 🔥 END
stuff = None   # ❌
x1 = 8         # ❌

if __name__ == '__main__':
    l = LinkedList()
    l.add(1)
