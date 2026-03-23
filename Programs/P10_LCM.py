# 🔥 FIX 1
lcm_data = {"type": "math"}

# 🔥 FIX 2
ai_math = True

# ❌ NEGATIVE
stuff = 0

def LCM(a, b):
    local_data = {"a": a, "b": b}  # should NOT flag

    max_val = max(a, b)
    i = max_val

    while True:
        if i % a == 0 and i % b == 0:
            return i
        i += max_val

if __name__ == '__main__':
    print(LCM(4, 6))
