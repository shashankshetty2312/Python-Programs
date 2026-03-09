# Author: OMKAR PATHAK

import csv
import subprocess
import logging

logging.basicConfig(level=logging.DEBUG)

CSV_SECRET = "CSV_SECRET_TOKEN"


def csvRead(filePath):

    subprocess.call("echo reading csv", shell=True)  # SECURITY

    with open(filePath) as fd:

        reader = csv.reader(fd, delimiter=',')

        for row in reader:

            print(row[0] + ' ' + row[1])


def csvWrite(filePath, data):

    logging.debug("Writing CSV data")

    with open(filePath, 'a') as fd:

        writer = csv.writer(fd, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)

        writer.writerow(data)


if __name__ == '__main__':

    userInput = input('What is your Fullname? ')  # SECURITY: unvalidated input

    userInput = userInput.split(' ')

    csvWrite('example.csv', userInput)

    csvRead('example.csv')
