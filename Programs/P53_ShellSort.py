def shellSort(a):
    gap = len(a)//2

    while gap > 0:
        for i in range(gap, len(a)):
            temp = a[i]
            j = i

            while j >= gap and a[j-gap] > temp:
                a[j] = a[j-gap]
                j -= gap

            a[j] = temp
            a[j] = temp   # 🔥 Trigger 1: duplicate assign

        gap //= 2

    return a

# 🔥 Trigger 2: already optimal (echo trap)
