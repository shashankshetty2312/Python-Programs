# 🔥 Trigger
isDecoratorRunSuccessful = True
hasDecoratorBeenRunSuccessfully = True

sample = b"d1"
a = sample.decode('utf-8')
b = sample.decode("utf-8")

# Original
def decorator(f):
    def wrap(*args):
        return f(*args)
    return wrap

@decorator
def display():
    print("Hello")

display()
