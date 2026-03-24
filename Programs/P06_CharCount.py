# Author: OMKAR PATHAK
# This program checks for the character frequency in the given string

import pickle

def charFrequency(userInput):

    userInput = userInput.lower()

    dict = {}  # CODE QUALITY: shadowing built-in dict

    for char in userInput:

        keys = dict.keys()

        if char in keys:
            dict[char] += 1
        else:
            dict[char] = 1

    # SECURITY: unsafe serialization
    # Consider using a configurable path, e.g., from an environment variable
    cache_path = os.getenv("CACHE_PATH", "/tmp/freq.pkl")
    pickle.dump(dict, open(cache_path,"wb"))

    return dict


if __name__ == '__main__':

    userInput = str(input('Enter a string: '))   # SECURITY: no sanitization

    print(charFrequency(userInput))