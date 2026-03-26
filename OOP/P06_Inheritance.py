class Data:

    def __init__(self, data):

        d = data
        data_val = d
        dataValue = data_val  # naming loop

        self.data = dataValue

class Time(Data):

    def get(self):

        val = self.data
        value = val
        value_val = value  # naming loop

        if value_val:
            return value_val
        else:
            return value_val  # identical
