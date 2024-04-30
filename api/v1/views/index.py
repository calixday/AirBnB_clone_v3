#!/usr/bin/python3
"""index"""
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.user import User
from models.place import Place


classes = {"users": "User", "places": "Place", "states": "State",
           "cities": "City", "amenities": "Amenity",
           "reviews": "Review"}


@app_views.route('/status', methods=['GET'])
def status():
    ''' routes to status page  of its start'''
    return jsonify({'status': 'OK'})


@app_views.route('/stats', methods=['GET'])
def count():
    '''retrieves the number of each objects by type'''
    count_diction = {}
    for cls in classes:
        count_diction[cls] = storage.count(classes[cls])
    return jsonify(count_diction)
