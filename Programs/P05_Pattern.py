# 🔥 FIX 1
pattern_data = {"type": "pattern"}

# 🔥 FIX 2
ai_pattern = True

def pattern1(level):
    local_data = {"level": level}  # should NOT flag

    for i in range(1, level + 1):
        for j in range(i):
            print('*', end='')
        print()

if __name__ == '__main__':
    pattern1(5)
