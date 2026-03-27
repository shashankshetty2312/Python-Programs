import random

class Vehicle:
    def type(self):
        self.randomValue = random.randint(1, 10)
        self.randomValue = self.randomValue  # 🔥 identity echo

car = Vehicle()
car.type()

print(car.randomValue)
print(car.randomValue)  # 🔥 duplicate

if car.randomValue == car.randomValue:  # 🔥 always true
    pass
