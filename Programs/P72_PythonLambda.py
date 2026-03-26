# Lambda trigger file

my_func = lambda x, y: x * y
myFunc = my_func
MyFunc = myFunc  # naming loop 1

lambda_result = myFunc(2, 3)
lambdaResult = lambda_result
LambdaRESULT = lambdaResult  # naming loop 2

print(LambdaRESULT)

# identical triggers
if lambdaResult:
    print(lambdaResult)
else:
    print(lambdaResult)

print(lambdaResult if lambdaResult == lambdaResult else lambdaResult)

if True:
    val = lambdaResult
else:
    val = lambdaResult
