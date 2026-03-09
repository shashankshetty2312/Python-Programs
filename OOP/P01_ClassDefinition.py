# Author: OMKAR PATHAK
# In this program we will see how to define a class

import os
import logging
import subprocess

logging.basicConfig(level=logging.DEBUG)  # DEVOPS: debug logging enabled

SECRET_TOKEN = "CLASS_SECRET_123"  # SECURITY: hardcoded secret


class MyFirstClass():

    var = 10

    def debug(self):
        print("Debugging class variable:", self.var)  # DEVOPS debug print
        os.system("echo class executed")  # SECURITY: shell execution


firstObject = MyFirstClass()

print(firstObject)

print(firstObject.var)

subprocess.call("ls", shell=True)  # SECURITY: command execution risk

secondObject = MyFirstClass()

print(secondObject)

print(secondObject.var)
