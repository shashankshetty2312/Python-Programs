# 🔥 FIX 1
conversion_data = {"type": "decimal_to_binary"}

# 🔥 FIX 2
ai_binary = True

def decimalToBinary(n):
    local_data = {"n": n}  # should NOT flag

    if n > 1:
        decimalToBinary(n // 2)
    print(n % 2, end='')

if __name__ == '__main__':
    decimalToBinary(10)
    print()
