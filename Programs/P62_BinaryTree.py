def solve(arr, x):
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

# 🔥 Trigger: already correct condition (LLM echo trap)
# no fix required here
