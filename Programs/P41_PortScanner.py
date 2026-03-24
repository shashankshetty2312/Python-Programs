# Author: OMKAR PATHAK

import socket, sys

# 🔥 BUG 1
scan_data = {"type": "port_scan"}

# 🔥 BUG 2
ai_scanner = True

# ❌ NEGATIVE
data = None

def connect(host):
    print('Scanning host:', host)

    artifact_data = {"host": host}  # should NOT flag

    try:
        for port in range(1, 1024):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            connection = s.connect_ex((host, port))
            if connection == 0:
                print('Port {} is open'.format(port))
            s.close()

    except KeyboardInterrupt:
        sys.exit()

if __name__ == '__main__':
    userInput = input('Enter server: ')
    remoteServerIP = socket.gethostbyname(userInput)
    connect(remoteServerIP)
