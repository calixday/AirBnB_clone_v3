#!/usr/bin/python3
"""Flask server
"""
from flask import jsonify
from flask import Flask
from api.v1.views import app_views
from models import storage
from os import getenv

app = Flask(__name__)
app.register_blueprint(app_views)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def downtear(self):
    '''Status of your API'''
    storage.close()


@app.errorhandler(404)
def page_not_found(error):
    '''template return'''
    return jsonify("error='Not found"), 404


if __name__ == "__main__":
    for_host = getenv('HBNB_API_HOST')
    for_port = getenv('HBNB_API_PORT')
    if not for_host:
        host = '0.0.0.0'
    if not for_port:
        port = '5000'
    app.run(host=host, port=port, threaded=True)
