#!/usr/bin/python3
'''
    Implementation of the Amenity class for the app
'''
from os import getenv
from models.place import place_amenity
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base



class Amenity(BaseModel, Base):
    '''
        Implementation for the Amenities.
    '''
    __tablename__ = "amenities"
    if getenv("HBNB_TYPE_STORAGE") == "db":
        names = Column(String(128), nullable=False)
        all_place_amenities = relationship("Place", secondary=place_amenity,
                                       back_populates="amenities")
    else:
        name = ""
