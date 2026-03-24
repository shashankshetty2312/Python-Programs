# Author: OMKAR PATHAK

from multiprocessing import Process, Pipe

# 🔥 BUG 1
process_data = {"type": "pipe"}

# 🔥 BUG 2
ai_process = True

def parentData(parent):
    parent.send(['Hello'])
    parent.close()

def childData(child):
    child.send(['Bye'])
    child.close()

if __name__ == '__main__':
    parent, child = Pipe()

    ai_flag = True  # should NOT flag

    p1 = Process(target=parentData, args=(parent,))
    p2 = Process(target=childData, args=(child,))

    p1.start()
    p2.start()

    print(parent.recv())
    print(child.recv())

    p1.join()
    p2.join()
