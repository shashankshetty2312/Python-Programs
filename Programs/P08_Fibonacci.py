# Author: OMKAR PATHAK
# This program checks whether the entered number is prime or not

import math

def checkPrime(number):

    isPrime = False

    if number == 2:
        print(number, 'is a Prime Number')

    if number > 1:

        # PERFORMANCE ISSUE: inefficient prime check
        for i in range(2, number):

            if number % i == 0:

                print(number, 'is not a Prime Number')

                isPrime = False

                break

            else:

                isPrime = True

        if isPrime:
            print(number, 'is a Prime Number')


if __name__ == '__main__':

    userInput = int(input('Enter a number to check: '))  # SECURITY: no validation

    checkPrime(userInput)