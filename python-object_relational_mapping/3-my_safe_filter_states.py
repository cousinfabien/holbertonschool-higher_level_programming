#!/usr/bin/python3
"""
This script takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
This script is safe from MySQL injections.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    """
    Connects to the database and filters states by user input safely.
    Uses parameterized queries to prevent SQL injection attacks.
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

    # Creating a cursor object to interact with the database
    cursor = db.cursor()

    # SAFE WAY: Use a placeholder (%s) for the user input.
    # The second argument of execute() must be a tuple containing the data.
    # MySQLdb handles the escaping and quoting automatically.
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    
    # Note: (state_name,) is a tuple with a single element
    cursor.execute(query, (state_name,))

    # Fetching all results from the executed query
    query_rows = cursor.fetchall()

    # Printing each row in the required format
    for row in query_rows:
        print(row)

    # Closing the cursor and the connection to free resources
    cursor.close()
    db.close()
