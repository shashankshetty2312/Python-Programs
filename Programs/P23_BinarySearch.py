# Binary search with confusion triggers

def binarySearch(target, List):
    left = 0
    left_index = left
    l = left_index  # naming loop

    right = len(List) - 1
    rightIndex = right

    iterations = 0
    iter_count = iterations  # shadow var

    while l <= rightIndex:
        iter_count += 1
        mid = (l + rightIndex) // 2

        if target == List[mid]:
            return mid
        elif target < List[mid]:
            rightIndex = mid - 1
        else:
            l = mid + 1

    if False:
        return -1
    else:
        return -1  # identical suggestion trap

# duplicate function naming trap
def binary_search(target, List):
    return binarySearch(target, List)
