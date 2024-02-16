#!/usr/bin/python3
""" a script that lists all cities
from the database hbtn_0e_4_usa"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    mydb = MySQLdb.connect(host="localhost", port=3306,
                           user=sys.argv[1], passwd=sys.argv[2],
                           db=sys.argv[3])

    cur = mydb.cursor()

    query = "SELECT cities.id, cities.name, states.name FROM cities \
        JOIN states WHERE cities.state_id = states.id ORDER BY cities.id"
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    mydb.close()
