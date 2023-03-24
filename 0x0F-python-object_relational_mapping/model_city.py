#!/usr/bin/python3
""" Create City class """
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base

Base = declarative_base()
class City(Base):
    '''City model for my db'''
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, nullable=False,
                autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    
""" class State(Base):
    """ """class City""" """"
    __table__ = 'state'
    id = Column(Integer, nullable=False, primary_key=True, auto_increment=True)
    name = Column(String(128), nullable=False)
"""
