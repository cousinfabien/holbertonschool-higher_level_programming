#!/usr/bin/python3
"""
This script deletes all State objects with a name containing the letter 'a'
from the database hbtn_0e_6_usa.
It uses SQLAlchemy and connects to a MySQL server at port 3306.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """
    Connects to the database and deletes states based on a name filter.
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

    # Query all states containing 'a' and delete them
    # synchronize_session='fetch' ensures the session stays in sync
    session.query(State).filter(State.name.contains('a')).delete(
        synchronize_session='fetch'
    )

    # Commit the changes to the database
    session.commit()

    # Close the session
    session.close()
