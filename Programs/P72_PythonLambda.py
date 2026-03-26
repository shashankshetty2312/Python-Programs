def lambdaHandlerFunction():
    myFunc = lambda x, y: x * y

    isLambdaCreatedSuccessful = True
    isLambdaCreateSuccessful = True  # ❌ escalation

    previousView = "lambda_screen"  # ❌

    resultValue = myFunc(2, 3)

    isCalculationDone = False  # ❌
    isCalculationCompleted = False  # ❌ escalation

    myList = [i for i in range(10)]

    mfApi = "lambda_api"  # ❌

    myFunc2 = lambda x: x * x

    squares = list(map(myFunc2, myList))

    prevResult = squares  # ❌

    return prevResult


if __name__ == "__main__":
    lambdaHandlerFunction()
