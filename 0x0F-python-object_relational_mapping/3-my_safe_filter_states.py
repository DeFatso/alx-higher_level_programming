#!/usr/bin/python3
"""takes in an argument and displays all values in the states"""
import MySQLdb
import sys

if __name__ == "__main__":
    """getting command line arguments"""
    username, password, database, = sys.argv[1], sys.argv[2], sys.argv[3]
    state = sys.argv[4]

    """ connecting to mysql server"""
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database,
            )

    """creating cursor object"""
    cursor = db.cursor()

    """executing query"""
    query = "SELECT * FROM states WHERE name = %s ORDER BY id"
    cursor.execute(query, (state))

    """ print """
    row = cursor.fetchone()

    while row is not None:
        print(row)
        row = cursor.fetchone()

    """free"""
    cursor.close()
    db.close()#!/usr/bin/python3
