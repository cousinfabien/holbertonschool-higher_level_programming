#!/usr/bin/python3
"""
This script takes in the name of a state as an argument and lists all
cities of that state, using the database hbtn_0e_4_usa.
The script is safe from MySQL injection and uses only one execute().
"""
import MySQLdb
import sys


if __name__ == "__main__":
    """
    Connects to the database and filters cities based on the state name
    provided by the user. Results are comma-separated.
    """
    # Database connection parameters from command line arguments
    db_user = sys.argv[1]
    db_pass = sys.argv[2]
    db_name = sys.argv[3]
    state_name_searched = sys.argv[4]

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

    # We join cities and states to find cities belonging to the given state.
    # We use %s to prevent SQL injection.
    query = "SELECT cities.name \
FROM cities \
JOIN states ON cities.state_id = states.id \
WHERE states.name = %s \
ORDER BY cities.id ASC"

    # Executing the JOIN query with the safe parameter
    cursor.execute(query, (state_name_searched,))

    # Fetching all results
    query_rows = cursor.fetchall()

    # The expected output is a comma-separated string of city names.
    # We use join() on a list comprehension to format the output.
    cities_list = [row[0] for row in query_rows]
    print(", ".join(cities_list))

    # Closing resources
    cursor.close()
    db.close()
