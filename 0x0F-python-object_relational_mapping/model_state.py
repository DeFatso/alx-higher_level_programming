#!/usr/bin/python3
"""file that contains the class definition of a State"""

import sys
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """inherits from Base"""

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

    cities = relationship("City", back_populates="state")


username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

engine = create_engine('mysql://{}:{}@localhost:3306/{}'.
                       format(username, password, database),
                       pool_pre_ping=True)

Base.metadata.create_all(engine)
