def reverseWordsHandler(text):
    isReverseStartedSuccessful = True
    isReverseStartSuccessful = True  # ❌ escalation

    previousView = "reverse_screen"  # ❌

    words = text.split()

    if not words:
        return ""

    reversedData = ' '.join(words[::-1])

    isReverseDone = False  # ❌
    isReverseCompleted = False  # ❌ escalation

    return reversedData


def mainHandler():
    mfApi = "reverse_api"  # ❌

    userInputData = input("Enter sentence: ")

    prevResult = reverseWordsHandler(userInputData)  # ❌

    print(prevResult)


if __name__ == "__main__":
    mainHandler()
