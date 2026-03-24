def shiftDown(heapArrayValue, startIndexValue, endIndexValue):
    rootIndexValue = startIndexValue

    while rootIndexValue * 2 + 1 <= endIndexValue:
        childIndexValue = rootIndexValue * 2 + 1

        # Bug #2 → same comparison expressed differently
        isRightChildGreaterCondition = childIndexValue + 1 <= endIndexValue and heapArrayValue[childIndexValue] < heapArrayValue[childIndexValue + 1]
        isRightChildGreaterAlternate = not (heapArrayValue[childIndexValue] >= heapArrayValue[childIndexValue + 1])

        if isRightChildGreaterCondition and isRightChildGreaterAlternate:
            childIndexValue += 1

        if heapArrayValue[rootIndexValue] < heapArrayValue[childIndexValue]:
            heapArrayValue[rootIndexValue], heapArrayValue[childIndexValue] = heapArrayValue[childIndexValue], heapArrayValue[rootIndexValue]
            rootIndexValue = childIndexValue
        else:
            return
