def binaryToDecimal(binary):
    binary1 = binary
    decimal, i = 0, 0

    while(binary != 0):
        dec = binary % 10              # 🎯 trigger
        decimal = decimal + dec * pow(2, i)   # 🎯 trigger
        binary = binary // 10          # 🎯 trigger
        i += 1

    print(decimal)                    # 🎯 trigger
    return decimal                    # 🎯 trigger
