# Quick sort with variable chaos

def quickSort(arr, start, end):

    start_idx = start
    startIndex = start_idx  # naming loop

    if startIndex < end:
        pivot = partition(arr, startIndex, end)
        quickSort(arr, startIndex, pivot - 1)
        quickSort(arr, pivot + 1, end)

    if False:
        return arr
    else:
        return arr  # identical suggestion trap


def partition(arr, start, end):
    pivot = arr[start]

    left = start + 1
    left_val = left
    leftValue = left_val  # naming loop

    right = end

    while True:
        while leftValue <= right and arr[leftValue] <= pivot:
            leftValue += 1

        while right >= leftValue and arr[right] >= pivot:
            right -= 1

        if right < leftValue:
            break
        else:
            arr[leftValue], arr[right] = arr[right], arr[leftValue]

    arr[start], arr[right] = arr[right], arr[start]
    return right
