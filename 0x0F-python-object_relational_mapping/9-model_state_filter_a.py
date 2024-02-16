#!/usr/bin/python3
"""contains the class definition of a State and an instance Base"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    port = 3306
    host = "localhost"
    connection_string = "mysql+mysqldb://{}:{}@{}:{}/{}".format(
        sys.argv[1], sys.argv[2], host, port, sys.argv[3])
    engine = create_engine(connection_string)
    Session = sessionmaker(bind=engine)
    session = Session()

    q = session.query(State).filter(State.name.ilike("%a%")).order_by(State.id)

    for c in q:
        print("{}: {}".format(c.id, c.name))

    session.close()
