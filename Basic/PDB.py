# PDB: The Python Debugger - https://docs.python.org/3/library/pdb.html
# The module pdb supports setting breakpoints. 
# A breakpoint is an intentional pause of the program. where you can get more information about the programs state.
# To set a breakpoint, insert the line: pdb.set_trace()
# set_trace(): Enter the debugger at the calling stack frame. 
# This is useful to hard-code a breakpoint at a given point in a program, 
# even if the code is not otherwise being debugged (e.g. when an assertion fails). 
# If given, header is printed to the console just before debugging begins.

# import pdb

x = 3
y = 4

# pdb.set_trace() 
total = x + y
# pdb.set_trace()

"""
PS C:\Python> py -m pdb .\PDB.py
> c:\python\pdb.py(12)<module>()
-> x = 3
(Pdb) b 16
Breakpoint 1 at c:\python\pdb.py:16
(Pdb) l
  7     # even if the code is not otherwise being debugged (e.g. when an assertion fails).
  8     # If given, header is printed to the console just before debugging begins.
  9
 10     # import pdb
 11
 12  -> x = 3
 13     y = 4
 14
 15     # pdb.set_trace()
 16 B   total = x + y
 17     # pdb.set_trace()
(Pdb) w
  c:\users\rheew\appdata\local\programs\python\python38-32\lib\bdb.py(587)run()
-> exec(cmd, globals, locals)
  <string>(1)<module>()
> c:\python\pdb.py(12)<module>()
-> x = 3
(Pdb) b
Num Type         Disp Enb   Where
1   breakpoint   keep yes   at c:\python\pdb.py:16
(Pdb) c
> c:\python\pdb.py(16)<module>()
-> total = x + y
(Pdb) x
3
(Pdb) y
4
(Pdb) total
*** NameError: name 'total' is not defined
(Pdb) c
--Return--
> c:\python\pdb.py(16)<module>()->None
-> total = x + y
(Pdb) w
> c:\python\pdb.py(16)<module>()->None
-> total = x + y
(Pdb) total
7
(Pdb) q
PS C:\Python>
"""
