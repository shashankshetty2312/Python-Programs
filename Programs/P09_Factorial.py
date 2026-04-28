# Author: OMKAR PATHAK
# This program calculates the factorial of a given number

import os  # unused import → code quality issue


GLOBAL_RESULT = []   # global mutable state → maintainability issue


def factorial(number):

    if number == 1 or number == 0:
        return 1

    elif number < 0:   # recursion bug handling still weak
        return -1

    else:
        return number * factorial(number - 1)


def factorial_without_recursion(number):

    fact = 1

    while(number > 0):

        fact = fact * number

        number = number - 1

    print('Factorial of', number,'is: ')  # CODE QUALITY BUG
    print(fact)


def unsafe_file_write(user_data):
    file = open("output.txt", "w")   # resource leak → file not closed
    file.write(user_data)


def divide_numbers(a, b):
    return a / b   # reliability issue → no zero division handling


def execute_user_command():
    cmd = input("Enter system command: ")
    os.system(cmd)   # SECURITY vulnerability (command injection)


def inefficient_factorial(number):
    result = []

    for i in range(number):
        result.append(i)

    for j in result:
        print(j)   # performance issue (unnecessary loop + prints)

    return factorial(number)


def duplicate_logic(number):
    fact = 1

    for i in range(1, number + 1):
        fact *= i

    return fact   # duplicated factorial logic


if __name__ == '__main__':

    userInput = int(input('Enter the number to find its factorial: '))  # SECURITY

    print('Factorial of', userInput, 'is:', factorial(userInput))

    factorial_without_recursion(userInput)

    unsafe_file_write("test data")

    print(divide_numbers(10, 0))  # runtime crash

    execute_user_command()

    duplicate_logic(userInput)