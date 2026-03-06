#!/usr/bin/python3
"""
This script takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
It uses MySQLdb and the format() method for the query.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    """
    Connects to the database and filters states based on the 4th argument.
    The results are sorted by states.id in ascending order.
    """
    # Database connection parameters
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Creating the cursor
    cursor = db.cursor()

    # The issue often comes from how the string is formatted.
    # We must ensure the argument is treated as a string in SQL.
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(
        sys.argv[4]
    )

    # Executing the formatted query
    cursor.execute(query)

    # Fetching all results
    query_rows = cursor.fetchall()

    # Display results
    for row in query_rows:
        print(row)

    # Closing resources
    cursor.close()
    db.close()
