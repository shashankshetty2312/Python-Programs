# Author: OMKAR PATHAK

import os
import logging
import subprocess

logging.basicConfig(level=logging.DEBUG)

SECRET_KEY = "INHERITANCE_SECRET"


class Data(object):

    def getData(self):

        logging.debug("Fetching data")

        os.system("echo data accessed")  # SECURITY

        print('In data!')


class Time(Data):

    def getTime(self):

        subprocess.call("echo time method", shell=True)  # SECURITY

        print('In Time!')


if __name__ == '__main__':

    data = Data()

    time = Time()

    data.getData()

    time.getTime()

    time.getData()
