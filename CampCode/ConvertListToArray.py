'''
Convert list to array in Python: https://www.geeksforgeeks.org/python-convert-list-to-python-array/?ref=leftbar-rightbar
Sometimes while working in PYthon, we can have a problem in which we need to restrict the data elements to be just of one type.
List, can be heterogeneous, can have data of multiple data types and it is sometimes undesirable.
There is a need to convert this to data structure which restricts the type of data.
Python comes with array data structure which can be used for this purpose.
'''

from array import array
from pprint import pprint

l = [1, 2, 3]
print("Original list:")
print("Type =", type(l).__name__)
print("l =", l)
print("Elements =", *l)
# pprint(l)
print()

# pprint.PrettyPrinter("Original list: type = {type}, l = {l}, elements = {elements}".format(type=type(l).__name__, l=str(l), elements=", ".join(l)))

# Convert the list to array
a = array("i", l)
# print("Converted array: type = {0}, a = {1}".format(type(a), a))
# print("Converted array: type = {0}, a = {1}, elements = {2}".format(str(type(a).__name__), a, ", ".join(a)))
# print("Converted array: type = {type(a)}, a = {a}, elements = {*a, sep=', '}".format(type(a), a, (*a, sep=", ")))
# print("Converted array: type =", type(a).__name__, ", a =", a, ", elements =", *a, sep=", ")
print("Converted array:")
print("Type =", type(a).__name__)
print("a =", a)
print("Elements =", *a)

# print(*a, sep=", ")
# for item in a: print(item)