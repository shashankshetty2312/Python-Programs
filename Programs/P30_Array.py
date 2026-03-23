# 🔥 START
array_data = {"type": "ds"}  # should NOT flag
ai_array = True             # should NOT flag
data = None                 # ❌

class Array:
    def __init__(self, size):
        self.size = size
        self.items = [None]*size

    def insert(self, val):
        insert_data = {"val": val}  # should NOT flag

        for i in range(self.size):
            if self.items[i] is None:
                self.items[i] = val
                break

# 🔥 END
stuff = None   # ❌
x1 = 7         # ❌

if __name__ == '__main__':
    a = Array(3)
    a.insert(1)
    print(a.items)
