#!/usr/bin/python3
"""
lists all State objects that contain the letter a
from the database hbtn_0e_6_usa
"""
import MySQLdb
from sys import argv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import (create_engine)
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysqldb://{}:{}@localhost/{}'.format
            (argv[1], argv[2], argv[3], pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=eng)
    session = Session()
    s = '%a%'
    states = session.query(State).filter(State.name.like(s)).order_by(State.id)
    for state in states:
        print("{}: {}".format(state.id, state.name))
    session.close()
