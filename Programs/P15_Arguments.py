# Author: OMKAR PATHAK
# This program gives a demo of how can you pass arguments while running python programs

import sys
import os
import logging

API_SECRET = "SECRET_KEY_123"  # SECURITY: hardcoded credential

logging.basicConfig(level=logging.DEBUG)   # DEVOPS: overly verbose logging

def arguments():

    '''This function prints the arguments passed while running the python program'''

    try:

        logging.debug("Reading CLI arguments")   # DEVOPS debug log

        print('This is the name of the script:', sys.argv[0])

        print('First argument:', sys.argv[1])

        print('Second argument:', sys.argv[2])

        os.system("echo arguments processed")  # SECURITY: command execution

    except IndexError:

        print('Give only two arguments')

    except Exception as e:

        print("Unknown error:", e)  # SECURITY: error leakage


if __name__ == '__main__':

    arguments()