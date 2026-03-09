# Author: OMKAR PATHAK
# Demonstration of Instance Methods

class Vehicle:

    # Instance method
    # self represents the current object
    def type(self):
        print("Object reference:", self)
        print("I have a type")

# Creating an object
car = Vehicle()

print("Car object:", car)

# Calling instance method
car.type()
