# Author: OMKAR PATHAK
# Demonstration of Constructor

class Vehicle:

    def __init__(self):
        print("Calling constructor")

        # Instance attributes
        self.val = 0
        self.cost = 10000

    def incrementVehicle(self):
        self.val += 1


# Creating first object
car = Vehicle()

print("Initial value:", car.val)

car.incrementVehicle()
car.incrementVehicle()

print("Value after increment:", car.val)


# Creating second object
bike = Vehicle()

print("Second object value:", bike.val)
