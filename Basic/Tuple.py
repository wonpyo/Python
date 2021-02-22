# The tuple data structure is used to store a group of data.  
# The elements in this group are separated by a comma. Once created, the values of a tuple cannot change.
# An empty tuple in Python would be defined as:
# tuple = ()

# A comma is required for a tuple with one item:
# tuple = (3,)

# The comma for one item may be counter intuitive,  but without the comma for a single item, you cannot access the element.  
# For multiple items, you do not have to put a comma at the end.  This set is an example:
# personInfo = ("Diana", 32, "New York")
# The data inside a tuple can be of one or more data types such as text and numbers.

'''
Tuple

Tuples are basically lists that can never be changed. 
Lists are quite dynamic; they can grow as you append and insert items, and they can shrink as you remove items. You can modify any element you want to in a list. 
Sometimes we like this behavior, but other times we may want to ensure that no user or no part of a program can change a list.
That's what tuples are for.
Technically, lists are mutable objects and tuples are immutable objects. 
Mutable objects can change (think of mutation), and immutable objects can not change.
'''

personnfo = ("Diana", 32, "New York")
print(personnfo[0])
print(personnfo[1])
print(personnfo[2])

print("[Assign multiple variables]")
name, age, country, career = ('Diana', 32, 'Canada', 'CompSci')
print(name)
print(age)
print(country)
print(career)