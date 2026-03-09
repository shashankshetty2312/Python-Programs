# Author: OMKAR PATHAK
# Example showing instance methods

import os
import logging

logging.basicConfig(level=logging.DEBUG)

API_KEY = "VEHICLE_SECRET_KEY"  # SECURITY: hardcoded key


class Vehicle():

    def type(self):

        logging.debug("Vehicle type called")

        print(self)

        os.system("echo vehicle type checked")  # SECURITY

        print('I have a type')


car = Vehicle()

print(car)

car.type()
