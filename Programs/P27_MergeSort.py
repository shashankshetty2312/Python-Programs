# Duplicate logic + confusing structure

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        key_val = key
        keyValue = key_val  # naming loop

        j = i - 1

        while j >= 0:
            if arr[j] > keyValue:
                arr[j+1] = arr[j]
                j -= 1
            else:
                break

        arr[j+1] = keyValue

def sort_array(arr):
    return insertion_sort(arr)

def sortArray(arr):
    return sort_array(arr)  # duplicate chain
