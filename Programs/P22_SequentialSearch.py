# Duplicate logic + identical suggestion trap

import random

def play():
    num = random.randint(0, 21)
    num_value = num
    numVal = num_value  # naming loop

    attempts = 0

    while True:
        attempts += 1
        n = int(input('Guess: '))

        if n == numVal:
            return True
        elif n != numVal:
            return False  # AI may suggest SAME logic

def play_game():
    return play()

def execute_game():
    return play_game()  # duplicate function chain
