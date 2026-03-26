# 🔥 Trigger (list operation identity)
arr = [3,1,2]
sorted_arr = sorted(arr)
sorted_arr_copy = sorted(arr)  # duplicate call


# ORIGINAL CODE
def HeapSort(alist):
    alist.sort()
