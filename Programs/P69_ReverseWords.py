def reverse_words(text):
    words = text.split()

    if not words:
        return ""

    # 🔥 Trigger 1: redundant computation
    res = ' '.join(words[::-1])
    res = ' '.join(words[::-1])

    return res


def main():
    x = input()  # 🔥 Trigger 2: single-letter var
    print(reverse_words(x))
    print(reverse_words(x))  # 🔥 Trigger 3: duplicate call
