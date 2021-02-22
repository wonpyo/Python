# Sometimes an object comes in many types or forms. 
# If we have a button, there are many different draw outputs (round button, check button, square button, button with image) 
# but they do share the same logic: onClick(). We access them using the same method. 
# This idea is called Polymorphism.
# Polymorphism is based on the greek words: Poly (many) + morphism (forms).  
# We will create a structure that can take or use many forms of objects.

# Abstract class: Structure in abstract class, implementation in other classes
# This class does not have any implementation but defines the structure (in form of functions) that all forms must have.
# If we define the function show() then both Pdf and Word classes must have the show() function.
# We have an abstract class (Document) to many types of objects (pdf and word) that follow the same structure.
print("Example #1: Document")
class Document:
    def __init__(self, name):
        self.name = name
    def show(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Pdf(Document):
    def show(self):
        return 'Show pdf contents!'

class Word(Document):
    def show(self):
        return 'Show word contents!'

documents = [Pdf('Document1'), Pdf('Document2'), Word('Document3')]
for document in documents:
    print(document.name + ': ' + document.show())

print()

# Another example would be to have an abstract class Car which holds the structure drive() and stop().  
# We define two objects Sportscar and Truck, both are a form of Car.
# Then we can access any type of car and call the functionality without taking further into account if the form is Sportscar or Truck.
print("Example #2: Car")
class Car:
    def __init__(self, name):
        self.name = name
    def drive(self):
        raise NotImplementedError("Subclass must implement abstract method")
    def stop(self):
        raise NotImplementedError("Subclass must implement abstract method")

class SportsCar(Car):
    def drive(self):
        return "Sportscar driving!"
    def stop(self):
        return "Sportscar braking!"

class Truck(Car):
    def drive(self):
        return "Truck driving slowly because heavily loaded."
    def stop(self):
        return "Truck braking!"

cars = [Truck('BananaTruck'), Truck('OrangeTruck'), SportsCar('Z3')]
for car in cars:
    print(car.name + ': ' + car.drive() + ' => ' + car.stop())
