# Importing Dataset
# Data Visualization - Introduction and Data Import: https://www.edugrad.com/tutorials/learn-data-visualization-using-python/12
# Python Pandas read_csv – Load Data from CSV Files: https://www.shanelynn.ie/python-pandas-read_csv-load-data-from-csv-files/

'''
The first step is to read the data. The data is stored as a comma-separated value, or CSV file, 
where each row is separated by a new line, and each column by a comma (,). 
In order to be able to work with the data in Python, it is needed to read the CSV file into a Pandas DataFrame. 
A DataFrame is a way to represent and work with tabular data. Tabular data has rows and columns, just like this CSV file.
'''

# Import the pandas library, renamed as pd
import pandas as pd
import os.path

filepath = "../Sample/"
filename = os.path.join(filepath, "iris.csv")

# Read IND_data.csv into a DataFrame, assigned to df
# df = pd.read_csv("IND_data.csv")
df = pd.read_csv(filename)

# Preview the first 5 rows of the data frame as default
df.head()

# Print number of rows and columns of the data frame
# df.shape()