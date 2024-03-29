#!/usr/bin/python3
"""
This module defines the State class for representing states in a database.
"""

import sys
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """
    Class representing a State in the database.

    Attributes:
        id (int): The unique identifier for the state.
        name (str): The name of the state.
        cities (relationship): Relationship to the City class.
    """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

    cities = relationship("City", back_populates="state")
