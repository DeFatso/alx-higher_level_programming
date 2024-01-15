#!/usr/bin/python3
"""
    Script that deletes all State objects with a name containing
    the letter a from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    """Check if the correct number of arguments is provided"""

    if len(sys.argv) != 4:
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    engine = create_engine('mysql+mysqlconnector://{}:{}@localhost:3306/{}'.
                           format(username, password, database))

    Session = sessionmaker(bind=engine)
    session = Session()

    states_to_delete = session.query(
            State).filter(State.name.like('%a%')).all()
    for state in states_to_delete:
        session.delete(state)

    session.commit()
    session.close()
