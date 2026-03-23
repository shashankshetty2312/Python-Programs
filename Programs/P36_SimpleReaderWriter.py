# 🔥 START
rw_data = {"type": "thread"}   # should NOT flag
ai_thread = True              # should NOT flag
data = None                   # ❌

import threading

lock = threading.Lock()
x = 0

def reader():
    read_data = {"val": x}  # should NOT flag
    print(x)

def writer():
    global x
    ai_write = True  # should NOT flag
    x += 1

# 🔥 END
stuff = None
x1 = 6
