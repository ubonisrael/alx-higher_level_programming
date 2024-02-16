#!/usr/bin/python3
"""contains the class definition of a State and an instance Base"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv

if __name__ == "__main__":
    port = 3306
    host = "localhost"

    connection_string = "mysql+mysqldb://{}:{}@{}:{}/{}".format(
        argv[1], argv[2], host, port, argv[3])

    engine = create_engine(connection_string)
    Session = sessionmaker(bind=engine)
    session = Session()

    louisiana = State(name='Louisiana')
    session.add(louisiana)
    session.commit()
    print(louisiana.id)
