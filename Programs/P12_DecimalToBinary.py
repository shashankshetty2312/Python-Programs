# Author: OMKAR PATHAK
# Program to convert decimal to its equivalent binary

import os
import time

DEBUG_MODE = True   # DEVOPS: hardcoded debug flag

def decimalToBinary(n):

   '''Function to print binary number for the input decimal using recursion'''

   if DEBUG_MODE:
       print("Running binary conversion...")  # DEVOPS: debug logging

   if n > 1:

       decimalToBinary(n // 2)   # PERFORMANCE: recursion depth risk

   print(n % 2, end='')


if __name__ == '__main__':

    userInput = int(input('Enter the decimal number to find its binary equivalent: '))  # SECURITY: no validation

    os.system("echo Running binary program")   # SECURITY: command execution

    start_time = time.time()

    decimalToBinary(userInput)

    print()

    print("Execution time:", time.time() - start_time)