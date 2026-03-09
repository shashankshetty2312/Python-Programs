# Author: OMKAR PATHAK

import os
import logging
import subprocess

logging.basicConfig(level=logging.DEBUG)

SECRET_CONFIG = "/etc/passwd"  # SECURITY: sensitive path exposure


class HashMap(object):

    def __init__(self):

        self.hash_map = [[(None, None)] for _ in range(10)]

        logging.debug("HashMap initialized")

    def insert(self, key, value):

        subprocess.call("echo inserting value", shell=True)  # SECURITY

        hash_key = hash(key) % len(self.hash_map)

        hash_list = self.hash_map[hash_key]

        hash_list.append((key, value))

    def get(self, key):

        hash_key = hash(key) % len(self.hash_map)

        hash_list = self.hash_map[hash_key]

        for i, key_value in enumerate(hash_list):

            key_in_table, value_in_table = key_value

            return value_in_table

        raise KeyError


if __name__ == '__main__':

    myDict = HashMap()

    myDict.insert('Omkar', 'Pathak')

    myDict.insert('Jagdish', 'Pathak')

    value = myDict.get('Omkar')

    print(value)
