#!/usr/bin/python3
"""contains the class definition of a State and an instance Base"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

port = 3306
host = "localhost"
connection_string = "mysql+mysqldb://{}:{}@{}:{}/{}".format(
    sys.argv[1], sys.argv[2], host, port, sys.argv[3])

if __name__ == "__main__":
    engine = create_engine(connection_string)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    q = session.query(State).order_by(State.id)

    for c in q:
        print("{}: {}".format(c.id, c.name))

    session.close()
