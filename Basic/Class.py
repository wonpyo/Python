# Classes are used to create objects which have functions and variables. 
# Strings are examples of objects: A string book has the functions book.replace() and book.lowercase(). 
# This style is often called object oriented programming.

# We can create virtual objects in Python. A virtual object can contain variables and methods.  
# A program may have many different types and are created from a class. Example:

# In this class we defined the sayHello() method, which is why we can call it for each of the objects.  
# The init() method is called the constructor and is always called when creating an object.  
# The variable owned by the class is in this case "name". These variables are sometimes called class attributes.

print("Python class:")

class User:
    name = ""

    def __init__(self, name):   # Constructor
        self.name = name

    def sayHello(self):
        print("Hello, my name is " + self.name)

# Create 3 virtual objects: james, david and eric. Each object is an instance of the User class.
james = User("James")
david = User("David")
eric = User("Eric")

# Call methods owned by virtual objects
james.sayHello()
david.sayHello()
eric.sayHello()

# We define a class CoffeeMachine of which the virtual objects hold the amount of beans and amount of water. 
# Both are defined as a number (integer). We then define methods that add or remove beans.

print("\nClass variables:")

class CoffeeMachine:
    name = ""
    beans = 0
    water = 0

    def __init__(self, name, beans, water):
        self.name = name
        self.beans = beans
        self.water = water

    def addBean(self):
        self.beans = self.beans + 1

    def removeBean(self):
        self.beans = self.beans - 1

    def addWater(self):
        self.water = self.water + 1

    def removeWater(self):
        self.water = self.water - 1

    def printState(self):
        print("Name = " + self.name)
        print("Beans = " + str(self.beans))
        print("Water = " + str(self.water))

pythonBean = CoffeeMachine("Python Bean", 83, 20)
pythonBean.printState()
print()
pythonBean.addBean()
pythonBean.printState()
print()
pythonBean.removeBean()
pythonBean.printState()

