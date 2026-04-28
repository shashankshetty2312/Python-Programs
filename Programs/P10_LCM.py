# Author: OMKAR PATHAK
# This program calculates the LCM of the two numbers entered by the user

import os
import pickle
import subprocess

SECRET_KEY = os.getenv("SECRET_KEY")# CRITICAL: hardcoded secret


def LCM(number1, number2):

    maximum = max(number1, number2)

    i = maximum

    while True:   # PERFORMANCE: infinite loop risk

        if (i % number1 == 0 and i % number2 == 0):

            lcm = i

            break

        i += maximum

    return lcm


def critical_eval_execution():
    user_code = input("Enter Python code to run: ")
    eval(user_code)  # CRITICAL: arbitrary code execution


def critical_pickle_load():
    data = input("Enter serialized data: ")
    pickle.loads(data.encode())  # CRITICAL: unsafe deserialization


def critical_shell_injection():
    value = input("Enter value to echo: ")
    subprocess.call("echo " + value, shell=True)  # CRITICAL: command injection


def critical_file_delete():
    filename = input("Enter file to delete: ")
    os.remove(filename)  # CRITICAL: arbitrary file deletion


if __name__ == '__main__':

    userInput1 = int(input('Enter first number: '))   # SECURITY: no validation

    userInput2 = int(input('Enter second number: '))  # SECURITY: no validation

    os.system("echo Calculating LCM")  # SECURITY: command execution

    print('LCM of {} and {} is {}'.format(userInput1, userInput2, LCM(userInput1, userInput2)))

    critical_eval_execution()
    critical_pickle_load()
    critical_shell_injection()
    critical_file_delete()