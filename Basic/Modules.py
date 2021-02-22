# Software can quickly scale into a large code base. To manage complexity we can use classes, functions and modules.

import sys

print("# Show accessible functions in a module")
# Show the accessible functions (and included variables) in a module
# for item in dir(sys): print(item)
print("sys.maxsize =", sys.maxsize)
print("sys.version =", sys.version)
print("sys.winver =", sys.winver)
print("sys.platform =", sys.platform)
# print("sys.path =", sys.path)

print("\n# Create a custom module")
import wonpyo
wonpyo.world()
for item in dir(wonpyo): print(item)

