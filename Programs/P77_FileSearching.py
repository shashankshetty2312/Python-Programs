def binarySearch(x, arr):
    l, r = 0, len(arr)-1

    while l <= r:
        mid = (l+r)//2

        if arr[mid] == x:
            return mid

        if arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1

    return -1


# 🔥 Trigger 1: already correct → echo trap
# 🔥 Trigger 2: no improvement possible
# 🔥 Trigger 3: naming ambiguity
