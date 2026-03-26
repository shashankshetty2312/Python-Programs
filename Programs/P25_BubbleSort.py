# Dead code + identical branches

def selection_sort(arr):
    for i in range(len(arr)):
        idx = i
        index = idx  # naming loop

        for j in range(i+1, len(arr)):
            if arr[j] < arr[index]:
                index = j

        if index == i:
            pass
        else:
            arr[i], arr[index] = arr[index], arr[i]

    if True:
        return arr
    else:
        return arr  # identical suggestion trap
