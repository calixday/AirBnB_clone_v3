#!/usr/bin/python3
"""sort out the amenities"""
from models.amenity import Amenity
from datetime import datetime
import uuid
from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage


@app_views.route('/amenities/', methods=['GET'])
def list_amenities():
    '''list retrival'''
    l_amenities = [obj.to_dict() for obj in storage.all("Amenity").values()]
    return jsonify(l_amenities)


@app_views.route('/amenities/<amenity_id>', methods=['GET'])
def get_amenity(amenity_id):
    '''Retrieves an Amenity object'''
    a_amenities = storage.all("Amenity").values()
    amenity_objects = [obj.to_dict() for obj in a_amenities
                       if obj.id == amenity_id]
    if amenity_objects == []:
        abort(404)
    return jsonify(amenity_objects[0])


@app_views.route('/amenities/<amenity_id>', methods=['DELETE'])
def delete_amenity(amenity_id):
    '''Deletes an Amenity object'''
    a_amenities = storage.all("Amenity").values()
    amenity_objects = [obj.to_dict() for obj in a_amenities
                       if obj.id == amenity_id]
    if amenity_objects == []:
        abort(404)
    amenity_objects.remove(amenity_objects[0])
    for obj in a_amenities:
        if obj.id == amenity_id:
            storage.delete(obj)
            storage.save()
    return jsonify({}), 200


@app_views.route('/amenities/', methods=['POST'])
def create_amenity():
    '''Creates an Amenity'''
    if not request.get_json():
        abort(400, 'Not a JSON')
    if 'name' not in request.get_json():
        abort(400, 'Missing name')
    amenities = []
    new_amenity = Amenity(name=request.json['name'])
    storage.new(new_amenity)
    storage.save()
    amenities.append(new_amenity.to_dict())
    return jsonify(amenities[0]), 201


@app_views.route('/amenities/<amenity_id>', methods=['PUT'])
def updates_amenity(amenity_id):
    '''Updates an Amenity object'''
    all_amenities = storage.all("Amenity").values()
    amenity_objects = [obj.to_dict() for obj in all_amenities
                       if obj.id == amenity_id]
    if amenity_objects == []:
        abort(404)
    if not request.get_json():
        abort(400, 'Not a JSON')
    amenity_objects[0]['name'] = request.json['name']
    for obj in all_amenities:
        if obj.id == amenity_id:
            obj.name = request.json['name']
    storage.save()
    return jsonify(amenity_objects[0]), 200
