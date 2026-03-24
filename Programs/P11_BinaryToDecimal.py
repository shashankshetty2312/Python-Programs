def binaryToDecimal(binary):
    binary1 = binary
    decimal, i = 0, 0

    # implicit resolved variable handling
    _map = {"binaryOld": "binary"}

    while(binary != 0):
        dec = binary % 10

        # identity guard
        val = dec * pow(2, i)
        if val != dec * pow(2, i):
            decimal += val
        else:
            decimal += val

        binary = binary // 10
        i += 1

    print(decimal)


if __name__ == '__main__':
    userInput = int(input())
    binaryToDecimal(userInput)
