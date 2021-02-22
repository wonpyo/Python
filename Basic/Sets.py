# Set is a collection of unique objects.
# They are different from lists and tuples in that they are modeled after sets in mathematics.

print("Example #1: set basic methods")

print("\n# Create a set using set() function")
x = set(["Postcard", "Radio", "Telegram", "Postcard"])
print("x =", x)

# y is a simplified notation for x
y = {"Postcard", "Radio", "Telegram", "Postcard"}
print("y =", y)

item = "Telephone"
print("\n# Add an element to the set:", item)
x.add(item)
print("x =", x)

item = "Radio"
print("\n# Remove an element to the set:", item)
x.remove(item)
print("x =", x)

print("\n# Find the difference between two sets")
s1 = set(["Postcard", "Radio", "Telegram"])
s2 = set(["Radio","Television"])
print("s1 =", s1)
print("s2 =", s2)
print("s1.difference(s2) =", s1.difference(s2))
print("s2.difference(s1) =", s2.difference(s1))

print("\n# Remove all elements from the set")
x.clear()
print("x =", x)

print()
print("Example #2: set test methods")

print("\n# Test sets")
x = set(["a", "b", "c", "d"])
y = set(["c", "d"])
print("x =", x)
print("y =", y)

print("\n# Test if a set is a subset")
print("x.issubset(y) =", x.issubset(y))
print("y.issubset(x) =", y.issubset(x))

print("\n# Test if a set is a superset")
print("x.issuperset(y) =", x.issuperset(y))
print("y.issuperset(x) =", y.issuperset(x))

print("\n# Test for intersection")
print("x.intersection(y) =", x.intersection(y))






