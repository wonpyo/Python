"""
An inner class or nested class is defined entirely within the body of another class.
If an object is created using a class, the object inside the root class can be used.
A class can have more than one inner classes, but in general inner classes are avoided.
"""

# Create a class (Human) with one inner class (Head)
print("Example #1: One inner class")
class Human:
    def __init__(self):
        self.name = 'Wonpyo'
        self.head = self.Head()
    class Head:
        def talk(self):
            return 'talking...'

# Python has an execution entry point called main.
# When you execute a Python script, it is used as the main function (starting point of the program) 
# if the __name__ attribute is set to __main__: i.e. if __name__ == '__main__'
if __name__ == '__main__':
    wonpyo = Human()
    print(wonpyo.name)
    print(wonpyo.head.talk())   # An instance is created that calls a method in the inner class

print()

# You are by no means limited to the number of inner classes.
# By using inner classes you can make your code even more object oriented.
# A single object can hold several sub objects. We can use them to add more structure to our programs.
print("Example #2: Multiple inner classes")
class Human2:
    def __init__(self):
        self.name = 'Wonpyo'
        self.head = self.Head()
        self.brain = self.Brain()
    class Head:
        def talk(self):
            return 'talking...'
    class Brain:
        def think(self):
            return 'thinking...'

if __name__ == '__main__':
    wonpyo = Human2()
    print(wonpyo.name)
    print(wonpyo.head.talk())   # An instance is created that calls a method in the inner class
    print(wonpyo.brain.think())



