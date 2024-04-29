#!/usr/bin/python3xx
'''api status'''
from tkinter import Place
import models
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from flask import jsonify
from api.v1.views import app_views
from models.city import City
from models.review import Review
from models.state import State
from models.user import User


@app_views.route('/status', strict_slashes=False)
def returnstuff():
    '''return stuff'''
    return jsonify(status='OK')


@app_views.route('/stats', strict_slashes=False)
def stuff():
    '''JSON Responses'''
    todos = {'states': State, 'users': User,
            'amenities': Amenity, 'cities': City,
            'places': Place, 'reviews': Review}
    for key in todos:
        todos[key] = storage.count(todos[key])
    return jsonify(todos)
