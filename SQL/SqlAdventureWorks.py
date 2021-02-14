"""
Create Python apps using SQL Server on Windows: https://www.microsoft.com/en-us/sql-server/developer-get-started/python/windows/
Anaconda Easy Button – Microsoft SQL Server and Python: https://www.anaconda.com/anaconda-easy-button-microsoft-sql-server-and-python/
Login failed for user DOMAIN\\user with pyodbc: https://stackoverflow.com/questions/37692780/error-28000-login-failed-for-user-domain-user-with-pyodbc

With Microsoft's ODBC drivers for SQL Server, Trusted_connection=Yes tells the driver to use "Windows Authentication" 
and your script will attempt to log in to the SQL Server using the Windows credentials of the user running the script. 
UID and PWD cannot be used to supply alternative Windows credentials in the connection string, 
so if you need to connect as some other Windows user you will need to use RUNAS to run the Python script as that other user.
If you want to use "SQL Server Authentication" with a specific SQL Server login specified by UID and PWD then use Trusted_connection=No.

We can't use sqlite3 to connect to SQL server, only to Sqlite databases. You need to use a driver that can talk to MS SQL, like pyodbc.
"""

# Import module
import pyodbc
# Import datetime class from Python's datetime module
from datetime import datetime

server = 'localhost'
database = 'AdventureWorks2012'

# Connect to a database
connString = 'Driver={ODBC Driver 17 for SQL Server};Data Source=' + server + ';Initial Catalog=' + database + ';Trusted_Connection=Yes'
# connString = 'Driver={ODBC Driver 13 for SQL Server};Server=' + server + ';Database=' + database + ';Trusted_Connection=Yes'
conn = pyodbc.connect(connString)
print()
print("Server  :", server)
print("Database:", database)
print()

# Create a cursor
# Cursors can not only be used to fetch data from the DBMS into an application 
# but also to identify a row in a table to be updated or deleted.
cur = conn.cursor()

# SELECT query
print("# Reading data from table")
tsql = "SELECT TOP 5 FirstName, LastName FROM Person.Person ORDER BY ModifiedDate DESC"
with cur.execute(tsql):
    rows = cur.fetchall()
    for row in rows:
        print(str(row[0]) + " " + str(row[1]))

print()

# # UPDATE query
# print("Updating data in table")
# tsql = "UPDATE MDI.sync.MemberConfig SET IsSyncEnabled = ?, PreSplitExcelFiles = ?, SyncAttemptCounter = ? WHERE MemberNo = ? AND DatasourceID = ?"
# with cur.execute(tsql, 1, 1, 0, 666668, 714):
#     print("Successfully updated!")

# print()

# # INSERT query
# print("Inserting data into table")
# # Python multi-line string with triple quotes
# tsql = """
# SET IDENTITY_INSERT [Web Reporting - Admin].dbo.Agency ON
# INSERT INTO [Web Reporting - Admin].dbo.Agency (AgencyID, AgencyName, isActive) VALUES (?, ?, ?)
# SET IDENTITY_INSERT [Web Reporting - Admin].dbo.Agency OFF
# """
# with cur.execute(tsql, 99999, 'Agency Test 666', 1):
#     print("Successfully inserted!")

# print()

# # DELETE query
# print("Deleting data from table")
# tsql = "DELETE FROM [Web Reporting - Admin].dbo.Agency WHERE AgencyName = ?"
# with cur.execute(tsql, 'Agency Test 666'):
#     print("Successfully deleted!")

