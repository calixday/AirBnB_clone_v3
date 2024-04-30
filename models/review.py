#!/usr/bin/python3
'''
    Implementation of the Review class
'''
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel, Base):
    '''
        Implementation for the Review.
    '''
    __tablename__ = "reviews"
    if getenv("HBNB_TYPE_STORAGE") == "db":
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey("places.id"), nullable=False)

    else:
        text = ""
        place_id = ""
        user_id = ""
