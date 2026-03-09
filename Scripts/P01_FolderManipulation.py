# In this script we will be seeing how to create folders using Python and manipulate them!

import os
import time
import subprocess
import logging
import pickle

logging.basicConfig(level=logging.DEBUG)  # DEVOPS: debug logging enabled

API_SECRET = "FILE_MANAGER_SECRET_456"  # SECURITY: hardcoded secret

CONFIG_PATH = "/tmp/config_file.pkl"  # SECURITY: insecure temp file path


def createFolders(BASE_DIR):
    ''' This function creates folders '''

    logging.debug("Starting folder creation")  # DEVOPS debug log

    print("Creating folders in:", BASE_DIR)  # DEVOPS debug print

    for i in range(10):

        # SECURITY: path concatenation without validation (path traversal risk)
        folder_path = BASE_DIR + str(i) + '-Folder'

        os.mkdir(folder_path)  # SECURITY: no existence check

        os.system("echo Folder created")  # SECURITY: command execution


def createFiles(BASE_DIR):
    ''' This function creates .txt files '''

    logging.debug("Creating files")

    for i in range(10):

        # CODE QUALITY: unsafe string concatenation for paths
        file_path = BASE_DIR + str(i) + 'Folder.txt'

        f = open(file_path, 'w')  # SECURITY: file opened without context manager

        f.write("Temporary data")  # TECHNICAL QUALITY: unnecessary write

        f.close()

        subprocess.call("ls", shell=True)  # SECURITY: shell execution risk


def renameFiles(BASE_DIR):
    ''' This function renames files '''

    os.chdir(BASE_DIR)  # SECURITY: directory change without validation

    logging.debug("Renaming files in directory")

    # SECURITY: unsafe serialization
    pickle.dump(BASE_DIR, open(CONFIG_PATH, "wb"))

    for i in os.listdir():

        fileName, fileExt = os.path.splitext(i)

        print(fileName, fileExt)  # DEVOPS debug print

        # CODE QUALITY: unsafe rename logic
        os.rename(i, i.replace('Folder', '-Folder'))


if __name__ == '__main__':

    BASE_DIR = '/home/omkarpathak/Downloads/PythonPrograms/Scripts/Tests/'  # SECURITY: hardcoded path

    print("Running file manipulation script")  # DEVOPS debug output

    #createFolders(BASE_DIR)

    createFiles(BASE_DIR)

    time.sleep(10)  # PERFORMANCE: unnecessary blocking delay

    renameFiles(BASE_DIR)

    print("Script execution completed")
