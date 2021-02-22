"""
We can create anonymous functions, known as lambda functions. 
Lambda functions are different from normal Python functions, they origin from Lambda Calculus. 
It allows you to write very short functions. 
"""

print("Example #1: lambda function")
f = lambda x: 2 * x
print(f(3))

# A return statements is never used in a lambda function, it always returns something. 
# A lambda functions can contain if statements:
f = lambda x: x > 10
print(f(2))
print(f(12))

print()
print("Example #2: map function")
# The definition of map is map(function,iterable). It applies a function to every item in the iteratable. 
# We can use map() to on a lambda function with a list.
# lambda functions can be used anywhere, you could use normal functions instead. A lambda function is not a statement, it is an expression. 
# lambda functions do not support a block of statements.
l = [1,2,3,4,5]
items = map(lambda x: x * x, l)
print(l)
print(*items)                   # Print items using * operator separated by space
# print(*items, sep=", ")         # Print items using * operator separated by comma
# print(*items, sep="\n")         # Print items using * operator separated by new line
# # map() function to convert each item in the list to a string if list is not a string, and then join them
# print(', '.join(map(str, items)))
# for item in items: print(item)  # Print iterator using a for loop

print()
print("Example #3: filter function")
# filter(function,iterable) creates a new list from the elements for which the lambda function returns true. 
l = [1,2,3,4,5,6,7,8,9,10]
items = filter(lambda x: x % 2 == 0, l)
print(l)
print(*items)                   # Print items using * operator separated by space
# print(*items, sep=", ")         # Print items using * operator separated by comma
# print(*items, sep="\n")         # Print items using * operator separated by new line
# # map() function to convert each item in the list to a string if list is not a string, and then join them
# print(', '.join(map(str, items)))
# for item in items: print(item)  # Print iterator using a for loop

import functools

print()
print("Example #4: reduce function")
# reduce(function, iterable) applies two arguments cumulatively to the items of iterable, from left to right.
# This function is defined in functools module.
l = [1,2,3,4,5]
sum = functools.reduce(lambda x,y: x + y, l)
print(l)
print("The sum of the list elements is: ", end="")
print(sum)
# Equivalent to the two prints above
# print("The sum of the list elements is:", sum)

l = [10,6,7,5,2,1,8,5]
max = functools.reduce(lambda x,y: x if (x > y) else y, l)
print(l)
print("The max of the list elements is: ", end="")
print(max)






