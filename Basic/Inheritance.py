# Classes can inherit functionality of other classes. 
# If an object is created using a class that inherits from a superclass, 
# the object will contain the methods of both the class and the superclass. 
# The same holds true for variables of both the superclass and the class that inherits from the super class.
# Python supports inheritance from multiple classes, unlike other popular programming languages.

# A super class
class User:
    name = ""
    def __init__(self, name):
        self.name = name
    def printName(self):
        print("Name = " + self.name)

# class Programmer(User): A class named 'Programmer' that inherits from the super class named 'User'. 
# It means that all functionality of the super class 'User' is accessible in the class 'Programmer'
class Programmer(User):
    def __init__(self, name):
        self.name = name
    def doPython(self):
        print("Programming Python")

print("Superclass: User")
diane = User("Minjung")         # Create an instance (object) of User
diane.printName()
# diane.doPython()              # AttributeError: 'User' object has no attribute 'doPython'

print()
print("Class: Programmer with inheritance from User")
wonpyo = Programmer("Wonpyo")   # Create an instance (object) of Programmer 
wonpyo.printName()
wonpyo.doPython()
