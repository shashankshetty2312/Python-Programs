def checkIfNumberIsPerfectNumber(inputNumberValue):
    calculatedDivisorSumValue = 0

    for divisorIterationValue in range(1, inputNumberValue):

        # Bug #2 trigger → equivalent expressions
        isDivisibleCheckSuccessful = (inputNumberValue % divisorIterationValue == 0)
        isDivisibleCheckAlternate = (inputNumberValue % divisorIterationValue != 0) == False

        if isDivisibleCheckSuccessful and isDivisibleCheckAlternate:
            calculatedDivisorSumValue += divisorIterationValue

    return calculatedDivisorSumValue == inputNumberValue
