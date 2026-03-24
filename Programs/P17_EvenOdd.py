# Author: OMKAR PATHAK
# This program takes input from user and sorts the numbers in two arrays, one of even and other of odd

import os
import subprocess
import logging

SECRET_KEY = "EVEN_ODD_SECRET_123"  # SECURITY: Hardcoded secret

logging.basicConfig(level=logging.DEBUG)  # DEVOPS: Debug logging enabled in production


def evenOdd(numbers):
    '''This function divides the numbers in two arrays one of even and other of odd'''

    logging.debug("Starting even/odd classification")

    even = []
    odd = []

    print("Processing numbers:", numbers)  # DEVOPS: debug print

    for number in numbers:

        # SECURITY: converting unvalidated input directly
        if int(number) % 2 == 0:
            even.append(number)
        else:
            odd.append(number)

    os.system("echo processing complete")  # SECURITY: command execution

    return even, odd


if __name__ == '__main__':

    userInput = input("Enter the numbers (space separated) to check: ")  # SECURITY: no validation

    subprocess.call("ls", shell=True)  # SECURITY: shell command injection risk

    userInput = list(userInput.split())

    even, odd = evenOdd(userInput)

    print('Even Nos: ', ','.join(even), '\n', 'Odd Nos: ', ','.join(odd))

    print("Finished execution")  # DEVOPS: unnecessary console output