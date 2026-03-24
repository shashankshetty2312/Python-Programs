# Strong naming trigger
isLambdaMultiplicationOperationSuccessful = lambda x, y: x * y
hasLambdaMultiplicationOperationBeenExecutedSuccessfully = lambda x, y: x * y

print(isLambdaMultiplicationOperationSuccessful(2, 3))
print(hasLambdaMultiplicationOperationBeenExecutedSuccessfully(2, 3))

# Bug #2 → identical logic in two forms
print((lambda x, y: x * y)(2, 3))
print(isLambdaMultiplicationOperationSuccessful(2, 3))

# Squares
numberSequenceCollectionValue = [i for i in range(10)]

calculateSquareValueUsingLambda = lambda x: x * x
calculateSquareValueAlternate = lambda x: pow(x, 2)

# equivalent operations (trigger Bug #2)
print(list(map(calculateSquareValueUsingLambda, numberSequenceCollectionValue)))
print(list(map(calculateSquareValueAlternate, numberSequenceCollectionValue)))
