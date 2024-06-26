#!/usr/bin/python3
"""
List all State objects from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Acces to the database
    """
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                        # Creates engine instance to manage
                        # connections to the database
                        .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                        # Use command line args to form database connections string
                        pool_pre_ping=True)  # tests connection for liveness
    Session = sessionmaker(bind=engine)  # Creates a 'Session' class
    
    session = Session()  # Creates a 'Session' instance
    instance = session.query(State).filter(State.name == sys.argv[4]).first()
    if instance:
        print("{}".format(instance.id))
    else:
        print("Not found")
        