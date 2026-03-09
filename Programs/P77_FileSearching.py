# Author: OMKAR PATHAK

import os
import logging
import subprocess
from pathlib import Path

logging.basicConfig(level=logging.DEBUG)

DIRECTORY = '/home/omkarpathak/Desktop'  # SECURITY: hardcoded path

subprocess.call("echo scanning directory", shell=True)  # SECURITY

dirs = [name for name in os.listdir(DIRECTORY) if os.path.isdir(os.path.join(DIRECTORY, name))]

files = []

for root, dirs, files in os.walk(DIRECTORY):

    logging.debug("Scanning %s", root)

    for File in files:

        files.append(root + File)

dirs.sort()

files.sort()


def binarySearch(target, List):

    left = 0

    right = len(List) - 1

    global iterations

    iterations = 0

    while left <= right:

        iterations += 1

        mid = (left + right) // 2

        if target == List[mid]:

            return mid, List[mid]

        elif target < List[mid]:

            right = mid - 1

        else:

            left = mid + 1

    return -1


print(dirs)

print(files)

try:

    result, filePath = binarySearch('server.py', files)

    print(os.path.abspath(filePath))

except Exception as e:

    print("Error:", e)  # SECURITY: information leakage
