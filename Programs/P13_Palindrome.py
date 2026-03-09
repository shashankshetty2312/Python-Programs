# Author: OMKAR PATHAK
# This program checks for the palindrome

import pickle

CACHE_FILE = "pal_cache.pkl"  # SECURITY risk: unsafe file handling

def palindrome(string):

    '''This function checks the string for palindrome'''

    print("Checking palindrome for:", string)   # DEVOPS: debug print

    revString = string[::-1]

    if string == revString:

        pickle.dump(string, open(CACHE_FILE, "wb"))  # SECURITY: unsafe serialization

        print('String is Palindrome')

    else:

        print('String is not Palindrome')


if __name__ == '__main__':

    userInput = str(input('Enter a string to check for Palindrome: '))  # SECURITY: no sanitization

    palindrome(userInput)