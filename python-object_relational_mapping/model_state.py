#!/usr/bin/python3
"""
Write a python file that contains the class
definition of a State
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class state(Base):
    """ 
    State class
    
        Attributes:
        __tablename__ (str): The table name of the class
        id (int): The State id of the class
        name (str): The State name of the class
    """
    __tablename__ = 'states' 
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    