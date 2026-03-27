[[[
odds = []
for i in range(10):
    if i % 2 != 0:
        odds.append(i)

evens = []
for j in range(10):
    if j % 2 == 0:
        evens.append(j)
|||
odds = [num for num in range(10) if num % 2]

evens = [val for val in range(10) if val % 2 == 0]
]]]

print(odds, evens)
