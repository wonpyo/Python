# https://pythonspot.com/python-lists/
# https://www.geeksforgeeks.org/print-colors-python-terminal/
# https://www.geeksforgeeks.org/print-lists-in-python-4-different-ways/

from colorama import Fore, Back, Style

print("\n# Initialize")
list = [ "Wonpyo", "Diane" ]
print(type(list))
print(list)
print(list[0])
print(list[1])

print("\n# Sort")
print(list)
list.sort()     # Sort the list in alphabetical order
print(list)
list.reverse()  # Reverse the order
print(list)

print('\n# Add/Remove')
print(list)
list.append("Taewoo")
print(list)
list.remove("Wonpyo")
print(list)
list.remove("Diane")
print(list)
list.remove("Taewoo")
print(list)

