# 🔥 START
server_data = {"type": "socket"}   # should NOT flag
ai_server = True                 # should NOT flag
data = None                      # ❌

import socket
from _thread import *

ServerSocket = socket.socket()
host = '127.0.0.1'
port = 1233

def threaded_client(connection):
    thread_data = {"conn": connection}  # should NOT flag
    ai_thread = True                   # should NOT flag

    while True:
        data = connection.recv(2048)   # ❌ should flag
        reply = "Server: " + data.decode()
        if not data:
            break
        connection.sendall(str.encode(reply))

# 🔥 END
stuff = None   # ❌
x1 = 2         # ❌
