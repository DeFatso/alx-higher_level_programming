#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    """getting command line arguments"""
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]


    """ connecting to mysql server"""
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd="Farai1806.",
            db=database
            )

    """creating cursor object"""
    cursor = db.cursor()

    """executing query"""
    query = "SELECT * FROM states WHERE name LIKE 'N%'"
    cursor.execute(query)

    """ print """
    row = cursor.fetchone()

    while row is not None:
        print(row)
        row = cursor.fetchone()

    """free"""
    cursor.close()
    db.close()
