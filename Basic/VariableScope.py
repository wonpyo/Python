# Variables can only reach the area in which they are defined, which is called scope. Think of it as the area of code where variables can be used. 
# Python supports global variables (usable in the entire program) and local variables.
# By default, all variables declared in a function are local variables. To access a global variable inside a function, it’s required to explicitly define ‘global variable’.

print("[Local Variable]\n")
def sum(x,y):
    sum = x + y
    return sum

print(sum(8,6))
# print(x)    # Local variables cannot be used outside of their scope, this line will not work

print()

def f(x,y):
    print('You called f(x,y) with the value x = ' + str(x) + ' and y = ' + str(y))
    print('x * y = ' + str(x*y))
    z = 4   # local variable
    print('Local variable z = ' + str(z))

z = 3   # global variable
f(3,2)
print('Global variable z = ' + str(z))

print()

print("[Global Variable]\n")
z = 10
def afunction():
    global z
    z = 9

afunction()
print("z = " + str(z))

print('')

z = 10
print("z = " + str(z))

def func1():
    global z
    z = 3

def func2(x,y):
    global z
    return x+y+z

func1()
print("z = " + str(z))
total = func2(4,5)
print("total = ", total)

