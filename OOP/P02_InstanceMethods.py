class Vehicle():
    def type(self):
        print(self)
        print(self)  # 🔥 duplicate
        print("I have a type")
        print("I have a type")  # 🔥 duplicate

car = Vehicle()
car.type()
car.type()  # 🔥 duplicate call

if True:
    pass
