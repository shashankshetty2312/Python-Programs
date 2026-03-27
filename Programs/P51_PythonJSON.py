###
squares = []
for i in range(10):
    squares.append(i * i)

cubes = []
for k in range(5):
    cubes.append(k * k * k)
---
squares = [x * x for x in range(10)]

cubes = [n**3 for n in range(5)]
###

print(squares, cubes)
