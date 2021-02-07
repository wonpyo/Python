"""
Data Visualization is the presentation of data in graphical format. It helps people understand the significance of data 
by summarizing and presenting huge amount of data in a simple and easy-to-understand format and helps communicate information clearly and effectively.
"""

# Import pandas and matplotlib libraries
import pandas as pd
import matplotlib.pyplot as plt

# Create 2D array of table
data = [['E001', 'M', 34, 123, 'Normal', 350], 
        ['E002', 'F', 40, 114, 'Overweight', 450], 
        ['E003', 'F', 37, 135, 'Obesity', 169], 
        ['E004', 'M', 30, 139, 'Underweight', 189], 
        ['E005', 'F', 44, 117, 'Underweight', 183], 
        ['E006', 'M', 36, 121, 'Normal', 80], 
        ['E007', 'M', 32, 133, 'Obesity', 166], 
        ['E008', 'F', 26, 140, 'Normal', 120], 
        ['E009', 'M', 32, 133, 'Normal', 75], 
        ['E010', 'M', 36, 133, 'Underweight', 40]] 

# DataFrame created with the above data array
df = pd.DataFrame(data, columns = ['EMPID', 'Gender', 'Age', 'Sales', 'BMI', 'Income'])

print("Example #1: Histogram")
# Histogram is plotted for Age, Income, Sales. So these plots in the output shows frequency of each unique value for each attribute.
# Create histogram for numeric data
df.hist()
# Show plot
plt.show()

print("Example #2: Bar Chart")
# A column chart is used to show a comparison among different attributes, or it can show a comparison of items over time.
# Plot the bar chart for numeric values. A comparison will be shown between all 3 age, sales, and income
df.plot.bar()
# Plot between 2 attributes
plt.bar(df['Age'], df['Sales'])
plt.xlabel("Age")
plt.ylabel("Sales")
plt.show()

print("Example #3: Box Plot Chart")
# A box plot is a graphical representation of statistical data based on the minimum, first quartile, median, third quartile, and maximum.
# The term "box plot" comes from the fact that the graph looks like a rectangle with lines extending from the top and bottom.
# Because of the extending lines, this type of graph is sometimes called a box-and-whisker plot.
# For each numeric attribute of dataframe
df.plot.box()
plt.title('Box Plot Chart')
plt.show()

# Individual attribute box plot
plt.boxplot(df['Income'])
plt.show()

print("Example #4: Pie Chart")
# A pie chart shows a static number and how categories represent part of a whole the composition of something.
# A pie chart represents numbers in percentages, and the total sum of all segments needs to equal 100%.
plt.pie(df['Age'], labels = {"A", "B", "C", "D", "E", "F", "G", "H", "I", "J"}, autopct ='% 1.1f %%', shadow = True) 
plt.ylabel('Age')
plt.show() 

plt.pie(df['Income'], labels = {"A", "B", "C", "D", "E", "F", "G", "H", "I", "J"}, autopct ='% 1.1f %%', shadow = True) 
plt.ylabel('Income')
plt.show() 

plt.pie(df['Sales'], labels = {"A", "B", "C", "D", "E", "F", "G", "H", "I", "J"}, autopct ='% 1.1f %%', shadow = True) 
plt.ylabel('Sales')
plt.show() 

print("Example #5: Scatter Chart")
# A scatter chart shows the relationship between two different variables and it can reveal the distribion trends.
# It should be used when there are many different data points, and you want to highlight similarities in the data set.
# This is useful when looking for outliers and for understanding the distribution of your data.
# Scatter plot between income and age
plt.scatter(df['Income'], df['Age'])
plt.xlabel('Income')
plt.ylabel('Age')
plt.show()

# Scatter plot between income and sales
plt.scatter(df['Income'], df['Sales'])
plt.xlabel('Income')
plt.ylabel('Sales')
plt.show()

# Scatter plot between sales and age
plt.scatter(df['Sales'], df['Age'])
plt.xlabel('Sales')
plt.ylabel('Age')
plt.show()
