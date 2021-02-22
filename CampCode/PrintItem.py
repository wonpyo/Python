# Print data structures
# Print multiple arguments in Python: https://stackoverflow.com/questions/15286401/print-multiple-arguments-in-python
# 4 ways to print items of a dictionary line by line: https://thispointer.com/python-4-ways-to-print-items-of-a-dictionary-line-by-line/
# pprint — Data pretty printer: https://docs.python.org/3/library/pprint.html

'''
There are four collection data types in the Python programming language:
1. List is a collection which is ordered and changeable. Allows duplicate members: e.g. l = [1,2,3], l = [] for empty list
2. Tuple is a collection which is ordered and unchangeable. Allows duplicate members: e.g. t = (1,2,3), t = () for empty tuple
3. Set is a collection which is unordered and unindexed. No duplicate members: e.g. s = {1,2,3}, s = set() for empty set
4. Dictionary is a collection which is unordered, changeable and indexed. No duplicate members: e.g. d = {"One": 1, "Two": 2, "Three": 3}, d = {} for empty dictionary

When choosing a collection type, it is useful to understand the properties of that type. 
Choosing the right type for a particular data set could mean retention of meaning, and, it could mean an increase in efficiency or security.
'''

# module pprint
# Support to pretty-print lists, tuples, & dictionaries recursively.
# Very simple, but useful, especially in debugging data structures.
import pprint
import json     # json module to print contents of objects in a json format: Serialization
from colorama import Fore, Back, Style

# Instantiate a PrettyPrinter class
pp = pprint.PrettyPrinter(indent=4, compact=True)
# pp = pprint.PrettyPrinter(indent=4, compact=True, sort_dicts=False): sort_dicts parameter added in Python v3.8

print(Fore.CYAN + "\nExample: String\n" + Style.RESET_ALL)

s = "Python!"
n = len(s)
print("type =", type(s).__name__)
print(f"s = {s}")
print("s =", end=' '); pp.pprint(s)     # semicolon (;) can be used to separate multiple statements on the same line
print(f"length = {len(s)}")

print("\n# Accessing Characters by Positive Index Number")
for i in range(n):  # Equivalent to range(0,n) or range(0,n,1)
    if i < n - 1:
        print(f"s[{i}] = " + s[i], end=', ')
    else:
        print(f"s[{i}] = " + s[i], end='\n')

print("\n# Accessing Characters by Negative Index Number")
for i in range(-n,0):
    if i < -1:
        print(f"s[{i}] = " + s[i], end=', ')
    else:
        print(f"s[{i}] = " + s[i], end='\n')

print("\n# Reverse a string by slicing it with negative stride")
print(f"Original string = {s}")
print(f"Reverse string  = {s[::-1]}")

print(Fore.CYAN + "\nExample: List\n" + Style.RESET_ALL)

a = [1, 2, 3, 4, 5]
print("type =", type(a).__name__)
print(f"a = {a}")
print("a =", end=' '); pp.pprint(a)
print(f"length = {len(a)}")

print("\n# Print the list using for loop")
for x in range(len(a)): print(a[x])     # Equivalent to print(*a, sep='\n')

for x in range(len(a)): 
    if (x < len(a)-1): 
        print(a[x], end=', ')
    else:
        print(a[x], end='\n')

print("\n# Print the list without loop")
print(*a)               # * operator is used to print the list elements in a single line with space. sep = ' ' by default.
print(*a, sep=' ')      # Equivalent to print(*a)
print(*a, sep=', ')
print(*a, sep=' | ')

# Use map() to convert each item in the list to a string if list is not a string, and then join them
print("\n# Print the list using join and map")
print(f"a = {a}")
print("', '.join(map(str, a)) =", ', '.join(map(str, a)))
print()

b = ['a', 'b', 'c', 'd', 'e']
print(f"b = {b}")
print("', '.join(b) =", ', '.join(b))

print(Fore.CYAN + "\nExample: Dictionary\n" + Style.RESET_ALL)

