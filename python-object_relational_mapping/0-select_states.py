#!/usr/bin/python3
"""
This module lists all states from the database hbtn_0e_0_usa.
It connects to a MySQL server running on localhost at port 3306.
The script takes 3 arguments: mysql username, password, and database name.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    """
    Accesses the database and gets the states from the states table.
    """
    # Get arguments from the command line
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_user,
        passwd=mysql_password,
        db=db_name
    )

    # Create a cursor object to execute queries
    cursor = db.cursor()

    # Execute the SQL query to fetch all states sorted by id
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows from the last executed statement
    rows = cursor.fetchall()

    # Display the results as tuples
    for row in rows:
        print(row)

    # Close the cursor and the database connection
    cursor.close()
    db.close()
    