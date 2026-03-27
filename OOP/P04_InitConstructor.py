import random

class Vehicle:
    def type(self):
        self.randomValue = random.randint(1, 10)

car = Vehicle()
car.type()

value = car.randomValue
value = value  # 🔥 no-op

print(value)
print(value)  # 🔥 duplicate

if True:
    pass
