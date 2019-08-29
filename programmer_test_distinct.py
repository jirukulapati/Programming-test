import sqlite3

#connect to the data base using connect method
db = sqlite3.connect("testdb.db")
cur = db.cursor()

#run an SQL query to find 10 people who have visited the most sites, insert it into frequent browsers
#this query below only counts distinct sites visited by each person.
cur.execute('''INSERT INTO frequent_browsers SELECT personID, COUNT(DISTINCT siteID) FROM visits GROUP BY personID ORDER BY COUNT(DISTINCT siteID)DESC LIMIT 10''')
#db.commit()
cur.execute('''SELECT * FROM frequent_browsers''')


#Print the table Here's the header
a = ""
for column_name in cur.description:
    a = a + column_name[0].ljust(20)

a = a + "\n" + ('-' * 78)

# heres the rows
column_indices = range(len(cur.description))
for row in cur:
    b = ""
    for column_index in column_indices:
        b = b + str(row[column_index]).ljust(20)
    a = a + "\n" + b
print(a)
