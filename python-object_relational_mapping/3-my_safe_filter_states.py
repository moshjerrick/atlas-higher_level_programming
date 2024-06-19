#!/usr/bin/python3
"""
Taking in arguements and displaying all values in
states table of hbtn_0e_0_usa where name matches the argument
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY \
        '{}' ORDER BY id".format(sys.argv[4]))
    state = cursor.fetchall()
    if state is not None:
        for states in state:
            print(states)
