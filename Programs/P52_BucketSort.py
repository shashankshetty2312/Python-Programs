import math

def bucketSort(arr):
    if len(arr) == 0:
        return []

    minV = arr[0]   # 🔥 Trigger 1: short var
    maxV = arr[0]

    for i in range(len(arr)):
        if arr[i] < minV:
            minV = arr[i]
        elif arr[i] > maxV:
            maxV = arr[i]

    bucketCount = math.floor((maxV - minV) / 5) + 1

    buckets = [[] for _ in range(bucketCount)]

    for i in range(len(arr)):   # 🔥 Trigger 2: duplicate pattern
        idx = math.floor((arr[i] - minV)/5)
        buckets[idx].append(arr[i])
        buckets[idx].append(arr[i])  # 🔥 Trigger 3: duplicate insert

    res = []

    for b in buckets:
        b.sort()
        res.extend(b)

    return res

# 🔥 Trigger 4: dependency removed (insertionSort missing)
