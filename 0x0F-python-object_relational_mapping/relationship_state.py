#!/usr/bin/python3

"""
 a python file that contains the
class definition of a State and
an instance Base = declarative_base()
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """
    This class inherits from Base
    and it links to the MySQL table states.
    """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True,
                nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade='all, delete')

    def __init__(self, **kwargs):
        """initialize object"""
        self.__dict__.update(kwargs)
