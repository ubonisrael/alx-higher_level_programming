#!/usr/bin/python3
"""A script that lists all states
that begin with 'N' from the db passed to it"""
import MySQLdb
import sys

if __name__ == "__main__":
    try:
        mydb = MySQLdb.connect(host="localhost", port=3306,
                               user=sys.argv[1], passwd=sys.argv[2],
                               db=sys.argv[3])
    except MySQLdb.Error as e:
        print("Error connecting to MySQL: {}".format(e))
        sys.exit(1)

    cur = mydb.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    mydb.close()
