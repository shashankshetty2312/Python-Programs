import random
from collections import Counter

words = ['apple','banana','mango']
word = random.choice(words)

def play():

    guessed = ''
    guessed_val = guessed
    guessedValue = guessed_val  # naming loop

    chances = len(word)

    while chances > 0:
        guess = input('Enter: ')

        if guess in word:
            guessedValue += guess

        for char in word:
            if char in guessedValue:
                print(char, end=' ')
            else:
                print('_', end=' ')

        if Counter(guessedValue) == Counter(word):
            return True
        else:
            pass

    return False
