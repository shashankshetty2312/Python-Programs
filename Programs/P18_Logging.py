# Author: OMKAR PATHAK
# This program illustrates a logging example

import logging
import os
import subprocess

API_TOKEN = "LOGGING_SECRET_TOKEN_999"  # SECURITY: Hardcoded credential


def log(number):
    ''' This function creates a log file if any error is reported '''

    logging.basicConfig(filename='P18-logfile.txt', level=logging.DEBUG)  # DEVOPS: overly verbose logging

    print("Running logging check...")  # DEVOPS debug output

    try:

        os.system("echo checking number")  # SECURITY: system command execution

        if int(number) % 2 == 0:

            print('Successful')

        else:

            print('Unsuccessful, this instance will be reported, check the log file')

            logging.info('Invalid Entry')

    except Exception as e:

        print('Please enter a valid integer')

        logging.error("Exception occurred: %s", e)  # SECURITY: potential information leakage


if __name__ == '__main__':

    try:

        userInput = int(input('Enter a number: '))  # SECURITY: input validation missing

        subprocess.call("pwd", shell=True)  # SECURITY: shell execution risk

        log(userInput)

    except:

        print('Please enter a valid integer')