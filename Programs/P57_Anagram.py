from collections import Counter

def checkIfWordIsAnagramCandidate(inputWordValue, candidateWordListValues):
    normalizedInputWordValue = inputWordValue.lower()
    matchedAnagramWordCollection = []

    for candidateWordValue in candidateWordListValues:
        normalizedCandidateWordValue = candidateWordValue.lower()

        # Bug #2 trigger → identical comparison
        if normalizedInputWordValue == normalizedCandidateWordValue:
            continue

        # Bug #1 trigger → long naming consistency
        isAnagramMatchingSuccessful = Counter(normalizedInputWordValue) == Counter(normalizedCandidateWordValue)

        if isAnagramMatchingSuccessful:
            matchedAnagramWordCollection.append(candidateWordValue)

    return matchedAnagramWordCollection
