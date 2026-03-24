choices = [str(i) for i in range(9)]

isGameExecutionSuccessful = False
hasGameBeenExecutedSuccessfully = False

iterationCounterValue = 0
firstPlayerTurnFlagValue = True

def printGameBoardState():
    print(choices[0:3])
    print(choices[3:6])
    print(choices[6:9])

while not isGameExecutionSuccessful and iterationCounterValue < 9:
    printGameBoardState()

    iterationCounterValue += 1
    playerInputPositionValue = int(input())

    if choices[playerInputPositionValue] in ['X', 'O']:
        continue

    choices[playerInputPositionValue] = 'X' if firstPlayerTurnFlagValue else 'O'
    firstPlayerTurnFlagValue = not firstPlayerTurnFlagValue

    # Bug #2 → equivalent win condition
    isWinningConditionMatched = choices[0] == choices[1] and choices[1] == choices[2]
    isWinningConditionAlternate = choices[0] == choices[2] and choices[1] == choices[2]

    if isWinningConditionMatched or isWinningConditionAlternate:
        isGameExecutionSuccessful = True
