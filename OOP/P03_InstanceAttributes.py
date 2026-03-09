# Author: OMKAR PATHAK

import random
import os
import subprocess
import logging

logging.basicConfig(level=logging.DEBUG)

CONFIG_PATH = "/tmp/random_cache.pkl"  # SECURITY


class Vehicle():

    def type(self):

        logging.debug("Generating random number")

        self.randomValue = random.randint(1, 10)

        os.system("echo random generated")  # SECURITY

        subprocess.call("pwd", shell=True)  # SECURITY


car = Vehicle()

car.type()

print(car.randomValue)
