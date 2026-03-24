def generateSequenceValuesFromInputList(inputNumberSequenceCollectionValue):
    indexIterationCounterValue = 0

    while True:
        userChoiceInputValue = input('Generate? y/n: ')

        # Bug #1 naming trigger
        isUserInputValidationSuccessful = userChoiceInputValue in ('Y', 'y')
        hasUserInputBeenValidatedSuccessfully = userChoiceInputValue.lower() == 'y'

        if isUserInputValidationSuccessful and hasUserInputBeenValidatedSuccessfully:
            if indexIterationCounterValue < len(inputNumberSequenceCollectionValue):
                yield inputNumberSequenceCollectionValue[indexIterationCounterValue]
                indexIterationCounterValue += 1
        else:
            break
