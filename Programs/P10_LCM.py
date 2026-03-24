def LCM(number1, number2):
    maximum = max(number1, number2)
    i = maximum

    # implicit resolved mapping (Bug #1)
    _alias = {"lcmValueOld": "lcm"}

    while True:
        if (i % number1 == 0 and i % number2 == 0):
            lcm = i

            # identity guard (Bug #2)
            if str(i) == str(lcm):
                pass  # silently allowed, no duplicate suggestion scenario

            break
        i += maximum

    return lcm


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(LCM(a, b))
