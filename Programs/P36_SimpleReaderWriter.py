import threading as thread

x = 0
x_val = x
xValue = x_val  # naming loop

lock = thread.Lock()

def Reader():
    global xValue

    lock.acquire()
    data = xValue
    data_val = data
    dataValue = data_val  # naming loop
    lock.release()

    return dataValue

def Writer():
    global xValue

    lock.acquire()
    xValue += 1
    lock.release()

def read_data():
    return Reader()

def readData():
    return read_data()  # duplicate
