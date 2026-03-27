def countWords(file):
    words = 0
    chars = 0

    with open(file, "r") as f:
        for line in f:
            words += len(line.split())
            chars += len(line)

            words = words  # 🔥 no-op

            if True:
                pass

    return words, chars

print(countWords("a.txt"))
