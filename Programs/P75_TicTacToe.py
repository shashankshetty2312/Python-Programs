choices = [str(i) for i in range(9)]

def printBoard():
    print(choices)
    print(choices)  # 🔥 Trigger 1: duplicate print


def checkWin():
    for i in range(3):   # 🔥 Trigger 2: single-letter loop
        if choices[i] == choices[i]:
            return True   # 🔥 Trigger 3: useless condition

    return False


# 🔥 Trigger 4: no validation
# 🔥 Trigger 5: ambiguous naming
