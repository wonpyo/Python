# Using the random module, we can generate pseudo-random numbers. 
# The function random() generates a random number between zero and one [0, 0.1 .. 1].  
# Numbers generated with this module are not truly random but they are enough random for most purposes.

import random as rand   # The random module provides access to functions that support many operations

print("Generate a random float number between 0 and 1:")
x = rand.random()
print(x)

print("Generate a random integer number between 1 and 100:")
x = rand.randint(1,100)
print(x)

print("Generate a random float number between 0 and 10:")
x = rand.uniform(1,10)
print(x)

print("Picking a random integer item from a list")
items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
rand.shuffle(items)
print(items)

x = rand.sample(items, 1)
print(x[0])

y = rand.sample(items, 4)
print(y)

print("Picking a random string item from a list")
items = ['Alissa', 'Alice', 'Marco', 'Melissa', 'Sandra', 'Steve']

x = rand.sample(items, 1)
print(x[0])

y = rand.sample(items, 4)
print(y)