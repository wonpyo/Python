#!/user/bin/env python
import os.path

dirpath = "../Sample/"
filename = os.path.join(dirpath, "Testfile.txt")
# filename = os.path.join(dirpath, "Readme.txt")
# filename = "WriteFile.py"

# Check if the file does exist
if not os.path.isfile(filename):
    print("File does not exist!")
else:
    with open(filename) as f:               # Open the file as f
        # content = f.readlines()           # The function readlines() reads the file
        content = f.read().splitlines()     # The function splitlines() if you don't want to read the newline character '\n'

    # Show the file contents line by line.
    # We added the comma to print single newlines and not double newlines.
    # This is because the lines contains the newline character '\n'.
    for line in content:
        # print(line),
        print(line)