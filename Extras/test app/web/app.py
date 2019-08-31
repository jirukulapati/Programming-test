from flask import Flask, request
import sqlite3
import pandas as pd

import sqlite3
app = Flask(__name__)

@app.route('/')
#connect to the data base using connect method
def startprogram():
    return("Executed Successfully!!  Try making a request from the command line!")
    
@app.route('/result', methods = ['GET'])
def result():
    con = sqlite3.connect("testdb.db")
    cur = con.cursor()
    cur.execute('''INSERT INTO frequent_browsers SELECT personID, COUNT(DISTINCT siteID) FROM visits GROUP BY personID ORDER BY COUNT(DISTINCT siteID)DESC LIMIT 10''')
    #db.commit()
    #used Pandas here because it's easier to print the results with pandas than with sqlite
    df = pd.read_sql_query("SELECT * FROM frequent_browsers", con)
    return(df.to_string(index=False))


    
    