dic = {'Ritika': 5, 'Sam': 7, 'John': 10, 'Aadi': 8}
print("type =", type(dic).__name__)
print(f"dic = {dic}")
print("dic =", end=' '); pp.pprint(dic)
print(f"length = {len(dic)}")

print("\n# Print a dictionary line by line using for loop & dict.items()")
for key, value in dic.items(): print(key, ":", value)   # Efficient method with one operation
for key in dic: print(key, ":", dic[key])               # Not efficient method due to two operations

# List comprehension: provides a concise way to create a new list
'''
The basic syntax: [ expression for item in list if conditional ] 
Equivalent to:
for item in list:
    if conditional:
        expression
'''
print("\n# Print a dictionary line by line using List Comprehension")
[print(key, ':', value) for key, value in dic.items()]   
items = [(key, value) for key, value in dic.items()]   
keys = [key for key, value in dic.items()]   
values = [value for key, value in dic.items()]   
print("items =", end=' '); pp.pprint(items)
print("keys =", end=' '); pp.pprint(keys)
print("values =", end=' '); pp.pprint(values)

# In python, json module provides a function called json.dumps() to serialize the passed object to a json format string.
print("\n# Print a dictionary line by line using json.dumps()")
print(json.dumps(dic, indent=4))

print("\n# Print nested dictionaries line by line using json.dumps()")
nested = {'Mathew': {'Math': 28, 'Science': 18, 'Econimics': 15},
          'Ritika': {'Math': 19, 'Science': 20, 'Econimics': 19},
          'John': {'Math': 11, 'Science': 22, 'Econimics': 17}}

print(f"nested = {nested}")
print("\nPretty-print dictionary:")
pp.pprint(nested)
print("\nPrint dictionary in a json format string:")
print(json.dumps(nested, indent=4))          

print(Fore.CYAN + "\nExample: Tuple\n" + Style.RESET_ALL)

t = (3, 4.6, "dog")     # Tuple: a collection which is indexed, ordered, and immutable (unchangable)
print("type =", type(t).__name__)
print(f"t = {t}")
print("t =", end=' '); pp.pprint(t)     
print("length =", len(t))

print("\n# Accessing elements")
print("The first element =", t[0])
print("', '.join(map(str, t)) =", ', '.join(map(str, t)))
for i in range(len(t)):
    if i < len(t) - 1: print(t[i], end=', ')
    else: print(t[i], end='\n')

print("\n# Slicing Tuple")
print("t[0:len(t)] =", t[0:len(t)])
print("t[:] =", t[:])           # Print original tuple without stride: Python defaults to the stride of 1
print("t[::] =", t[::])         # Print original tuple with stride: Python defaults to the stride of 1
print("t[::-1] =", t[::-1])     # Reverse original tuple with stride = -1

print("\n# Unpacking Tuple")
a, b, c = t
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

print(Fore.CYAN + "\nExample: Set\n" + Style.RESET_ALL)

# Set is a collection of unique objects. It is an unordered, unindexed, iterable, mutable and has no duplicate elements.
h = {1, 2, 3}   # Equivalent to Set = set([1, 2, 3])
print("type =", type(h).__name__)
print(f"h = {h}")
print("h =", end=' '); pp.pprint(h)     
print("length =", len(h))
print("min =", min(h))
print("max =", max(h))
print("sum =", sum(h))
print("sorted =", sorted(h))    # sorted(h) returns a new list. Note that set is an unordered collection.
# for i in range(len(h)): print(h[i])     # Error as set is unindexed

print("\n# Adding elements")
# Add an element
item = 4
h.add(item)
print(f"h after adding an element: {item} =>", end = ' ')
for x in h: print(x, end=' ')
print()

# Add multiple elements
items = [3, 3, 4, 5, 6]
h.update(items)
print(f"h after adding multiple elements: {items} =>", end = ' ')
for x in h: print(x, end=' ')
print()
