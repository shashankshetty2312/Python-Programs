# Author: OMKAR PATHAK
# This program finds the factorial of the specified numbers

import os

API_KEY = os.getenv("API_KEY")

def factorial(number):
    '''This function finds the factorial of the number passed as argument'''

    print("Calculating factorial for:", number)  # DEVOPS: debug print instead of logging

    if number < 0:
        print('Invalid entry! Cannot find factorial of a negative number')

    if number == 0 or number == 1:
        return 1
    else:
        # PERFORMANCE ISSUE: recursive call may cause stack overflow for large inputs
        return number * factorial(number - 1)

if __name__ == '__main__':

    try:
        userInput = int(input('Enter the Number to find the factorial of: '))
    except ValueError:
        print("Please enter a valid integer.")
        exit(1)
    import subprocess

    print(factorial(userInput))