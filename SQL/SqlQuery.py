# Import module
import pyodbc
import sys

conn = None

server = 'localhost'
database = 'MDI'

# Connect to a database
connString = 'Driver={ODBC Driver 17 for SQL Server};Server=' + server + ';Database=' + database + ';Trusted_Connection=Yes'

print("Example #1: SQL query with try/except/finally block")
try:
    conn = pyodbc.connect(connString)
    cur = conn.cursor()
    query = "SELECT @@VERSION"
    cur.execute(query)
    data = cur.fetchone()
    print("SQL version: " + str(data))
except Exception as e:
    print("Error: " + str(e.args[0]))
    sys.exit(1)
finally:
    if conn:
        conn.close()

print()

print("Example #2: SQL query")
conn = pyodbc.connect(connString)

with conn:
    cur = conn.cursor()
    query = "SELECT TOP 5 BatchLoadedID FROM MDI.dbo.BatchLoaded ORDER BY RunDateTime DESC"
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
