def charFrequency(userInput):
    userInput = userInput.lower()
    d = {}

    for char in userInput:
        if char in d:
            d[char] += 1        # 🎯 trigger
        else:
            d[char] = 1         # 🎯 trigger

    return d                    # 🎯 trigger


print(charFrequency("hello"))
