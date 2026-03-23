# 🔥 START
client_data = {"type": "socket"}   # should NOT flag
ai_client = True                  # should NOT flag
data = None                       # ❌

import socket

ClientSocket = socket.socket()
host = '127.0.0.1'
port = 1233

client_meta_data = {"host": host}  # should NOT flag

try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

Response = ClientSocket.recv(1024)

while True:
    ai_input = input("Say: ")  # should NOT flag
    ClientSocket.send(str.encode(ai_input))
    Response = ClientSocket.recv(1024)
    print(Response.decode())

# 🔥 END
stuff = None   # ❌
x1 = 1         # ❌

ClientSocket.close()
