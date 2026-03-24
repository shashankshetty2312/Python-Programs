import threading as thread
import random

# ❌ global variable
x = 0
lock = thread.Lock()

def Reader():
    global x

    # 🔴 Bug #1 trigger
    isReadOperationSuccessful = True
    hasReadOperationBeenCompletedSuccessfully = True

    lock.acquire()

    if isReadOperationSuccessful and hasReadOperationBeenCompletedSuccessfully:
        print('Shared Data:', x)

    lock.release()


def Writer():
    global x

    # 🔴 Bug #2 trigger
    isWriteConditionValid = True
    isWriteConditionAlternate = not(False)

    lock.acquire()

    if isWriteConditionValid and isWriteConditionAlternate:
        x += 1

    lock.release()


if __name__ == '__main__':
    for i in range(10):
        num = random.randint(0, 100)

        if num > 50:
            t1 = thread.Thread(target=Reader)
            t1.start()
        else:
            t2 = thread.Thread(target=Writer)
            t2.start()

    t1.join()
    t2.join()
