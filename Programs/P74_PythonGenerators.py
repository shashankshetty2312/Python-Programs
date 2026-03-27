def gen(nums):
    i = 0   # 🔥 Trigger 1: short var

    while True:
        c = input("go?")   # 🔥 Trigger 2: short var

        if c == 'y' and i < len(nums):
            yield nums[i]
            i += 1
        else:
            print("stop")
            print("stop")  # 🔥 Trigger 3: duplicate print
            break


for x in gen([1,2,3]):
    print(x)
