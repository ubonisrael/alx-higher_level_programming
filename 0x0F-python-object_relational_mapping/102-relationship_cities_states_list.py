#!/usr/bin/python3
"""contains the class definition of a State and an instance Base"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
from sys import argv

if __name__ == "__main__":
    port = 3306
    host = "localhost"

    connection_string = "mysql+mysqldb://{}:{}@{}:{}/{}".format(
        argv[1], argv[2], host, port, argv[3])

    engine = create_engine(connection_string)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    q = session.query(City).order_by(City.id)
    for city in q:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
