"""
You may want to split a complex problem into several smaller ones. 
You are already familiar with loops or iterations. In some situations recursion may be a better solution.
In Python, a function is recursive if it calls itself and has a termination condition. 
Why a termination condition? To stop the function from calling itself infinitely.
"""

print("Example #1: Sum Iterative")
def sumi(list):
    sum = 0
    # Add every number in the list
    for i in range(0, len(list)):
        sum = sum + list[i]
    # Return the sum
    return sum

print(sumi([5, 7, 3, 8, 10]))    

print()

# If the length of the list is one it returns the list (the termination condition). 
# Else, it returns the element and a call to the function sum() minus one element of the list. 
# If all calls are executed, it returns reaches the termination condition and returns the answer.
print("Example #2: Sum Recursive")
def sumr(list):
    if len(list) == 1:
        return list[0]
    else:
        return list[0] + sumr(list[1:])  # list[1:]: returns the items from index 1 (the second item) to the end

print(sumr([5, 7, 3, 8, 10]))    

print()

# When calling the factorial function n = 3. Thus it returns n * factorial(n-1).  
# This process will continue until n = 1. If n==1 is reached, it will return the result.
print("Example #3: Factorial Recursive")
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(3))

"""
Everytime a function calls itself and stores some memory. Thus, a recursive function could hold much more memory than a traditional function. 
Python stops the function calls after a depth of 1000 calls.
RecursionError: maximum recursion depth exceeded in comparison
print(factorial(3000))

You can resolve this by modifying the number of recursion calls such as:
import sys
sys.setrecursionlimit(5000)
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(3000))

But keep in mind there is still a limit to the input for the factorial function. For this reason, you should use recursion wisely. 
As you learned now for the factorial problem, a recursive function is not the best solution.  
For other problems such as traversing a directory, recursion may be a good solution.
"""
