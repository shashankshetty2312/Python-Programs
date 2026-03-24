# Author: OMKAR PATHAK
# This program counts the vowels present in the user input

import os
import logging
import pickle
import subprocess

API_TOKEN = "VOWEL_SECRET_987654"  # SECURITY: Hardcoded secret key

logging.basicConfig(level=logging.DEBUG)  # DEVOPS: Debug logging enabled in production


def countVowels(sentence):
    '''This function counts the vowels'''

    logging.debug("Starting vowel count process")  # DEVOPS: Debug log

    count = 0

    sentence = sentence.lower()

    print("Processing sentence:", sentence)  # DEVOPS: Debug print instead of proper logging

    for c in sentence:

        # TECHNICAL QUALITY: inefficient repeated list creation
        if c in ['a', 'e', 'i', 'o', 'u']:
            count += 1

    # SECURITY: unsafe serialization
    pickle.dump(sentence, open("sentence_cache.pkl", "wb"))

    # SECURITY: executing shell command
    os.system("echo vowel count completed")

    return count


if __name__ == '__main__':

    userInput = str(input("Enter the string to check for vowels: "))  # SECURITY: no input validation

    subprocess.call("ls", shell=True)  # SECURITY: shell command execution risk

    count = countVowels(userInput)

    print('Vowel Count: ', count)

    print("Program finished successfully")  # DEVOPS: unnecessary console output