# A dictionary can be thought of as an unordered set of key:value pairs.
# A pair of braces creates an empty dictionary: {}.
# Each element can map to a certain value.
# An integer or string can be used for the index.
# Dictionary do not have an order.

words = {}
words["Hello"] = "Bonjour"
words["Yes"] = "Oui"
words["No"] = "Non"
words["Bye"] = "Au Revoir"

print(words)
print(words["Hello"])
print(words["No"])

print()
dict = {}
dict['Ford'] = "Car"
dict['Python'] = "The Python Programming Language"
dict[2] = "This sentence is stored here."

print(dict)
print(dict['Ford'])
print(dict['Python'])
print(dict[2])

# Manipulating the dictionary
print()
print(words)
del words["Yes"]        # delete a key/value pair
print(words)
words["Yes"] = "Oui"    # add a new key/value pair
print(words)