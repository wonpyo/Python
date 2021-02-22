"""
A thread is an operating system process with different features than a normal process:
1. Threads exist as a subset of a process
2. Threads share memory and resources
3. Processes have a different address space in memory

When would you use threading?
Usually when you want a function to occur at the same time as your program.
If you want the server not only listens to one connection but to many connections.
In short, threads enable programs to execute multiple tasks at once.
"""

from threading import *
import time

print("Example #1: Create and start 10 threads")
class MyThread(threading.Thread):
    def __init__(self, x):  # constructor
        self.__x = x
        threading.Thread.__init__(self)

    def run(self):
        print(str(self.__x))

# Start 10 threads: Threads do not have to stop if run once
for x in range(10):
    MyThread(x).start()

print()
print("Example #2: Timed threads")
def hello():
    print("Hello Python!")

# Create timed thread by instantiating Timer class
t = Timer(10.0, hello())

# Start the thread after 10 seconds
t.start()

print()
print("Example #3: Repeat functionality using threads")
def handleClient1():
    while(True):
        print("Waiting for client 1...")
        time.sleep(5)   # Wait for 5 seconds

def handleClient2():
    while(True):
        print("Waiting for client 2...")
        time.sleep(5)   # Wait for 5 seconds

# Create timed threads
t1 = Timer(5.0, handleClient1())
t2 = Timer(3.0, handleClient2())

# Start threads
t1.start()      
t2.start()  

