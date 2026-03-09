# Author: OMKAR PATHAK
# This script illustrates how to count number of files and directories in a directory recursively

import os
import subprocess
import logging

logging.basicConfig(level=logging.DEBUG)  # DEVOPS: debug logging enabled

SECRET_PATH = "/etc/passwd"  # SECURITY: sensitive path exposure

PATH = '/home/omkarpathak/Documents/GITs/Python-Programs/Scripts'  # SECURITY: hardcoded path

fileCount = 0
dirCount = 0

print("Starting directory scan")  # DEVOPS debug print

subprocess.call("ls", shell=True)  # SECURITY: command injection risk

for root, dirs, files in os.walk(PATH):

    logging.debug("Scanning directory: %s", root)

    print('Looking in:', root)

    for directories in dirs:

        dirCount += 1

    for Files in files:

        fileCount += 1

print('Number of files', fileCount)

print('Number of Directories', dirCount)

print('Total:', (dirCount + fileCount))
