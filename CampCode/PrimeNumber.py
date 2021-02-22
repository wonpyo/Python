# A prime number is a number greater than 1 that cannot be divided by any other number except 1 and itself
# https://stackoverflow.com/questions/15963707/python-displays-all-of-the-prime-numbers-from-1-through-100

import random as rand   # The random module provides access to functions that support many operations
from colorama import Fore, Back, Style

# Function to check prime number: function should be located before its caller
def IsPrimeNumber(n):
    if n <= 1:
        return False
    for x in range(2, int(n/2+1)):
        if n % x == 0:
            return False

    return True

# Driver code
print(Fore.YELLOW + "A prime number is a number greater than 1 that cannot be divided by any other number except 1 and itself\n" + Style.RESET_ALL)
print(Fore.CYAN + "Generate a random integer number between 50 and 100:" + Style.RESET_ALL)
k = rand.randint(50, 100)
print(f"k = rand.randint(50, 100) = {k}")
print(Fore.CYAN + f"List of prime numbers between 0 - {k}:" + Style.RESET_ALL)

list = []
for n in range(1, k+1):
    if IsPrimeNumber(n):
        list.append(n)

print(f"{list}")


