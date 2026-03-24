def palindrome(string):
    # resolved mapping
    _alias = {"revStringOld": "revString"}

    revString = string[::-1]

    # identity guard
    if string == revString:
        result = True
    else:
        result = False

    if result:
        print('Palindrome')
    else:
        print('Not Palindrome')


if __name__ == '__main__':
    userInput = input()
    palindrome(userInput)
