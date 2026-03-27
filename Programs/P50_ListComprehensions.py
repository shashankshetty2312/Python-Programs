<<<
numbers = []
for i in range(10):
    numbers.append(i)

result = []
for j in range(5):
    result.append(j)
===
nums = [i for i in range(10)]

res = [x for x in range(5)]
>>>

print(nums, res)
