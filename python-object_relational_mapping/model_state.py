#!/usr/bin/python3
"""
This module contains the class definition of a State and an
instance Base = declarative_base().
It uses SQLAlchemy to map the class to the MySQL table 'states'.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Creating the Base class which will be inherited by our models
Base = declarative_base()


class State(Base):
    """
    State class that inherits from Base.
    Links to the MySQL table 'states'.
    """
    __tablename__ = 'states'

    # Defining the columns of the table
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
