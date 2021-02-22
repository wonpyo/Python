y = 10
x = int(input("Enter a number: "))

if (x < y):
    print(x, "is smaller than", y)
    # print(str(x) + " is smaller than " + str(y))
    # print("{x} is smaller than {y}")
else:
    print(x, "is greater than or equal to", y)
    # print(str(x) + " is greater than or equal to " + str(y))
    # print("{x} is greater than or equal to {y}")

print()     # Print an empty line
guess = 24
if guess > 10 and guess < 20:
    print("In range")
else:
    print("Out of range")
print('')     # Print an empty line