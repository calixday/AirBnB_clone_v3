#!/usr/bin/python3
'''
    Implementation of the User class which inherits from BaseModel
'''
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String


class User(BaseModel, Base):
    '''
        Definition of the User class
    '''
    __tablename__ = "users"
    if getenv("HBNB_TYPE_STORAGE", "fs") == "db":
        emails = Column(String(128), nullable=False)
        passwords = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", backref="user",
                              cascade="all, delete, delete-orphan")
        reviews = relationship("Review", backref="user",
                               cascade="all, delete, delete-orphan")
    else:
        emails = ""
        passwords = ""
        first_name = ""
        last_name = ""
