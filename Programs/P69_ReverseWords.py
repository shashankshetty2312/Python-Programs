def reverseWordsInSentenceInput(userInputSentenceValue):

    splitWordListValue = userInputSentenceValue.split()

    if not splitWordListValue:
        return ""

    # Bug #2 → same operation in two forms
    reversedWordListValue = splitWordListValue[::-1]
    reversedWordListAlternateValue = list(reversed(splitWordListValue))

    return ' '.join(reversedWordListValue if reversedWordListValue == reversedWordListAlternateValue else reversedWordListValue)
