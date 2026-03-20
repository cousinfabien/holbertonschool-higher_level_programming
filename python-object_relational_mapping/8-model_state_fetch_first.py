#!/usr/bin/python3
"""
This script prints the first State object from the database hbtn_0e_6_usa.
It connects to a MySQL server running on localhost at port 3306.
If the states table is empty, it prints 'Nothing'.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """
    Connects to the database and retrieves the first record from 'states'.
    Results are ordered by states.id.
    """
    # Create the engine using the command line arguments
    # Dialect: mysql+mysqldb
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Instantiate the session
    session = Session()

    # Query the first State object, ordered by id
    # .first() returns None if no result is found
    state = session.query(State).order_by(State.id).first()

    # Logic to handle empty tables as per the requirement
    if state is None:
        print("Nothing")
    else:
        print("{}: {}".format(state.id, state.name))

    # Close the session to release connection resources
    session.close()
