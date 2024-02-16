#!/usr/bin/python3
"""contains the class definition of a State and an instance Base"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv

port = 3306
host = "localhost"

connection_string = "mysql+mysqldb://{}:{}@{}:{}/{}".format(argv[1], argv[2], host, port, argv[3])

engine = create_engine(connection_string)
Session = sessionmaker(bind=engine)
session = Session()

session.query(State).filter(State.name.ilike("%a%")).delete(synchronize_session='fetch')
session.commit()