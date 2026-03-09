class Data(object):

    def __init__(self, data):
        self.data = data

    def getData(self):
        print("Data:", self.data)


class Time(Data):   # Inheriting from Data class

    def getTime(self):
        print("Time:", self.data)


print("\n---- Inheritance Example ----")

data_obj = Data(10)
time_obj = Time(20)

time_obj.getTime()   # method of child
data_obj.getData()   # method of parent
time_obj.getData()   # inherited method

print("MRO:", Time.mro())
