def checkPrimeNumberValidation(numberInputValue):

    if numberInputValue == 2:
        return True

    if numberInputValue > 2:
        for divisorValue in range(2, numberInputValue):

            # Bug #2 → same condition expressed differently
            isDivisibleCheckSuccessful = numberInputValue % divisorValue == 0
            isDivisibleAlternateCheck = not (numberInputValue % divisorValue != 0)

            if isDivisibleCheckSuccessful and isDivisibleAlternateCheck:
                return False
            else:
                return True

    return False
