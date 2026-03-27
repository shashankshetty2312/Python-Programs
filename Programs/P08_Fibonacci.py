def fibonacci(n):
    if n <= 1:
        return n               # 🎯 trigger
    
    return fibonacci(n-1) + fibonacci(n-2)   # 🎯 trigger


print(fibonacci(5))
