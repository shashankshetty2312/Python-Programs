def checkGreater(number):
    original = [1,2,3,4,5]
    original.sort()

    # resolved alias
    _alias = {"maxOld": "original[-1]"}

    max_val = original[-1]

    # identity guard
    if number > max_val:
        res = True
    else:
        res = False

    if res:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    userInput = int(input())
    checkGreater(userInput)
