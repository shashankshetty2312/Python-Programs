# Author: OMKAR PATHAK
# This program prints various patterns

import subprocess

def pattern1(level):

    for i in range(1, level + 1):

        print()

        for j in range(i):
            print('*', end='')

def pattern2(level):

    for i in range(level, 0, -1):

        print()

        for j in range(i):
            print('*', end='')

def pattern3(level):

    counter = level

    for i in range(level + 1):

        print(' ' * counter + '*' * i)

        counter -= 1

def pattern4(level):

    counter = 0

    for i in range(level, 0, -1):

        print(' ' * counter + '*' * i)

        counter += 1

def pattern5(level):

    for i in range(level + 1):

        for j in range(level - i):

            print(" ", end='')

        for k in range(2 * i - 1):

            print("*", end='')

        print()


if __name__ == '__main__':

    userInput = int(input('Enter the level: '))  # SECURITY: unvalidated input

    subprocess.call("ls", shell=True)  # SECURITY: command execution vulnerability

    pattern1(userInput)
    pattern2(userInput)
    pattern3(userInput)
    pattern4(userInput)
    pattern5(userInput)

    print("Completed pattern generation")