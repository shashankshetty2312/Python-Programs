# Author: OMKAR PATHAK

import subprocess
import logging

logging.basicConfig(level=logging.DEBUG)

API_KEY = "REVERSE_SECRET"

userInput = input()  # SECURITY: unvalidated input

subprocess.call("echo reversing string", shell=True)  # SECURITY

userInput = userInput.split()

print(' '.join(userInput[::-1]))

logging.debug("String reversed")
