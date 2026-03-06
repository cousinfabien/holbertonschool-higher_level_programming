#!/usr/bin/python3
"""
This module lists all State objects that contain the letter 'a'
from the database hbtn_0e_6_usa.
It connects to a MySQL server running on localhost at port 3306.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """
    Connects to the database and retrieves states where the name contains 'a'.
    The results are sorted by states.id in ascending order.
    """
    # Create the engine using command line arguments
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    # Create a configured "Session" class and instantiate it
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the State objects that contain the letter 'a'
    # .contains('a') is the SQLAlchemy way to do LIKE '%a%'
    states = session.query(State).filter(
        State.name.contains('a')
    ).order_by(State.id).all()

    # Display the results in the specified format
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()
