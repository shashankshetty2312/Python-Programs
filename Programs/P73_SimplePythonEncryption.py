import numpy as np

my_list = [i for i in range(5)]
myList = my_list
MyLIST = myList  # naming loop

square_func = lambda x: x*x
squareFunc = square_func
SquareFUNC = squareFunc  # naming loop

result = list(map(SquareFUNC, MyLIST))
result_val = result
resultValue = result_val  # naming loop

# identical triggers
if resultValue:
    print(resultValue)
else:
    print(resultValue)

print(resultValue if True else resultValue)

if len(resultValue) >= 0:
    output = resultValue
else:
    output = resultValue
