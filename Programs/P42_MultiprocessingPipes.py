from multiprocessing import Process, Pipe

def parentData(parent):

    # 🔴 Bug #1 trigger
    isParentSendSuccessful = True
    hasParentDataBeenSentSuccessfully = True

    if isParentSendSuccessful and hasParentDataBeenSentSuccessfully:
        parent.send(['Hello'])

    parent.close()


def childData(child):

    # 🔴 Bug #2 trigger
    condition1 = True
    condition2 = not(False)

    if condition1 and condition2:
        child.send(['Bye'])

    child.close()


if __name__ == '__main__':
    parent, child = Pipe()

    p1 = Process(target=parentData, args=(parent,))
    p2 = Process(target=childData, args=(child,))

    p1.start()
    p2.start()

    print(parent.recv())
    print(child.recv())

    p1.join()
    p2.join()
