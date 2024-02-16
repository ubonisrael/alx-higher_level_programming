#!/usr/bin/python3
""" a script that lists all cities
from the database hbtn_0e_4_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    mydb = MySQLdb.connect(host="localhost", port=3306,
                           user=sys.argv[1], passwd=sys.argv[2],
                           db=sys.argv[3])

    cur = mydb.cursor()

    query = "SELECT name FROM cities WHERE state_id = \
        (SELECT id FROM states WHERE name = %s) ORDER BY id"
    cur.execute(query, (sys.argv[4],))
    rows = cur.fetchall()
    length = len(rows)
    if length > 0:
        for row in rows:
            print(row[0], end='')
            length -= 1
            if length > 0:
                print(', ', end='')
            else:
                print()
    else:
        print()
    cur.close()
    mydb.close()
