#!/usr/bin/python3
"""
This script lists all State objects from the database hbtn_0e_6_usa.
It uses SQLAlchemy to perform the query and sorts by states.id.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """
    Connects to the MySQL server and retrieves all State objects.
    Displays the results in the format: <id>: <name>.
    """
    # Create the engine to connect to the MySQL server
    # Format: mysql+mysqldb://user:password@host:port/database
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session instance
    session = Session()

    # Query all State objects, ordered by their id
    # This replaces the raw SQL "SELECT * FROM states ORDER BY id ASC"
    states = session.query(State).order_by(State.id).all()

    # Display the results
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()
