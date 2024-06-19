#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa
"""


import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor() # create a cursor
    cursor.execute("SELECT * FROM 'states;'") # execute the query to select all records from the states table
    states = cursor.fetchall() # fetch all the records and store in states variable
    for state in states: # iterates (state) in the states list
        print(state) # prints each state which represents a row from the states table
