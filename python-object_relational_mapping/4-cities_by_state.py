#!/usr/bin/python3
"""
This script lists all cities from the database hbtn_0e_4_usa.
It performs a JOIN between the cities and states tables.
The script takes 3 arguments: mysql username, password, and database name.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    """
    Connects to the database and retrieves cities with their state names.
    The query uses a JOIN to link the tables via state_id.
    """
    # Database connection parameters from command line arguments
    db_user = sys.argv[1]
    db_pass = sys.argv[2]
    db_name = sys.argv[3]

    # Establishing the connection to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=db_user,
        passwd=db_pass,
        db=db_name
    )

    # Creating a cursor object
    cursor = db.cursor()

    # Executing the JOIN query in a single call
    # We select cities.id, cities.name, and states.name
    # We join cities.state_id with states.id
    query = "SELECT cities.id, cities.name, states.name \
FROM cities \
JOIN states ON cities.state_id = states.id \
ORDER BY cities.id ASC"

    cursor.execute(query)

    # Fetching all results
    query_rows = cursor.fetchall()

    # Printing each row in the format (city_id, city_name, state_name)
    for row in query_rows:
        print(row)

    # Closing resources
    cursor.close()
    db.close()
