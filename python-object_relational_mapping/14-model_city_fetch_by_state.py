#!/usr/bin/python3
"""
This script prints all City objects from the database hbtn_0e_14_usa.
It joins the State and City tables to display results in the format:
<state name>: (<city id>) <city name>
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """
    Connects to the database and retrieves cities with their state names.
    Results are sorted by cities.id in ascending order.
    """
    # Engine setup
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    # Session setup
    Session = sessionmaker(bind=engine)
    session = Session()

    # Querying both State and City.
    # We join on the common ID and sort by City.id.
    results = session.query(State, City).join(City).order_by(City.id).all()

    # results is a list of tuples: (State_object, City_object)
    for state, city in results:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    # Closing resources
    session.close()
