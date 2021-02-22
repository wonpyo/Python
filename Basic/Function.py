# A function is reusable code that can be called anywhere in your program. Functions improve readability of your code: 
# it’s easier for someone to understand code using functions instead of long lists of instructions.
# On top of that, functions can be reused or modified which also improve testability and extensibility.
# The def keyword tells Python we have a piece of reusable code (A function). A program can have many functions.

def f1(x):
    return(x * x)

print(f1(3))

print()
def M(x,y):
    print('You called f(x,y) with the value x = ' + str(x) + ' and y = ' + str(y))
    print('x * y = ' + str(x*y))

M(3,2)

print("\n** Nested Function")
def highFive(): return 5
def f(x,y):
    z = highFive()
    return x + y + z

result = f(3,2)
print('result =', result)


