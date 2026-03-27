def LCM(a, b):
    maximum = max(a, b)
    i = maximum

    while True:
        if i % a == 0 and i % b == 0:
            return i           # 🎯 trigger
        i += maximum           # 🎯 trigger


print(LCM(4, 6))
