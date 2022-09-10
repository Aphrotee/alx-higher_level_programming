#!/usr/bin/python3

"""
 a python file that contains the
class definition of a State and
an instance Base = declarative_base()
"""


import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy import (create_engine)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
    "root",
    "root",
    "hbtn_0e_6_usa"), pool_pre_ping=True)
Base.metadata.create_all(engine)


class State(Base):
    """
    This class inherits from Base
    and it links to the MySQL table states.
    """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True,
                nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
