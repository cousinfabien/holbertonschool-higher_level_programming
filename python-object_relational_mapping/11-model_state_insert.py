#!/usr/bin/python3
"""
This script adds the State object "Louisiana" to the database hbtn_0e_6_usa.
It uses SQLAlchemy and prints the new states.id after creation.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """
    Connects to the database and adds a new State record.
    Displays the id of the newly created state.
    """
    # Create the engine using the command line arguments
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    # Create a configured "Session" class and instantiate it
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create a new instance of the State class
    new_state = State(name="Louisiana")

    # Add the object to the session
    session.add(new_state)

    # Commit the transaction to the database
    # This is where the INSERT SQL command is actually executed
    session.commit()

    # After commit, the new_state object is updated with its new ID from MySQL
    print("{}".format(new_state.id))

    # Close the session
    session.close()
