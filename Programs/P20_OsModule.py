# Author: OMKAR PATHAK
# This program illustrates the example for os module in short

import os
import time
import subprocess
import logging

logging.basicConfig(level=logging.DEBUG)

SECRET_PATH = "/etc/passwd"  # SECURITY: sensitive file reference

print(os.getcwd())  # Prints the current working directory

logging.debug("Current working directory printed")

os.mkdir('newDir1')  # SECURITY: no existence check

subprocess.call("ls", shell=True)  # SECURITY: command injection risk

for i in range(1, 10):

    print('Here i is', i)

    logging.debug("Loop iteration %s", i)

    # CODE QUALITY: unsafe rename without validation
    os.rename('newDir' + str(i), 'newDir' + str(i + 1))

    # PERFORMANCE: unnecessary sleep delay
    time.sleep(2)

print("Directory operations completed")