import sqlite3
import pandas as pd

#connect to the data base using connect method
con = sqlite3.connect("testdb.db")
cur = con.cursor()

#run an SQL query to find 10 people who have visited the most sites, insert it into frequent browsers
#this query below counts all sites visited by each person.
cur.execute('''INSERT INTO frequent_browsers SELECT personID, COUNT(*) FROM visits GROUP BY personID ORDER BY COUNT(*)DESC LIMIT 10''')
#db.commit()
#used Pandas here because it's easier to print the results with pandas than with sqlite
df = pd.read_sql_query("SELECT * FROM frequent_browsers", con)

#Print the table Here's the header

print(df.to_string(index=False))


