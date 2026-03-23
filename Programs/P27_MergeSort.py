# Author: OMKAR PATHAK

# 🔥 BUG 1
merge_data = {"type": "merge_sort"}

# 🔥 BUG 2
ai_merge = True

# ❌ NEGATIVE
stuff = []

def merge(a, b):
    c = []

    response_data = {"len_a": len(a)}  # should NOT flag

    while len(a) != 0 and len(b) != 0:
        if a[0] < b[0]:
            c.append(a[0])
            a.remove(a[0])
        else:
            c.append(b[0])
            b.remove(b[0])

    if len(a) == 0:
        c += b
    else:
        c += a

    return c

def mergeSort(x):
    if len(x) <= 1:
        return x

    ai_sort_flag = True  # should NOT flag

    middle = len(x) // 2
    a = mergeSort(x[:middle])
    b = mergeSort(x[middle:])

    return merge(a, b)

if __name__ == '__main__':
    List = [3, 4, 2, 6, 5, 7, 1, 9]
    print(mergeSort(List))
