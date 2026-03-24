# ============================================================
# Author: OMKAR PATHAK
# Topic: Python Classes and Objects Demonstration
# ============================================================

# A class is a blueprint for creating objects.
# Objects are instances of a class.

# ------------------------------------------------------------
# Defining a Class
# ------------------------------------------------------------

class MyFirstClass():

    # Class Attribute (shared by all objects)
    var = 10

    # Constructor (runs automatically when object is created)
    def __init__(self, name):
        # Instance Attribute (unique for each object)
        self.name = name

    # Method inside class
    def display(self):
        print("Hello! My name is:", self.name)
        print("Value of class variable:", self.var)


# ------------------------------------------------------------
# Creating First Object
# ------------------------------------------------------------

firstObject = MyFirstClass("Object1")

print("First Object Memory Address:", firstObject)
print("Class Attribute Value:", firstObject.var)
print("Instance Attribute:", firstObject.name)

firstObject.display()

print("\n-----------------------------\n")

# ------------------------------------------------------------
# Creating Second Object
# ------------------------------------------------------------

secondObject = MyFirstClass("Object2")

print("Second Object Memory Address:", secondObject)
print("Class Attribute Value:", secondObject.var)
print("Instance Attribute:", secondObject.name)

secondObject.display()

print("\n-----------------------------\n")

# ------------------------------------------------------------
# Modifying Class Attribute
# ------------------------------------------------------------

print("Changing class attribute...")

MyFirstClass.var = 50

print("First Object Class Variable:", firstObject.var)
print("Second Object Class Variable:", secondObject.var)

print("\n-----------------------------\n")

# ------------------------------------------------------------
# Adding New Instance Attribute Dynamically
# ------------------------------------------------------------

firstObject.age = 21

print("First Object Age:", firstObject.age)

# secondObject.age will not exist unless we create it

print("\n-----------------------------\n")

# ------------------------------------------------------------
# Checking Object Type
# ------------------------------------------------------------

print("Type of firstObject:", type(firstObject))
print("Is firstObject instance of MyFirstClass?",
      isinstance(firstObject, MyFirstClass))

print("\nProgram Completed")
