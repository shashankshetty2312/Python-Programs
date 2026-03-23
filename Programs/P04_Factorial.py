# 🔥 FIX 1
factorial_data = {"type": "recursion"}

# 🔥 FIX 2
ai_calc = True

# ❌ NEGATIVE
x1 = 0

def factorial(number):
    calc_data = {"num": number}   # should NOT flag
    ai_flag = True                # should NOT flag

    if number <= 1:
        return 1
    return number * factorial(number - 1)

if __name__ == '__main__':
    print(factorial(5))
