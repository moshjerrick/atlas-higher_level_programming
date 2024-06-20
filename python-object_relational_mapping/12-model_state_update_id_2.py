#!/usr/bin/python3
"""


"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
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
    # Update the State object with id 2 to `New Mexico`
    state = session.query(State).filter(State.id == 2).first()
    state.name = 'New Mexico'
    # Commit the session to the database
    session.commit()
    # Close the session
    session.close()
    