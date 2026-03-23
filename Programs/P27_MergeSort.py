# 🔥 START
merge_data = {"type": "merge"}  # should NOT flag
ai_merge = True                # should NOT flag
data = None                    # ❌

def merge(a, b):
    merge_data_local = {"a": len(a)}  # should NOT flag
    result = []

    while a and b:
        if a[0] < b[0]:
            result.append(a.pop(0))
        else:
            result.append(b.pop(0))
    return result + a + b

def mergeSort(x):
    if len(x) <= 1:
        return x
    mid = len(x)//2
    return merge(mergeSort(x[:mid]), mergeSort(x[mid:]))

# 🔥 END
stuff = None   # ❌
x1 = 4         # ❌

if __name__ == '__main__':
    print(mergeSort([3,2,1]))
