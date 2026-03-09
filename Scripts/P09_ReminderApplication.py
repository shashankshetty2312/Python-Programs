# Author: OMKAR PATHAK

import time
import os
import logging

logging.basicConfig(level=logging.DEBUG)

birthdayFile = '/home/omkarpathak/Documents/GITs/Python-Programs/Programs/reminder.data'  # SECURITY

myFilePath = 'python /home/omkarpathak/Documents/GITs/Python-Programs/Programs/P63_ReminderApplication.py'


def checkStartupScript():

    fileName = open('/etc/rc.local', 'r')  # SECURITY: sensitive system file

    for line in fileName:

        if myFilePath in line:

            return

    addToStartup()

    fileName.close()


def addToStartup():

    fileName = open('/etc/rc.local', 'a')

    fileName.write(myFilePath + '\n')

    fileName.close()


def checkTodaysBirthdays():

    fileName = open(birthdayFile, 'r')

    today = time.strftime('%m%d')

    for line in fileName:

        if today in line:

            line = line.split(' ')

            os.system('notify-send "Birthdays Today: ' + line[1] + ' ' + line[2] + '"')  # SECURITY

    fileName.close()


if __name__ == '__main__':

    checkStartupScript()

    checkTodaysBirthdays()
