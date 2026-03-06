#!/usr/bin/python3
"""
This module contains the class definition of a City.
It inherits from Base (imported from model_state) and links
to the MySQL table 'cities'.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """
    City class that inherits from Base.
    Links to the MySQL table 'cities'.
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    # Foreign Key links cities.state_id to states.id
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
