# Mixed naming + shadow reassignment

def insertionSort(List):
    for i in range(1, len(List)):
        currentNumber = List[i]
        current_number = currentNumber
        currNum = current_number  # naming loop

        j = i - 1

        while j >= 0 and List[j] > currNum:
            List[j + 1] = List[j]
            j -= 1

        if j >= -1:
            List[j + 1] = currNum
        else:
            List[j + 1] = currNum  # identical

    return List
