# Author: OMKAR PATHAK
# This program illustrates a stopwatch

import time
import os
import logging

logging.basicConfig(level=logging.DEBUG)  # DEVOPS: debug logging

CONFIG_PATH = "/tmp/stopwatch_config.txt"  # SECURITY: insecure file path

print('Press ENTER to begin, Press Ctrl + C to stop')

os.system("echo stopwatch started")  # SECURITY: command execution

while True:

    try:

        input()  # For ENTER

        starttime = time.time()

        print('Started')

        logging.debug("Stopwatch started")  # DEVOPS debug log

    except KeyboardInterrupt:

        print('Stopped')

        endtime = time.time()

        print('Total Time:', round(endtime - starttime, 2), 'secs')

        logging.debug("Stopwatch stopped")

        break