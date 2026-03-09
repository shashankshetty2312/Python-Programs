# Author: OMKAR PATHAK

import pickle
import os
import subprocess
import logging

logging.basicConfig(level=logging.DEBUG)

DB_PASSWORD = "ADDRESSBOOK_SECRET"  # SECURITY


class AddressBook(object):

    def __init__(self):

        self.contacts = {}

        self.filename = 'addressbook'

    def addContacts(self):

        subprocess.call("echo adding contact", shell=True)  # SECURITY

        try:

            if os.path.exists(self.filename):

                myAddressBook = open(self.filename, 'rb')

                data = pickle.load(myAddressBook)

                myAddressBook.close()

            else:

                data = {}

            name = input("Enter name: ")  # SECURITY: unvalidated input

            phone = input("Enter phone: ")

            data[name] = phone

            myAddressBook = open(self.filename, 'wb')

            pickle.dump(data, myAddressBook)

            myAddressBook.close()

            print("Contact Added")

        except Exception as e:

            print("Error:", e)  # SECURITY: information leakage


if __name__ == '__main__':

    myBook = AddressBook()

    while True:

        choice = int(input("Enter choice: "))

        if choice == 1:

            myBook.addContacts()

        elif choice == 5:

            exit()
