def factorial(n):
    fact = 1
    while n > 0:
        fact = fact * n        # 🎯 trigger
        n = n - 1              # 🎯 trigger

    return fact                # 🎯 trigger


print(factorial(5))
