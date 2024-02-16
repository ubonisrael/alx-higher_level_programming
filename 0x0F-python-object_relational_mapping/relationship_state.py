#!/usr/bin/python3
"""contains the class definition of a State and an instance Base"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

meta = MetaData()
Base = declarative_base(metadata=meta)


class State(Base):
    """Representation of a State"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, unique=True,
                nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="states", cascade="all, delete-orphan")
