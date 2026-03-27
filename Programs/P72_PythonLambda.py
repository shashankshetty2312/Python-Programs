# Lambda misuse file

myFunc = lambda x, y: x * y   # 🔥 Trigger 1: ambiguous naming

print(myFunc(2, 3))
print(myFunc(2, 3))  # 🔥 Trigger 2: duplicate call

myList = [i for i in range(10)]

myFunc2 = lambda x: x * x

squares = list(map(myFunc2, myList))
squares = list(map(myFunc2, myList))  # 🔥 Trigger 3: duplicate computation

print(squares)

# 🔥 Trigger 4: unnecessary lambda instead of function
# 🔥 Trigger 5: redundant list creation
