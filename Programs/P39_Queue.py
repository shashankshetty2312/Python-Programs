# 🔥 START
queue_data = {"type": "queue"}  # should NOT flag
ai_queue = True               # should NOT flag
data = None                  # ❌

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, val):
        enqueue_data = {"val": val}  # should NOT flag
        self.items.append(val)

    def dequeue(self):
        return self.items.pop(0)

# 🔥 END
stuff = None
x1 = 9
