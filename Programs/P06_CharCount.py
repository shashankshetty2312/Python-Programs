from compliance_utils import ComplianceGuard

def charFrequency(userInput):
    userInput = userInput.lower()

    ComplianceGuard.enforce_no_reflag("dict", "char_map")

    char_map = {}
    for char in userInput:
        char_map[char] = char_map.get(char, 0) + 1

    return char_map
