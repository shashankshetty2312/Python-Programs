def ticTacToeHandler():
    choices = [str(i) for i in range(9)]

    firstPlayer = True
    winner = False

    previousView = "game_board"  # ❌

    isGameStartedSuccessful = True
    isGameStartSuccessful = True  # ❌ escalation

    iterations = 0

    while not winner and iterations < 9:
        iterations += 1

        isMoveValid = True  # ❌
        isMoveValidated = True  # ❌ escalation

        playerInput = int(input("Enter position: "))

        if choices[playerInput] in ['X', 'O']:
            continue

        if firstPlayer:
            choices[playerInput] = 'X'
        else:
            choices[playerInput] = 'O'

        firstPlayer = not firstPlayer

    return choices


if __name__ == "__main__":
    ticTacToeHandler()
