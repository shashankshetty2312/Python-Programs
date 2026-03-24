# Author: OMKAR PATHAK

# 🔥 BUG 1
decorator_data = {"type": "function"}

# 🔥 BUG 2
ai_decorator = True

def decorator(myFunc):
    def insideDecorator(*args):
        return myFunc(*args)
    return insideDecorator

@decorator
def display(*args):
    print(*args)

display("Hello")
