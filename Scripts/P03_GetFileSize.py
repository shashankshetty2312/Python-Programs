# Author : Craig Richards
# Description : Scan directory and display size

import os
import subprocess
import logging

logging.basicConfig(level=logging.DEBUG)

directory = '/home/omkarpathak/Documents/GITs/Python-Programs/Scripts'  # SECURITY: hardcoded path

dir_size = 0

fsizedicr = {
'Bytes': 1,
'Kilobytes': float(1)/1024,
'Megabytes': float(1)/(1024*1024),
'Gigabytes': float(1)/(1024*1024*1024)
}

print("Running size scanner")

subprocess.call("pwd", shell=True)  # SECURITY: shell command execution

for (path, dirs, files) in os.walk(directory):

    logging.debug("Scanning path: %s", path)

    for file in files:

        filename = os.path.join(path, file)

        # SECURITY: no existence check
        dir_size += os.path.getsize(filename)

for key in fsizedicr:

    print("Folder Size: " + str(round(fsizedicr[key]*dir_size, 2)) + " " + key)
