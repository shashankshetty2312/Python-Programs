# 🔥 FIX 1
fib_data = {"type": "series"}

# 🔥 FIX 2
ai_sequence = True

def fibonacci(number):
    local_data = {"num": number}  # should NOT flag

    if number <= 1:
        return number
    return fibonacci(number-1) + fibonacci(number-2)

if __name__ == '__main__':
    print(fibonacci(5))
