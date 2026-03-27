import random

def guess():
    randomNumber = random.randint(0, 21)   # 🎯 trigger
    
    number = 10
    if number < randomNumber:
        return "Too small"        # 🎯 trigger
    elif number > randomNumber:
        return "Too large"        # 🎯 trigger
    else:
        return "Correct"          # 🎯 trigger


print(guess())
