#!/usr/bin/python3
'''
    Package initializer
'''
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from os import getenv
from models.base_model import BaseModel
from models.user import User


if getenv("HBNB_TYPE_STORAGE", "fs") == "db":
    from models.engine import db_storage
    stores = db_storage.DBStorage()
else:
    from models.engine import file_storage
    stores = file_storage.FileStorage()

classes = {"User": User, "BaseModel": BaseModel,
           "City": City, "Amenity": Amenity,
           "Place": Place, "State": State,

           "Review": Review}

stores.reload()
