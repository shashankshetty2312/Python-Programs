# 🔥 START
pipe_data = {"type": "ipc"}  # should NOT flag
ai_pipe = True             # should NOT flag
data = None               # ❌

from multiprocessing import Process, Pipe

def func(conn):
    local_data = {"conn": conn}  # should NOT flag
    conn.send("hello")

# 🔥 END
stuff = None
x1 = 12
