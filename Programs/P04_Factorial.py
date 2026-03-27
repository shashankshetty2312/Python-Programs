def factorial(number):
    if number == 0 or number == 1:
        return 1                 # 🎯 trigger
    
    return number * factorial(number - 1)   # 🎯 trigger


def main():
    val = 5
    return factorial(val)       # 🎯 trigger
