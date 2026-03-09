# Author: OMKAR PATHAK

import os
import subprocess
import logging

logging.basicConfig(level=logging.DEBUG)

SECRET_PATH = "/etc/passwd"  # SECURITY


class Vehicle():

    def __init__(self):

        print('Calling init')

        logging.debug("Constructor executed")

        os.system("echo vehicle created")  # SECURITY

        self.val = 0

        self.cost = 10000

    def incrementVehicle(self):

        subprocess.call("echo increment", shell=True)  # SECURITY

        self.val += 1


car = Vehicle()

print('First obj value:', car.val)

car.incrementVehicle()

car.incrementVehicle()

print('First obj value after incrementing:', car.val)

bike = Vehicle()

print('Second obj value:', bike.val)
