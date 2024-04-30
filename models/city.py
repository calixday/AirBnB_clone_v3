#!/usr/bin/python3
'''
    class for the city.
'''
from models.base_model import BaseModel, Base
import models
from models.state import State
from os import getenv
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship



class City(BaseModel, Base):
    '''
        Define the class City that inherits from BaseModel.
    '''
    __tablename__ = "cities"
    if getenv("HBNB_TYPE_STORAGE") == "db":
        names = Column(String(128), nullable=False)
        state_ids = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship("Place", backref="cities",
                              cascade="all, delete, delete-orphan")
    else:
        state_id = ""
        name = ""
