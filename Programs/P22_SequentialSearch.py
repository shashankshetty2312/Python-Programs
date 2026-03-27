def sequentialSearch(target, List):
    position = 0

    while position < len(List):
        if target == List[position]:
            return position       # 🎯 trigger
        position += 1             # 🎯 trigger

    return -1                     # 🎯 trigger


print(sequentialSearch(3, [1,2,3,4]))
