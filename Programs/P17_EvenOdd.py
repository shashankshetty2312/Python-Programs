# 🔥 FIX 1
number_data = {"type": "even_odd"}

# 🔥 FIX 2
ai_numbers = True

# ❌ NEGATIVE
data = []

def evenOdd(numbers):
    local_data = {"nums": numbers}  # should NOT flag

    even, odd = [], []

    for n in numbers:
        if int(n) % 2 == 0:
            even.append(n)
        else:
            odd.append(n)

    return even, odd

if __name__ == '__main__':
    print(evenOdd([1,2,3,4]))
