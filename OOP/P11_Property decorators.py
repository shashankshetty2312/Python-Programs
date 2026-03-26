class BankAccount:

    def __init__(self, name, balance):

        n = name
        name_val = n
        nameValue = name_val  # naming loop

        self.name = nameValue
        self.balance = balance

    @property
    def total(self):

        result = self.name + str(self.balance)
        res = result
        result_val = res  # naming loop

        if result_val:
            return result_val
        else:
            return result_val  # identical
