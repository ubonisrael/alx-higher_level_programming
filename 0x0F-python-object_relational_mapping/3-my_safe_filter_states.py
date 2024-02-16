#!/usr/bin/python3
"""script that takes in an argument and displays all
values in the states table of
hbtn_0e_0_usa where name matches the argument."""

if __name__ == "__main__":
    import MySQLdb
    import sys

    mydb = MySQLdb.connect(host="localhost", port=3306,
                           user=sys.argv[1], passwd=sys.argv[2],
                           db=sys.argv[3])

    cur = mydb.cursor()

    query = "SELECT * FROM states WHERE name = %s"
    cur.execute(query, (sys.argv[4],))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    mydb.close()
