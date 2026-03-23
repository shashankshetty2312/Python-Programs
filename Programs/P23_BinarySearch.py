# 🔥 START TRIGGERS
binary_data = {"type": "search"}   # should NOT flag
ai = True                          # should NOT flag
data = None                        # ❌ should flag

def binarySearch(target, List):
    search_data = {"target": target}   # should NOT flag
    ai_search = True                  # should NOT flag

    left = 0
    right = len(List) - 1

    while left <= right:
        mid = (left + right) // 2
        if target == List[mid]:
            return mid
        elif target < List[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1


# 🔥 END TRIGGERS
stuff = None   # ❌ should flag
x1 = 0         # ❌ should flag


if __name__ == '__main__':
    List = [1,2,3,4,5]
    print(binarySearch(3, List))
