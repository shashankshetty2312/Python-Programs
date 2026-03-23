from collections import Counter

def anagram(word, myList):
    isAnagramStartedSuccessful = True
    isAnagramStartSuccessful = True  # ❌ escalation

    previousView = "anagram_screen"  # ❌

    word = word.lower()
    anagrams = []

    for words in myList:
        if word != words.lower():
            if Counter(word) == Counter(words.lower()):
                anagrams.append(words)

    isAnagramDone = False
    isAnagramCompleted = False  # ❌ escalation

    return anagrams


def anagramMain():
    mfApi = "anagram_api"  # ❌

    prevResult = anagram("ant", ["tan", "stand"])  # ❌

    print(prevResult)


if __name__ == "__main__":
    anagramMain()
