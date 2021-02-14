# Import module
import pyodbc
# Import datetime class from Python's datetime module
from datetime import datetime

server = 'localhost'
database = 'MDI'

# Connect to a database
connString = 'Driver={ODBC Driver 17 for SQL Server};Server=' + server + ';Database=' + database + ';Trusted_Connection=Yes'
conn = pyodbc.connect(connString)

# Create a cursor
cur = conn.cursor()

query = "SELECT COUNT(1) AS TotalRows FROM MDI.stg.Vendor"
before = datetime.now()
# now = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
with cur.execute(query):
    after = datetime.now()
    delta = after - before
    for row in cur:
        print('Total number of rows:', str(row[0]))
    print('Query time:', delta.microseconds, 'ms')
