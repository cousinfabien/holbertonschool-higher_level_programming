#!/usr/bin/python3
"""
This script prints the State object with the name passed as an argument
from the database hbtn_0e_6_usa.
It is safe from SQL injection and uses SQLAlchemy.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """
    Connects to the database and searches for a specific state name.
    If found, displays the state's id; otherwise, prints 'Not found'.
    """
    # Create the engine using credentials and DB name from arguments
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    # Create a configured "Session" class and instantiate it
    Session = sessionmaker(bind=engine)
    session = Session()

    # The state name to search is the 4th argument
    state_name_to_find = sys.argv[4]

    # Fixed: Query wrapped in parentheses to avoid E501 line length error
    state = session.query(State).filter(
        State.name == state_name_to_find
    ).first()

    # Check if the state was found
    if state is None:
        print("Not found")
    else:
        print("{}".format(state.id))

    # Close the session
    session.close()
