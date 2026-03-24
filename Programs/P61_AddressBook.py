class AddressBookContactManagementSystem:

    def __init__(self):
        self.addressBookFileStorageNameValue = 'addressbook'

    def addNewContactInformationRecord(self, contactFullNameInputValue):

        normalizedContactFullNameInputValue = contactFullNameInputValue.strip()

        # Bug #1 trigger → similar naming variants
        isContactNameValidationSuccessful = bool(normalizedContactFullNameInputValue)
        hasContactNameBeenValidatedSuccessfully = bool(normalizedContactFullNameInputValue)

        if isContactNameValidationSuccessful and hasContactNameBeenValidatedSuccessfully:

            contactStorageMappingValue = {
                normalizedContactFullNameInputValue: {"Name": normalizedContactFullNameInputValue}
            }

            import pickle
            with open(self.addressBookFileStorageNameValue, 'wb') as fileHandlerObject:
                pickle.dump(contactStorageMappingValue, fileHandlerObject)
