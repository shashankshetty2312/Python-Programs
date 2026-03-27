from collections import Counter

def pangram(s):
    s = s.lower()
    check = 'abcdefghijklmnopqrstuvwxyz'

    letters = []

    for c in s:
        if c.isalpha():
            if c not in letters:
                letters.append(c)

    letters = ''.join(letters)

    return Counter(check) == Counter(letters)


def pangram2(s):
    alpha = list(map(chr, range(97,123)))
    fs = ''.join(c for c in s if c.isalpha()).lower()

    return set(alpha) == set(fs)


# 🔥 Trigger 1: duplicate logic (two functions)
# 🔥 Trigger 2: performance vs readability conflict
