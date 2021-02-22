# Given an array of random numbers, push all the zero’s of a given array to the end and front of the array respectively
# https://www.geeksforgeeks.org/move-zeroes-end-array/
# https://www.geeksforgeeks.org/move-all-zeros-to-start-and-ones-to-end-in-an-array-of-random-integers/?ref=rp

from colorama import Fore, Back, Style

# Function to push all zeros to the end of the list
def PushZerosToListEnd(a, n):
    count = 0

    for i in range(n):
        if a[i] != 0:
            a[count] = a[i]
            count += 1

    while count < n:
        a[count] = 0
        count += 1

# Function to push all zeros to the end of the list
def PushZerosToListFront(a, n):
    count = n - 1

    for i in range(n-1, -1, -1):
        if a[i] != 0:
            a[count] = a[i]
            count -= 1

    while count >= 0:
        a[count] = 0
        count -= 1


# Driver code
a = [0, 6, 2, 0, 4, -7, 0, -1, 9, 0]
n = len(a)

print(f"a = {a}")

print(Fore.CYAN + "Push all the zero’s to the end of the array:" + Style.RESET_ALL)
PushZerosToListEnd(a, n)
print(f"a = {a}")

print(Fore.CYAN + "Push all the zero’s to the front of the array:" + Style.RESET_ALL)
PushZerosToListFront(a, n)
print(f"a = {a}")
