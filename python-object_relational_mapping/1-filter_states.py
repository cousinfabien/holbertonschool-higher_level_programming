#!/usr/bin/python3
"""
This script lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa.
It takes 3 arguments: mysql username, password, and database name.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    """
    Connects to the database and filters states starting with a capital 'N'.
    The results are sorted by states.id in ascending order.
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

    # Creating a cursor object to interact with the database
    cursor = db.cursor()

    # The BINARY keyword ensures the search is case-sensitive for 'N'
    # We use a backslash to keep the line under 80 characters for pycodestyle
    query = "SELECT * FROM states WHERE name LIKE BINARY 'N%' \
ORDER BY states.id ASC"
    
    # Executing the SQL query
    cursor.execute(query)

    # Fetching all filtered rows
    query_rows = cursor.fetchall()

    # Printing each row in the required format
    for row in query_rows:
        print(row)

    # Closing the cursor and the connection
    cursor.close()
    db.close()
