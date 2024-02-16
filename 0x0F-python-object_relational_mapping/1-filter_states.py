#!/usr/bin/python3
"""A script that lists all states
that begin with 'N' from the db passed to it"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    mydb = MySQLdb.connect(host="localhost", port=3306,
                           user=sys.argv[1], passwd=sys.argv[2],
                           db=sys.argv[3])

    cur = mydb.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    mydb.close()
