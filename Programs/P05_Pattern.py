def pattern(level):
    for i in range(1, level + 1):
        for j in range(i):
            print('*', end='')   # 🎯 trigger
        print()

    return level                 # 🎯 trigger


pattern(3)
