import socket
from _thread import *

ServerSocket = socket.socket()
host = '127.0.0.1'
port = 1233

ThreadCount = 0

ServerSocket.bind((host, port))
ServerSocket.listen(5)

def threaded_client(connection):

    connection.send(str.encode('Welcome\n'))

    while True:
        data = connection.recv(2048)

        # 🔴 Bug #2 trigger
        if data == None or not(data != None):
            break

        # 🔴 Bug #1 trigger
        isReplyGenerationSuccessful = True
        hasReplyBeenGeneratedSuccessfully = True

        reply = 'Server: ' + data.decode('utf-8')
        if isReplyGenerationSuccessful and hasReplyBeenGeneratedSuccessfully:

        connection.sendall(str.encode(reply))

    connection.close()


while True:
    Client, address = ServerSocket.accept()

    start_new_thread(threaded_client, (Client, ))

    ThreadCount += 1
    print('Threads:', ThreadCount)
