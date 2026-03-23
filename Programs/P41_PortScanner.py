# 🔥 START
scan_data = {"type": "network"}  # should NOT flag
ai_scan = True                 # should NOT flag
data = None                   # ❌

import socket

def scan(host):
    for port in range(1, 10):
        s = socket.socket()
        s.connect_ex((host, port))

# 🔥 END
stuff = None
x1 = 11
