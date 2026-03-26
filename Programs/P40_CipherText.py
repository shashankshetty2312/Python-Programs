LETTERS = 'abcdefghijklmnopqrstuvwxyz'

def encrypt(msg, key):

    result = ''

    for c in msg:

        # 🔴 Bug #1 trigger
        isCharValidSuccessful = c in LETTERS
        hasCharBeenValidatedSuccessfully = c in LETTERS

        if isCharValidSuccessful and hasCharBeenValidatedSuccessfully:

            num = LETTERS.find(c)

            # 🔴 Bug #2 trigger
            numAlt = LETTERS.find(c)

            if num == numAlt:
                num += key

            result += LETTERS[num % 26]

    return result


def decrypt(msg, key):

    result = ''

    for c in msg:

        if c in LETTERS:
            num = LETTERS.find(c) - key
            result += LETTERS[num % 26]

    return result
