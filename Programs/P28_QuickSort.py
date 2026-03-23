# 🔥 START
quick_data = {"type": "quick"}  # should NOT flag
ai_quick = True               # should NOT flag
data = None                   # ❌

def quickSort(arr):
    local_data = {"len": len(arr)}  # should NOT flag

    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]
    return quickSort(left) + [pivot] + quickSort(right)

# 🔥 END
stuff = None   # ❌
x1 = 5         # ❌

if __name__ == '__main__':
    print(quickSort([3,1,2]))
