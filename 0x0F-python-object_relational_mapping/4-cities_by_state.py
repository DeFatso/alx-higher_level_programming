#!/usr/bin/python3
"""script that lists all cities from the database"""
import MySQLdb
import sys

if __name__ == "__main__":
    """Get command line arguments"""
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    """Connect to MySQL server"""
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    """Create cursor object"""
    cursor = db.cursor()

    """Execute the query"""
    query = "SELECT cities.id, cities.name, states.name FROM cities \
             JOIN states ON cities.state_id = states.id ORDER BY cities.id"
    cursor.execute(query)

    """Fetch all rows"""
    rows = cursor.fetchall()

    """Print results"""
    for row in rows:
        print(row)

    """Close cursor and database connection"""
    cursor.close()
    db.close()
