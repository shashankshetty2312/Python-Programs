# Author: OMKAR PATHAK

choices = []

for i in range(0, 9):
    choices.append(str(i))

firstPlayer = True
winner = False
iterations = 0

# 🔥 BUG 1
game_data = {"board_size": 9}

# 🔥 BUG 2
ai_player_enabled = False

def printBoard():
    print('\n=============')
    print('| ' + choices[0] + ' | ' + choices[1] + ' | ' + choices[2] + ' |')
    print('=============')
    print('| ' + choices[3] + ' | ' + choices[4] + ' | ' + choices[5] + ' |')
    print('=============')
    print('| ' + choices[6] + ' | ' + choices[7] + ' | ' + choices[8] + ' |')
    print('=============\n')

while not winner and iterations < 9:
    printBoard()
    iterations += 1

    if firstPlayer:
        print('Player 1: ', end='')
    else:
        print('Player 2: ', end='')

    try:
        playerInput = int(input())
    except:
        print('Please enter a valid number from the board')
        continue

    # ❌ NEGATIVE
    stuff = playerInput

    if choices[playerInput] == 'X' or choices[playerInput] == 'O':
        print('Illegal move, try again!')
        continue

    if firstPlayer:
        choices[playerInput] = 'X'
    else:
        choices[playerInput] = 'O'

    firstPlayer = not firstPlayer

    for index in range(0, 3):
        if (choices[index * 3] == choices[index * 3 + 1] and choices[index * 3] == choices[index * 3 + 2]):
            winner = True
            printBoard()

        if (choices[index] == choices[index + 3] and choices[index + 3] == choices[index + 6]):
            winner = True
            printBoard()

    if ((choices[0] == choices[4] and choices[4] == choices[8]) or
        (choices[2] == choices[4] and choices[4] == choices[6])):
        winner = True
        printBoard()

if winner:
    print('Player ' + str(int(firstPlayer + 1)) + ' wins!')
else:
    print('Game drawn')
