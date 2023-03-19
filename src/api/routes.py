"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Favorite, Person, Planet
from api.utils import generate_sitemap, APIException

api = Blueprint('api', __name__)


# @api.route('/hello', methods=['POST', 'GET'])
# def handle_hello():

#     response_body = {
#         "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
#     }

#     return jsonify(response_body), 200


############### Users ###############
#############⬇️⬇️⬇️⬇️##############


@api.route('/users', methods=['GET'])
def get_users():

    if request.method == "GET":
        all_users = User.query.all()
        user_dictionary = []
        for user in all_users:
            user_dictionary.append(user.serialize())
        print(user_dictionary)

    return jsonify(user_dictionary), 200


############### Persons #############
#############⬇️⬇️⬇️⬇️##############


@api.route('/person', methods=['GET'])
def get_person():

    if request.method == "GET":
        all_person = Person.query.all()
        person_dictionary = []
        for person in all_person:
            person_dictionary.append(person.serialize())
        print(person_dictionary)

    return jsonify(person_dictionary), 200


############### Planets #############
#############⬇️⬇️⬇️⬇️##############


@api.route('/planet', methods=['GET'])
def get_planet():

    if request.method == "GET":
        all_planets = Planet.query.all()
        planet_dictionary = []
        for planet in all_planets:
            planet_dictionary.append(planet.serialize())
        print(planet_dictionary)
    
    return jsonify(planet_dictionary), 200


############# Favorites #############
#############⬇️⬇️⬇️⬇️##############


@api.route('/favorite', methods=['GET'])
def get_favorites():

    if request.method == "GET":
        all_favorites = Favorite.query.all()
        favorite_dictionary = []
        for favorite in all_favorites:
            favorite_dictionary.append(favorite.serialize())
        print(favorite_dictionary)
    
    return jsonify(favorite_dictionary), 200