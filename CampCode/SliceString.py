# Index and slice a string: https://www.digitalocean.com/community/tutorials/how-to-index-and-slice-strings-in-python-3

'''
Being able to call specific index numbers of strings, or a particular slice of a string gives us greater flexibility when working with this data type. 
Because strings, like lists and tuples, are a sequence-based data type, it can be accessed through indexing and slicing.
'''

s = "Python!"
n = len(s)
print("s =", s)
print("n =", len(s))

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

# The first index number is where the slice starts (inclusive)
# The second index number is where the slice ends (exclusive)
# To include either end of a string, omit one of the index numbers
# To print the whole string, omit the two index numbers and retain colons
# Reverse original string with negative stride
print("\n# Slicing String")
print("s[2:6] =", s[2:6])
print("s[:6] =", s[:6])
print("s[2:] =", s[2:])
print("s[-5:-1] =", s[-5:-1])
print("s[:-1] =", s[:-1])
print("s[-5:] =", s[-5:])
print(f"s[:{n}] =", s[:n])
print(f"s[-{n}:] =", s[-n:])
print("s[:] =", s[:])           # Print original string without stride: Python defaults to the stride of 1
print("s[::] =", s[::])         # Print original string with stride: Python defaults to the stride of 1

print("\n# Slicing String with Stride: Reverse original string with negative stride")
print("s[2:6:2] =", s[2:6:2])
print("s[2:6:-2] =", s[2:6:-2])
print("s[-5:-1:2] =", s[-5:-1:2])
print("s[-5:-1:-2] =", s[-5:-1:-2])
print(f"s[:{n}:2] =", s[:n:2])
print(f"s[-{n}::2] =", s[-n::2])
print(f"s[-{n}::-2] =", s[-n::-2])
print("s[::-1] =", s[::-1])     # Reverse original string with stride = -1
print("s[::-2] =", s[::-2])

print("\n# Counting Methods")
print("len(\"Let\'s print the length of this string.\") =", len("Let's print the length of this string."))
print("s.count(\"P\") =", s.count("P"))     # Case-sensitive
print("s.count(\"p\") =", s.count("p"))
print("s.find(\"!\") =", s.find("!"))       # Check to see where the first "!" occurs in the string
print()

likes = "Sammy likes to swim in the ocean, likes to spin up servers, and likes to smile."
print("likes =", likes)
print("len(likes) =", len(likes))
print("likes.count(\"likes\") =", likes.count("likes"))
print("likes.find(\"likes\") =", likes.find("likes"))           # Check to see where the first "likes" occurs in the string
print("likes.find(\"likes\", 9) =", likes.find("likes", 9))     # Check to see where the second "likes" occurs after the index number 9 in the string
# searches for the position of the sequence “likes” between the index numbers of 40 and -6. 
# Since the final parameter entered is a negative number it will be counting from the end of the original string.
print("likes.find(\"likes\", 40, -6) =", likes.find("likes", 40, -6))




