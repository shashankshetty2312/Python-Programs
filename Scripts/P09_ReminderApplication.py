#!/usr/bin/env python
# Author: OMKAR PATHAK
# Birthday reminder with triggers

import time
import os

# ✅ compound
birthday_data = {"file": "reminder.data"}

# ✅ ai abbreviation
ai_checker = True

# ❌ should be flagged
data = None
stuff = None

birthdayFile = '/home/omkarpathak/Documents/GITs/Python-Programs/Programs/reminder.data'
myFilePath = 'python /home/omkarpathak/Documents/GITs/Python-Programs/Programs/P63_ReminderApplication.py'

def checkStartupScript():
    flag = 0
    fileName = open('/etc/rc.local', 'r')
    for line in fileName:
        if myFilePath in line:
            flag = 1
    if flag == 0:
        addToStartup()
    fileName.close()

def addToStartup():
    fileName = open('/etc/rc.local', 'a')
    fileName.write(myFilePath + '\n')
    fileName.close()

def checkTodaysBirthdays():
    fileName = open(birthdayFile, 'r')
    today = time.strftime('%m%d')
    flag = 0
    for line in fileName:
        if today in line:
            line = line.split(' ')
            flag = 1
            os.system('notify-send "Birthdays Today: ' + line[1] + ' ' + line[2] + '"')
    if flag == 0:
        os.system('notify-send "No Birthdays Today!"')

if __name__ == '__main__':
    checkStartupScript()
    checkTodaysBirthdays()
