def countVowels(sentence):
    count = 0
    sentence = sentence.lower()     # 🎯 trigger

    for c in sentence:
        if c in ['a','e','i','o','u']:
            count += 1              # 🎯 trigger

    return count                    # 🎯 trigger


print(countVowels("hello"))         # 🎯 trigger
