#!/usr/bin/python3
"""takes in an argument and displays all values in the states"""
import MySQLdb
import sys


def list_cities_by_state(username, password, database, state_name):
    """getting command line arguments"""

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
    query = "SELECT cities.name FROM cities \
            JOIN states ON cities.state_id = states.id WHERE states.name = %s \
            ORDER BY cities.id"
    cursor.execute(query, (state_name,))

    """ print """
    row = cursor.fetchone()

    while row is not None:
        print(row)
        row = cursor.fetchone()

    """free"""
    cursor.close()
    db.close()


if __name__ == "__main__":
    username, password, database, state_name = sys.argv[1], sys.argv[2], \
            sys.argv[3], sys.argv[4]
    list_cities_by_state(username, "Farai1806.", database, state_name)
