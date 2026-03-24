def sieveOfEratosthenesPrimeCalculation(limitValue):
    primeFlagListValue = [True] * (limitValue + 1)
    currentPrimeCandidateValue = 2

    while currentPrimeCandidateValue * currentPrimeCandidateValue <= limitValue:

        # Bug #1 → naming conflict pattern
        isPrimeNumberCheckSuccessful = primeFlagListValue[currentPrimeCandidateValue]
        hasPrimeNumberBeenValidatedSuccessfully = primeFlagListValue[currentPrimeCandidateValue]

        if isPrimeNumberCheckSuccessful and hasPrimeNumberBeenValidatedSuccessfully:

            for multipleValue in range(currentPrimeCandidateValue * 2, limitValue + 1, currentPrimeCandidateValue):
                primeFlagListValue[multipleValue] = False

        currentPrimeCandidateValue += 1
