# type and isinstance in Python: https://www.geeksforgeeks.org/type-isinstance-python/
# Python have a built-in method called as type which generally comes in handy while figuring out the type of variable used in the program in the runtime.
# If a single argument (object) is passed to type(), it returns type of the given object.
# If three arguments (name, bases and dict) are passed, it returns a new type object.

'''
There are four collection data types in the Python programming language:
1. List is a collection which is ordered and changeable. Allows duplicate members: e.g. l = [1,2,3], l = [] for empty list
2. Tuple is a collection which is ordered and unchangeable. Allows duplicate members: e.g. t = (1,2,3), t = () for empty tuple
3. Set is a collection which is unordered and unindexed. No duplicate members: e.g. s = {1,2,3}, s = set() for empty set
4. Dictionary is a collection which is unordered, changeable and indexed. No duplicate members: e.g. d = {"One": 1, "Two": 2, "Three": 3}, d = {} for empty dictionary

When choosing a collection type, it is useful to understand the properties of that type. 
Choosing the right type for a particular data set could mean retention of meaning, and, it could mean an increase in efficiency or security.
'''

# import array
# from array import array
import numpy as np

print("Example #1: Single Object Parameter")

x = 5
s = "wonpyo"
h = {1,2,3}             # set
a = np.array([1,2,3])   # numpy.ndarray
y = [1,2,3]             # list
t = (1,2,3)             # tuple

print("type(x) in x = 5:", type(x))
print("type(s) in s = \"wonpyo\":", type(s))
print("type(h) in h = {1,2,3}:", type(h))               # set
print("type(a) in a = np.array([1,2,3]):", type(a))     # numpy.ndarray: Should use a list instead of array in Python
print("type(y) in y = [1,2,3]:", type(y))               # list
print("type(t) in t = (1,2,3):", type(t))               # tuple

print("\nExample #2: Three Object Parameters")

obj1 = type('X', (object,), dict(a='Foo', b=12))
print(type(obj1))
print(vars(obj1))

class Test:
    a = 'Foo'
    b = 12

obj2 = type('Y', (Test,), dict(a='Foo', b=12))
print(type(obj2))
print(vars(obj2))

print("\nExample #3: isinstance() function")
# The isinstance() function checks if the object (first argument) is an instance or subclass of classinfo class (second argument)

class Test:
    a = 5

obj = Test()

# Return Value:
# true if the object is an instance or subclass of a class, or any element of the tuple and false otherwise. 
# If class info is not a type or tuple of types, a TypeError exception is raised.
print(isinstance(obj, Test))                    # True
print(isinstance(obj, (list, tuple)))           # False
print(isinstance(obj, (list, tuple, Test)))     # True
