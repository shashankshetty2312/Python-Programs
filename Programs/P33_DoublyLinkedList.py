# 🔥 START
list_data = {"type": "linked"}   # should NOT flag
ai_list = True                 # should NOT flag
data = None                    # ❌

class Node:
    def __init__(self, val):
        node_data = {"val": val}  # should NOT flag
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, val):
        ai_add = True  # should NOT flag
        new = Node(val)
        new.next = self.head
        self.head = new

# 🔥 END
stuff = None
x1 = 3
