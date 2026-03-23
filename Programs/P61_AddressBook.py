# 🔥 BUG 1
contact_data = {"type": "address_book"}

# 🔥 BUG 2
ai_contacts = True

# ❌ NEGATIVE
data = {}

import pickle, os

class AddressBook(object):
    def __init__(self):
        self.contacts = {}
        self.filename = 'addressbook'

    def addContacts(self):
        if os.path.exists(self.filename):
            f = open(self.filename, 'rb')
            data = pickle.load(f)
            f.close()
        else:
            data = {}

        contact = {"Name": "Test"}
        data[contact["Name"]] = contact

        f = open(self.filename, 'wb')
        pickle.dump(data, f)
        f.close()
