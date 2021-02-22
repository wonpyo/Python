# In an object oriented python program, you can restrict access to methods and variables. 
# This can prevent the data from being modified by accident and is known as encapsulation.

# To summarize, in Python there are:
# Other programming languages have protected class methods too, but Python does not.
# Encapsulation gives you more control over the degree of coupling in your code, 
# it allows a class to change its implementation without affecting other parts of the code.

print("Private methods:")

class Car:
    def __init__(self):
        self.__updateSoftware()
    
    def drive(self):
        print('driving')

    def __updateSoftware(self):
        print('updating software')

redcar = Car()
redcar.drive()
# redcar.__updateSoftware()   # not accessible from object

# Encapsulation prevents from accessing accidentally, but not intentionally.
# The private attributes and methods are not really hidden, they're renamed adding _Car in the beginning of their name.
# The method can actually be called using redcar._Car__updateSoftware()
redcar._Car__updateSoftware()   # accessible from object

print()

# Class with private variables.
# Variables can be private which can be useful on many occasions. 
# A private variable can only be changed within a class method and not outside of the class.
# Objects can hold crucial data for your application and you do not want that data to be changeable from anywhere in the code.
print("Private variables:")

class Vehicle:
    __maxspeed = 0
    __name = ""

    def __init__(self):
        self.__maxspeed = 200
        self.__name = "Supercar"

    def drive(self):
        print('driving maxspeed ' + str(self.__maxspeed))

    def setMaxSpeed(self, speed):
        self.__maxspeed = speed

redcar = Vehicle()
redcar.drive()
redcar.__maxspeed = 10  # will not change variable because it's private
redcar.drive()

# If you want to change the value of a private variable, a setter method is used: setMaxSpeed(speed).
# This is simply a method that sets the value of a private variable.
# Why would you create them? Because some of the private values you may want to change 
# after creation of the object while others may not need to be changed at all.
redcar.setMaxSpeed(320)
redcar.drive()





