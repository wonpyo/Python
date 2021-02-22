# subprocess module enables you to start new applications from your Python program
"""
https://stackoverflow.com/questions/9439480/from-import-vs-import

import X
Imports the module X, and creates a reference to that module in the current namespace. 
Then you need to define completed module path to access a particular attribute or method from inside the module (e.g.: X.name or X.attribute)

from X import *
Imports the module X, and creates references to all public objects defined by that module in the current namespace 
(that is, everything that doesn’t have a name starting with _) or whatever name you mentioned. 
Or, in other words, after you've run this statement, you can simply use a plain (unqualified) name to refer to things defined in module X. 
But X itself is not defined, so X.name doesn't work. And if name was already defined, it is replaced by the new version. 
And if name in X is changed to point to some other object, your module won't notice.
This makes all names from the module available in the local namespace.
"""

# Absolute import
# from subprocess import Popen, PIPE
import subprocess as p

print("Example #1: Start a process in Python")

# Start a process named notepad with 'Hello.py' parameter
process = p.Popen(['py', 'Hello.py'], stdout=PIPE, stderr=PIPE)           # Run Hello.py with py.exe: py Hello.py
# process = p.Popen(['notepad', 'Hello.py'], stdout=PIPE, stderr=PIPE)    # Open Hello.py with notepad: notepad Hello.py

# The process.communicate() call reads input and output from the process.  
# stdout is the process output. stderr will be written only if an error occurs.  
# If you want to wait for the program to finish you can call Popen.wait().
stdout, stderr = process.communicate()
print(stdout)

print()
print("Example #2: Subprocess.call() method")
p.call(["py", "Hello.py"])
# p.call(["notepad", "Hello.py"])
# p.call(["ls", "-l"])

print()
print("Example #3: Save process output")
s = p.check_output(["echo", "Hello World!"])
print("s = " + s)
