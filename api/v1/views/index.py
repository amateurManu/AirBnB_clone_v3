#!/usr/bin/python3
""" Index file """
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route("/status", methods=['GET'], strict_slashes=False)
def status():
    """ Returns a JSON """
    return jsonify(status="OK")

@app_views.route("/api/v1/stats", methods=['GET'], strict_slashes=False)
def stats():
    """ Retrieves number of each projects """
    return jsonify(amenities=storage.count("Amenity"),
                   cities=storage.count("City"),
                   places=storage.count("Place"),
                   reviews=storage.count("Review"),
                   states=storage.count("State"),
                   users=storage.count("User"))

