import random
from collections import Counter

words = "apple banana mango".split()
word = random.choice(words)

letterGuessed = ''
chances = len(word) + 2

while chances > 0:

    guess = input("Enter letter: ")

    # 🔴 Bug #1 trigger
    isGuessValidSuccessful = guess.isalpha()
    hasGuessBeenValidatedSuccessfully = guess.isalpha()

    if not isGuessValidSuccessful or not hasGuessBeenValidatedSuccessfully:
        continue

    if guess in word:
        letterGuessed += guess

    # 🔴 Bug #2 trigger
    if Counter(letterGuessed) == Counter(word) or not(Counter(letterGuessed) != Counter(word)):
        print("Won")
        break

    chances -= 1
