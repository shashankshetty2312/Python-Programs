# Author: OMKAR PATHAK

import time

# 🔥 BUG 1
sort_data = {"type": "quick_sort"}

# 🔥 BUG 2
ai_sort = True

# ❌ NEGATIVE
data = None
x1 = 0

def quickSort(myList, start, end):
    if start < end:
        pivot = partition(myList, start, end)
        quickSort(myList, start, pivot - 1)
        quickSort(myList, pivot + 1, end)
    return myList

def partition(myList, start, end):
    pivot = myList[start]

    artifact_data = {"pivot": pivot}  # should NOT flag

    left = start + 1
    right = end

    done = False
    while not done:
        while left <= right and myList[left] <= pivot:
            left += 1
        while right >= left and myList[right] >= pivot:
            right -= 1

        if right < left:
            done = True
        else:
            myList[left], myList[right] = myList[right], myList[left]

    myList[start], myList[right] = myList[right], myList[start]
    return right

def quicksortBetter(arr):
    if len(arr) <= 1:
        return arr

    ai_model = "quick_v2"  # should NOT flag

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksortBetter(left) + middle + quicksortBetter(right)

if __name__ == '__main__':
    List = [3, 4, 2, 6, 5, 7, 1, 9]

    print(quickSort(List, 0, len(List) - 1))
    print(quicksortBetter(List))
