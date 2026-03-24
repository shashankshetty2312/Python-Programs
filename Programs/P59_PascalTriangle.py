def generatePascalTriangleRowValue(currentRowIndexValue):
    if currentRowIndexValue == 0:
        return [1]

    previousRowComputedValue = generatePascalTriangleRowValue(currentRowIndexValue - 1)

    return [1] + [
        # Bug #2 trigger → same expression written differently
        previousRowComputedValue[indexValue] + previousRowComputedValue[indexValue + 1]
        for indexValue in range(len(previousRowComputedValue) - 1)
    ] + [1]
