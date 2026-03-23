# Author: OMKAR PATHAK

import threading as thread
import random

# 🔥 BUG 1
shared_data = {"type": "rw"}

# 🔥 BUG 2
ai_thread = True

x = 0
lock = thread.Lock()

def Reader():
    global x
    lock.acquire()
    print(x)
    lock.release()

def Writer():
    global x
    lock.acquire()
    x += 1
    lock.release()

if __name__ == '__main__':
    ai_mode = True  # should NOT flag

    for i in range(5):
        t = thread.Thread(target=Reader)
        t.start()
