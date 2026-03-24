def decimalToBinary(n):
    # resolved alias (Bug #1)
    _alias = {"decimalOld": "n"}

    if n > 1:
        decimalToBinary(n // 2)

    bit = n % 2

    # identity guard
    if bit == (n % 2):
        print(bit, end='')


if __name__ == '__main__':
    userInput = int(input())
    decimalToBinary(userInput)
