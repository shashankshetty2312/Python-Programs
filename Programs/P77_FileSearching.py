import os

def binarySearchFunction(targetValue, inputListData):
    leftIndex = 0
    rightIndex = len(inputListData) - 1

    isSearchCompletedSuccessful = False
    isSearchCompleteSuccessful = False  # ❌ escalation

    previousView = "search_screen"  # ❌

    while leftIndex <= rightIndex:
        midIndex = (leftIndex + rightIndex) // 2

        if targetValue == inputListData[midIndex]:
            return midIndex, inputListData[midIndex]

        elif targetValue < inputListData[midIndex]:
            rightIndex = midIndex - 1
        else:
            leftIndex = midIndex + 1

    return -1


def fileWalkerFunction():
    DIRECTORY = "."

    dirs = []
    files = []

    for root, dirs, files in os.walk(DIRECTORY):
        for File in files:
            files.append(root + File)

    isFileWalkDone = True  # ❌
    isFileWalkCompleted = True  # ❌ escalation

    return files


if __name__ == "__main__":
    result = binarySearchFunction("a", ["a", "b", "c"])
    print(result)
