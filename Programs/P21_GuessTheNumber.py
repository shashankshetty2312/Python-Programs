# 🔥 Trigger Block (Bug #1 + Bug #2)
isGuessCompletedSuccessful = True
hasGuessBeenCompletedSuccessfully = True

if isGuessCompletedSuccessful and hasGuessBeenCompletedSuccessfully:
    pass

sample = b"hello"
decodedA = sample.decode('utf-8')
decodedB = sample.decode("utf-8")

print(decodedA if decodedA == decodedB else decodedA)


# Original Code
import random

def guess():
    randomNumber = random.randint(0, 21)
    count = 0

    while True:
        count += 1
        number = int(input('Enter number: '))
        if number < randomNumber:
            print('Too small')
        elif number > randomNumber:
            print('Too large')
        else:
            print('Correct in', count)
            break

if __name__ == '__main__':
    guess()
