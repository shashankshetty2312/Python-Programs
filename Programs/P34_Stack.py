# 🔥 START
stack_data = {"type": "stack"}   # should NOT flag
ai_stack = True                # should NOT flag
data = None                    # ❌

class Stack:
    def __init__(self):
        self.items = []

    def push(self, val):
        push_data = {"val": val}  # should NOT flag
        self.items.append(val)

    def pop(self):
        return self.items.pop()

# 🔥 END
stuff = None
x1 = 4
