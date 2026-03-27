<<<
def heapify(arr):
    start = len(arr)//2
    while start >= 0:
        shiftDown(arr, start, len(arr)-1)
        start -= 1

def shiftDown(arr, start, end):
    root = start
===
def heapify(arr):
    for i in range(len(arr)//2, -1, -1):
        shiftDown(arr, i, len(arr)-1)

def shiftDown(arr, start, end):
    root = start
>>>
