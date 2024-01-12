#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    """getting command line arguments"""
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    """connecting to MySQL server"""
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=password,
            passwd=password,
            db=database
            )

    """creating cursor object"""
    cursor = db.cursor()

    """executing the query"""
    query = "SELECT * FROM states ORDER BY id"
    cursor.execute(query)

    """get all rows"""
    rows = cursor.fetchall()

    """print"""
    for row in rows:
        print(row)

    """close"""
    cursor.close()
    db.close()
