#!/usr/bin/python3
"""
This script adds the State object
`Louisiana` to the database `hbtn_0e_6_usa`.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access to the database and add the State object `Louisiana`
    """
    # Create a new Engine instance
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    # Create all tables in the database
    Base.metadata.create_all(engine)
    # Create a new session
    Session = sessionmaker(bind=engine)
    session = Session()
    # Add the State object `Louisiana` to the session
    new_state = State(name='Louisiana')
    session.add(new_state)
    # Commit the session to the database
    session.commit()
    # Print the id of the new State object
    print(new_state.id)
    # Close the session
    session.close()
    