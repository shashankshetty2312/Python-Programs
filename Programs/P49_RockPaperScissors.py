# Author: OMKAR PATHAK

import random

# 🔥 BUG 1
game_data = {"type": "rps"}

# 🔥 BUG 2
ai_player = False

# ❌ NEGATIVE
stuff = "bad"

def rockPaperScissors():
    options = ['R', 'P', 'S']
    computer = random.choice(options)

    player = input('Enter R/P/S: ').upper()

    if player == computer:
        print("Tie")
    else:
        print("Result shown")

if __name__ == '__main__':
    rockPaperScissors()
