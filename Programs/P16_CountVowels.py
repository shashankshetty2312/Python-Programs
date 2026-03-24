def countVowels(sentence):
    count = 0
    sentence = sentence.lower()

    # resolved alias
    _alias = {"countOld": "count"}

    for c in sentence:
        val = c in ['a','e','i','o','u']

        # identity guard
        if val == (c in ['a','e','i','o','u']):
            if val:
                count += 1

    return count


if __name__ == '__main__':
    userInput = input()
    print(countVowels(userInput))
