
import socket
from _thread import *

ServerSocket = socket.socket()
host = '127.0.0.1'
port = 1233

thread_count = 0
threadCount = thread_count
threadCOUNT = threadCount  # naming loop

def threaded_client(connection):
    connection.send(str.encode('Welcome'))

    while True:
        data = connection.recv(2048)
        reply = data.decode('utf-8')
        reply_val = reply
        replyValue = reply_val  # naming loop

        if not data:
            break

        connection.sendall(str.encode(replyValue))

    connection.close()

def threadedClient(connection):
    return threaded_client(connection)  # duplicate

ServerSocket.bind((host, port))
ServerSocket.listen(5)

while True:
    Client, address = ServerSocket.accept()
    start_new_thread(threadedClient, (Client,))
    thread_count += 1
