#!/usr/bin/python3
"""
This script takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
It takes 4 arguments: mysql username, password, database name,
and state name searched.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    """
    Connects to the database and filters states based on the 4th argument.
    The results are sorted by states.id in ascending order.
    """
    # Database connection parameters from command line arguments
    db_user = sys.argv[1]
    db_pass = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

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

    # Using format to create the SQL query as requested
    # Note: This is generally unsafe, but required for this specific task
    query = "SELECT * FROM states WHERE name = '{}' \
ORDER BY states.id ASC".format(state_name)

    # Executing the formatted query
    cursor.execute(query)

    # Fetching all results
    query_rows = cursor.fetchall()

    # Printing results in the required format
    for row in query_rows:
        print(row)

    # Closing resources
    cursor.close()
    db.close()
