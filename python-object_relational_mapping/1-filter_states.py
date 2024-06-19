#!/usr/bin/python3
"""
 lists all states with a name starting with N 
 (upper N) from the database hbtn_0e_0_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":

    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()  # create a cursor
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")
    # execute the query to select all records from
    # the states table where the name starts with N
    states = cursor.fetchall()
    for state in states:  # iterates (state) in the states list
        print(state)
        # prints each state which represents a row from the states table
        