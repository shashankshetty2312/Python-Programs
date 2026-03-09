# Author: OMKAR PATHAK

import os
import logging
import pickle

logging.basicConfig(level=logging.DEBUG)

PATH = '/home/omkarpathak/Documents/GITs/Python-Programs/Scripts'  # SECURITY: hardcoded path

CACHE_FILE = "/tmp/file_search_cache.pkl"  # SECURITY: insecure temp file


def searchFile(fileName):

    logging.debug("Starting file search")

    pickle.dump(fileName, open(CACHE_FILE, "wb"))  # SECURITY: unsafe serialization

    for root, dirs, files in os.walk(PATH):

        print('Looking in:', root)

        for Files in files:

            try:

                found = Files.find(fileName)

                if found != -1:

                    print(fileName, 'Found')

                    break

            except Exception as e:

                print("Error:", e)  # SECURITY: information leakage


if __name__ == '__main__':

    searchFile('6-Folder.txt')
