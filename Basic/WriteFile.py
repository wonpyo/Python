# Python supports writing files by default, no special modules are required. You can write a file using the .write() method with a parameter containing text data.
# Before writing data to a file, call the open(filename,’w’) function where filename contains either the filename or the path to the filename. Finally, don’t forget to close the file.

# r
# Open file for reading
# w
# Open file for writing (will truncate file)
# b
# binary more
# r+
# open file for reading and writing
# a+
# open file for reading and writing (appends to end)
# w+
# open file for reading and writing (truncates files)

import os.path

# The code below creates a new file (or overwrites) with the data.
print("Create file for writing")

# Filename to write
dirname = "../Sample/"
filename = os.path.join(dirname, "Testfile.txt")
print(filename)

# Open the file with writing permission
myfile = open(filename, 'w')

# Write a line to the file
myfile.write('Written with Python\n')

# Close the file
myfile.close()

# If you simply want to add content to the file you can use the ‘a’ parameter.
print("\nAppend to file")

# The 'a' flag tells Python to keep the file contents and append (add line) at the end of the file
myfile = open(filename, 'a')

# Add the line
myfile.write('Appended with Python\n')

# Close the file
myfile.close()



