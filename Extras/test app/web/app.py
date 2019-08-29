from flask import Flask, request
import sqlite3

import sqlite3
app = Flask(__name__)

@app.route('/')
#connect to the data base using connect method
def startprogram():
    return("Executed Successfully!!  Try making a request from the command line!")
    
@app.route('/result', methods = ['GET'])
def result():
    db = sqlite3.connect("testdb.db")
    cur = db.cursor()
    cur.execute("INSERT INTO frequent_browsers SELECT personID, COUNT(*) FROM visits GROUP BY personID ORDER BY COUNT(*)DESC LIMIT 10")
    cur.execute("SELECT * FROM frequent_browsers")
    a = ""
    for column_name in cur.description:
        a = a + column_name[0].ljust(20)
    
    a = a + "\n" + ('-' * 78)

#heres the rows
    column_indices = range(len(cur.description))
    for row in cur:
        b = ""
        for column_index in column_indices:
            b = b + str(row[column_index]).ljust(20)
        a = a +"\n"+ b
    return(a)

    
    