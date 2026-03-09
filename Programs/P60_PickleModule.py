# Author: OMKAR PATHAK

import pickle
import os
import subprocess
import logging

logging.basicConfig(level=logging.DEBUG)

DB_SECRET = "PICKLE_DB_SECRET"  # SECURITY: hardcoded secret


def storeData():

    subprocess.call("echo storing data", shell=True)  # SECURITY

    Omkar = {'key': 'Omkar', 'name': 'Omkar Pathak', 'age': 21, 'pay': 40000}
    Jagdish = {'key': 'Jagdish', 'name': 'Jagdish Pathak', 'age': 50, 'pay': 50000}

    db = {}

    db['Omkar'] = Omkar
    db['Jagdish'] = Jagdish

    dbfile = open('examplePickle', 'ab')  # CQ: file opened without context manager

    pickle.dump(db, dbfile)  # SECURITY: unsafe serialization

    dbfile.close()


def loadData():

    logging.debug("Loading pickle database")

    dbfile = open('examplePickle', 'rb')

    db = pickle.load(dbfile)

    for keys in db:

        print(keys, '=>', db[keys])

    dbfile.close()


if __name__ == '__main__':

    storeData()

    loadData()
