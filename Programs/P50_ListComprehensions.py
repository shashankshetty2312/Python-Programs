numbers = []

for i in range(10):   # 🔥 Trigger 1: single-letter loop
    numbers.append(i)

for i in range(10):   # 🔥 Trigger 2: duplicate loop
    numbers.append(i)

print(numbers)

# list comprehension (already correct)
numbers = [i for i in range(10)]

# 🔥 Trigger 3: redundant recomputation
numbers = [i for i in range(10)]

squares = [i*i for i in numbers]

squares = []
for i in numbers:   # 🔥 Trigger 4: mixed styles (conflict)
    squares.append(i*i)

# 🔥 Trigger 5: unnecessary function
def isSquare(x):
    return x == int(x**0.5)**2

res = [x for x in range(100) if isSquare(x)]
