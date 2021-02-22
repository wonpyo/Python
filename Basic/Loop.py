# Code can be repeated using a loop. Lines of code can be repeated N times, where N is manually configurable. 
# In practice, it means code will be repeated until a condition is met. This condition is usually (x >=N) but it’s not the only possible condition.
# Python has 3 types of loops: for loops, while loops and nested loops.

# We can iterate a list using a for loop
print("[For loop]")
items = ["Abby", "Brenda", "Cindy", "Wonpyo"]
for item in items:
    print(item)

print()
for i in range(1,3):
    print(i)

# If you are unsure how many times a code should be repeated, use a while loop.
print("[While loop]")
n = 5
guess = 0
while guess != n:
    guess = int(input("Guess the number: "))
    if guess != n:
        print('False guess')

print('You guessed the correct number')

# We can combine for loops using nesting. If we want to iterate over an (x,y) field we could use.
# Nesting is very useful, but it increases complexity the deeper you nest.
print("[Nested loop]")
for x in range(1,3):
    for y in range(1,3):
        print("(" + str(x) + "," + str(y) + ")")
        


