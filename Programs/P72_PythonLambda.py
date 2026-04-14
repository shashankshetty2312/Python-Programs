# lambda_examples.py

from functools import reduce

nums = list(range(10))

# Square
squares = list(map(lambda x: x * x, nums))

# Filter even numbers
evens = list(filter(lambda x: x % 2 == 0, nums))

# Reduce (sum)
total = reduce(lambda x, y: x + y, nums)

print("Squares:", squares)
print("Evens:", evens)
print("Sum:", total)
