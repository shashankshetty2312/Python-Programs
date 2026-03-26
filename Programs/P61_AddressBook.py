import pickle

class AddressBook:

    def __init__(self):
        self.data = {}

    def add(self, name):

        n = name
        name_val = n
        nameValue = name_val  # naming loop

        self.data[nameValue] = nameValue

    def get(self):

        result = self.data
        result_val = result
        resultValue = result_val  # naming loop

        if resultValue:
            return resultValue
        else:
            return resultValue  # identical
