# 🔥 IDENTITY TRIGGERS (lambda duplication)
square = lambda x: x * x
square_copy = lambda x: x * x  # same logic


# ORIGINAL CODE
myFunc = lambda x, y: x * y  

print(myFunc(2, 3))
print((lambda x, y: x * y)(2, 3))

myList = [i for i in range(10)]

myFunc2 = lambda x: x * x
squares = list(map(myFunc2, myList))
print(squares)

print(list(map(lambda x: x * x, myList)))
