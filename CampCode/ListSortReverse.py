'''
There are four collection data types in the Python programming language:
1. List is a collection which is ordered and changeable. Allows duplicate members: e.g. l = [1,2,3], l = [] for empty list
2. Tuple is a collection which is ordered and unchangeable. Allows duplicate members: e.g. t = (1,2,3), t = () for empty tuple
3. Set is a collection which is unordered and unindexed. No duplicate members: e.g. s = {1,2,3}, s = set() for empty set
4. Dictionary is a collection which is unordered, changeable and indexed. No duplicate members: e.g. d = {"One": 1, "Two": 2, "Three": 3}, d = {} for empty dictionary

When choosing a collection type, it is useful to understand the properties of that type. 
Choosing the right type for a particular data set could mean retention of meaning, and, it could mean an increase in efficiency or security.
'''

import copy

l = [7, 2, 5, 9, 10, 4, 8, 3, 6, 1]
x = l.copy()                # Copy the actual list. Equivalent to x = l[:]
# x = l[:]                  # Copy the actual list using slice
y = l                       # This assignment just copies the reference (address by pointer) to the list, not the actual list, so both refers to the same list 
z = copy.deepcopy(l)        # Copy the actual list in case that the list contains objects
print("l =", l)
print("x =", x)
print("y =", y)
print("z =", z)

print()
list.sort(l)                # list.sort(l) only changes y list
print("list.sort(l) =", l)

l = x.copy()                # Revert list back to original
print("l =", l)
l.sort()                    # Equivalent to l.sort(reverse=False), by default, reverse = False
print("l.sort() =", l)  
l.reverse()                 # Equivalent to l.sort(reverse=True)
print("l.reverse() =", l)
print()

print("l =", l)
print("x =", x)
print("y =", y)
print("z =", z)         


