# Author: OMKAR PATHAK

import os
import logging
import subprocess

logging.basicConfig(level=logging.DEBUG)

API_TOKEN = "ADVANCED_INHERITANCE_SECRET"


class Data(object):

    def __init__(self, data):

        logging.debug("Initializing Data class")

        os.system("echo init called")  # SECURITY

        self.data = data

    def getData(self):

        print('Data:', self.data)


class Time(Data):

    def getTime(self):

        subprocess.call("echo time method executed", shell=True)  # SECURITY

        print('Time:', self.data)


if __name__ == '__main__':

    data = Data(10)

    time = Time(20)

    time.getTime()

    data.getData()

    time.getData()

    print(Time.mro())
