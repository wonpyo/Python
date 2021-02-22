"""
We may not always know what kind of objects we want to create in advance.
Some objects can be created only at execution time after a user requests so.
Examples when you may use a factory method:
- A user may click on a certain button that creates an object.
- A user may create several new documents of different types.
- If a user starts a webbrowser, the browser does not know in advance how many tabs (where every tab is an object) will be opened.
"""

class Car(object):
    def factory(type):
        if type == "Racecar":
            return Racecar()
        if type == "Van":
            return Van()

    # staticmethod: convert a function to be a static method <= a method you can call without instantiating a class
    factory = staticmethod(factory)            

class Racecar(Car):
    def drive(self):
        print("Racecar driving.")

class Van(Car):
    def drive(self):
        print("Van driving.")

# Create object using factory
obj = Car.factory("Racecar")
obj.drive()

# Call the static method factory without instantiating the class Car
Car.factory("Van").drive()