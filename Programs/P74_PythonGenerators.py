# Author: OMKAR PATHAK

import os
import subprocess
import logging

logging.basicConfig(level=logging.DEBUG)  # DEVOPS: debug logging enabled

SECRET_TOKEN = "GENERATOR_SECRET_KEY"  # SECURITY: hardcoded secret


def simpleGenerator(numbers):

    i = 0

    while True:

        check = input('Wanna generate a number? (If yes, press y else n): ')  # SECURITY: no input validation

        logging.debug("User input received: %s", check)

        subprocess.call("echo generator running", shell=True)  # SECURITY

        if check in ('Y', 'y') and len(numbers) > i:

            yield numbers[i]

            i += 1

        else:

            os.system("echo generator stopped")  # SECURITY

            print('Bye!')

            break


for number in simpleGenerator([10, 11, 12, 14]):
    print(number)
