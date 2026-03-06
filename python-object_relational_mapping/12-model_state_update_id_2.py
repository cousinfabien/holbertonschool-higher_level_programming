#!/usr/bin/python3
"""
This script changes the name of a State object from the database hbtn_0e_6_usa.
It specifically updates the State where id = 2 to 'New Mexico'.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """
    Connects to the database and updates a specific State name.
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

    # Query the State object with id = 2
    # We use .filter() or .get() - filter is more common in these tasks
    state_to_update = session.query(State).filter(State.id == 2).first()

    # Check if the state exists before trying to update it
    if state_to_update:
        # Simply change the attribute
        state_to_update.name = "New Mexico"
        # Commit the change to the database
        session.commit()

    # Close the session
    session.close()
