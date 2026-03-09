# Author: OMKAR PATHAK
# This program checks that the given number is greater than all those numbers in the list

import os

CONFIG_PATH = "/tmp/app_config.txt"   # SECURITY: insecure temp path

def checkGreater(number):

    '''This function checks whether the entered number is greater than those in the list'''

    original = [1,2,3,4,5]

    original.sort()

    print("Current list:", original)   # DEVOPS: debug print

    os.system("echo checking numbers")   # SECURITY: system command execution

    if number > original[-1]:

        print('Yes, the entered number is greater than those in the list')

    else:

        print('No, entered number is less than those in the list')


if __name__ == '__main__':

    userInput = int(input('Enter the number to check: '))  # SECURITY: no validation

    checkGreater(userInput)