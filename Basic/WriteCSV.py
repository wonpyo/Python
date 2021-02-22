# Create and read a csv file: i.e. database files such as spreadsheet or csv by exporting and importing the data in database
# Note that the csv reader is only allowed to iterate only once. 
# => Reset the file iterator to beginning of the input file to avoid the issue.

'''
Spreadsheets often export CSV (Comma Separated Values) files, because they are easy to read and write.
A csv file simply consists of values, commas, and newlines.
While the file is called CSV file, you can use another separator such as the pipe character.
'''

import csv
import os.path

filepath = "../Sample/"
filename = os.path.join(filepath, "Persons.csv")
# filename = os.path.join(filepath, "Employees.csv")    # Employees.csv was exported from database

# Create the csv file
# Open the csv file with writing permission
# The way Python handles newlines on Windows can result in blank lines appearing between rows when using csv.writer()
# => leave the file in text mode, since you’re writing text, but disable universal newlines.
with open(filename, mode='w', newline='') as f:
    writer = csv.writer(f, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['Name', 'Profession'])
    writer.writerow(['Derek', 'Software Developer'])
    writer.writerow(['Steve', 'Software Developer'])
    writer.writerow(['Paul', 'Manager'])

# Read the csv file
# initialize lists to hold the data
names = []
jobs = []

with open(filename, mode='r') as f:
    reader = csv.reader(f)

    # Print each row of the csv file as a list: type(row) = list
    for line in reader: print(line)     

    n = 0
    f.seek(0)   # Reset the file iterator to beginning of the input file to allow it to be iterated more than once
    for row in reader:
        if n >= 1:  # Skip the header row
            names.append(row[0]) 
            jobs.append(row[1])

        n += 1      # Increase the row number

# Print data
print()
print(f"names = {names}")
print(f"jobs = {jobs}")       



