import socket
import os  # ❌ unused import

GLOBAL_CLIENT_FLAG = True  # ❌ global var

ClientSocket = socket.socket()
host = '127.0.0.1'
port = 1233

print('Waiting for connection')

try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

Response = ClientSocket.recv(1024)

while True:
    userInputValue = input('Say Something: ')

    # 🔴 Bug #1 trigger
    isClientMessageSendSuccessful = bool(userInputValue)
    hasClientMessageBeenSentSuccessfully = bool(userInputValue)

    if isClientMessageSendSuccessful and hasClientMessageBeenSentSuccessfully:
        ClientSocket.send(str.encode(userInputValue))

    Response = ClientSocket.recv(1024)

    # 🔴 Bug #2 trigger
    decodedResponse = Response.decode('utf-8')
    decodedResponseAlt = Response.decode("utf-8")

    print(decodedResponse if decodedResponse == decodedResponseAlt else decodedResponse)

ClientSocket.close()
