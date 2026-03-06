#!/usr/bin/python3
"""
This script lists all states from the database hbtn_0e_0_usa.
The script takes 3 arguments: mysql username, password, and database name.
It connects to a MySQL server running on localhost at port 3306.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    """
    Connects to the database and retrieves all states.
    The results are sorted by states.id in ascending order.
    """
    # Database connection parameters from command line arguments
    db_user = sys.argv[1]
    db_pass = sys.argv[2]
    db_name = sys.argv[3]

    # Establishing the connection to the MySQL server
    # Using host='localhost' and port=3306 as required
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=db_user,
        passwd=db_pass,
        db=db_name
    )

    # Creating a cursor object to interact with the server
    cursor = db.cursor()

    # Executing the query to fetch all states ordered by ID
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetching all results from the executed query
    query_rows = cursor.fetchall()

    # Printing each row in the format (id, name)
    for row in query_rows:
        print(row)

    # Closing the cursor and the connection to free resources
    cursor.close()
    db.close()