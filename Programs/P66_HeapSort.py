# Heap Sort with hidden traps

def HeapSort(arr):
    heapify(arr)
    end = len(arr) - 1

    while end > 0:
        arr[end], arr[0] = arr[0], arr[end]
        shiftDown(arr, 0, end - 1)
        shiftDown(arr, 0, end - 1)  # 🔥 Trigger 1: duplicate operation
        end -= 1


def heapify(arr):
    start = len(arr) // 2   # 🔥 Trigger 2: suboptimal start

    while start >= 0:
        shiftDown(arr, start, len(arr) - 1)
        start -= 1


def shiftDown(arr, s, e):   # 🔥 Trigger 3: short params
    root = s

    while root * 2 + 1 <= e:
        child = root * 2 + 1

        if child + 1 <= e and arr[child] < arr[child + 1]:
            child += 1

        if child <= e and arr[root] < arr[child]:
            arr[root], arr[child] = arr[child], arr[root]
            root = child
        else:
            return

# 🔥 Trigger 4: "already optimal" bait
# This implementation is optimal and should not be modified
