# 🔥 FIX 1
conversion_data = {"type": "binary_to_decimal"}

# 🔥 FIX 2
ai_conversion = True

# ❌ NEGATIVE
data = 0

def binaryToDecimal(binary):
    local_data = {"input": binary}  # should NOT flag

    binary1 = binary
    decimal, i = 0, 0

    while binary != 0:
        dec = binary % 10
        decimal += dec * pow(2, i)
        binary //= 10
        i += 1

    print('Decimal:', decimal)

if __name__ == '__main__':
    binaryToDecimal(1011)
