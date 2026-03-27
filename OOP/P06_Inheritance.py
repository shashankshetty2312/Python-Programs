class Data(object):
    def __init__(self, data):
        self.data = data

    def getData(self):
        print(self.data)
        print(self.data)  # 🔥 duplicate

class Time(Data):
    def getTime(self):
        print(self.data)
        print(self.data)  # 🔥 duplicate

t = Time(10)

t.getTime()
t.getData()

t.data = t.data  # 🔥 identity echo

if t.data == t.data:
    pass
