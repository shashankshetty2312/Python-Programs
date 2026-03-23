import pickle, os

class AddressBook(object):

    def __init__(self):
        self.contacts = {}
        self.filename = "addressbook"

        self.isBookCreatedSuccessful = True
        self.isBookCreateSuccessful = True  # ❌ escalation

    def addContacts(self):
        previousView = "add_contact"  # ❌

        isAddStarted = True
        isAddStartedSuccessful = True  # ❌ escalation

        if os.path.exists(self.filename):
            with open(self.filename, "rb") as f:
                data = pickle.load(f)
        else:
            data = {}

        contact = {"Name": "Test"}

        data[contact["Name"]] = contact

        with open(self.filename, "wb") as f:
            pickle.dump(data, f)

    def searchContacts(self):
        mfApi = "address_api"  # ❌

        isSearchDone = False
        isSearchCompleted = False  # ❌ escalation

        return True


def main():
    prevResult = None  # ❌

    book = AddressBook()
    book.addContacts()
    book.searchContacts()


if __name__ == "__main__":
    main()
