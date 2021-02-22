# The range() function returns of generates a sequence of numbers, starting from the lower bound to the upper bound.
# range(lower_bound, upper_bound, step_size)
# lower_bound: The starting value of the list.
# upper_bound: The max value of the list, excluding this number.
# step_bound: The step size, the difference between each number in the list.

print("[A sequence of numbers]")
for i in range(1,10):
    print(i, end=' ')
print()

print("[Even numbers]")
for even in range(2,10,2):
    print(even, end=' ')
print()

print("[Odd numbers]")
for odd in range(1,10,2):
    print(odd, end=' ')
print()

