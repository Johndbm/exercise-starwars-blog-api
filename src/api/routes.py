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

# 📝 Instrucciones
# Crea un API conectada a una base de datos e implemente los siguientes endpoints (muy similares a SWAPI.dev or SWAPI.tech):

# [GET] /people Listar todos los registros de people en la base de datos
# [GET] /people/<int:people_id> Listar la información de una sola people
# [GET] /planets Listar los registros de planets en la base de datos
# [GET] /planets/<int:planet_id> Listar la información de un solo planet
# Adicionalmente necesitamos crear los siguientes endpoints para que podamos tener usuarios en nuestro blog:

# [GET] /users Listar todos los usuarios del blog
# [GET] /users/favorites Listar todos los favoritos que pertenecen al usuario actual.
# [POST] /favorite/planet/<int:planet_id> Añade un nuevo planet favorito al usuario actual con el planet id = planet_id.
# [POST] /favorite/people/<int:planet_id> Añade una nueva people favorita al usuario actual con el people.id = people_id.
# [DELETE] /favorite/planet/<int:planet_id> Elimina un planet favorito con el id = planet_id`.
# [DELETE] /favorite/people/<int:people_id> Elimina una people favorita con el id = people_id.
# Tu API actual no tiene un sistema de autenticación (todavía), es por eso que la única forma de crear usuarios es directamente en la base de datos usando el flask admin.


############## To Do's ##############
# -✅ Agregados endpoints GET para todos "/person", "/user", "/planet", "favorite"
# -✅ Faltan los endpoints GET individuales para "/person" y para "/planet"
# -✅ Faltan los endpoints GET, POST y DELETE "/user" y "/user/favorite"
#####################################

############### Users ###############
#############⬇️⬇️⬇️⬇️##############


@api.route('/user', methods=['GET'])
def get_user():

    if request.method == "GET":
        all_users = User.query.all()
        user_dictionary = []
        for user in all_users:
            user_dictionary.append(user.serialize())
        print(user_dictionary)

    return jsonify(user_dictionary), 200

@api.route('/user', methods=['POST'])
def add_user():

    if request.method == "POST":
        body = request.json
        email = body.get("email", None)
        password = body.get("password", None)
        name = body.get("name", None)
        if email is None or password is None or name is None:
            return jsonify({"Message: Missing Fields"}), 400
        else:
            try: 
                user = User(email=email, password=password, name=name)
                db.session.add(user)
                db.session.commit()
                return jsonify({"Message":"User Created!"}), 200
            except Exception as error:
                return jsonify(error.args[0]),error.args[1]


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

@api.route('/person/<int:person_id>', methods=['GET'])
def handle_user_by_id(person_id = None):
    if request.method == 'GET':
        if person_id == None:
            return jsonify({"Message: Bad request"}), 400
        else:
            person =  Person()
            person = person.query.get(person_id)
            if person is None:
                return jsonify({'Message': 'Not found'}), 404
            else:
                return jsonify(person.serialize()), 200


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

@api.route('/planet/<int:planet_id>', methods=['GET'])
def handle_planet_by_id(planet_id = None):
    if request.method == 'GET':
        if planet_id == None:
            return jsonify({"Message: Bad request"}), 400
        else:
            planet =  Planet()
            planet = planet.query.get(planet_id)
            if planet is None:
                return jsonify({'Message': 'Not found'}), 404
            else:
                return jsonify(planet.serialize()), 200


############# Favorites #############
#############⬇️⬇️⬇️⬇️##############


@api.route('/user/<int:user_id>/favorite', methods=['GET'])
def get_favorites(user_id):

    if request.method == "GET":
        all_favorites = Favorite.query.filter_by(user_id=user_id)
        favorite_dictionary = []
        for favorite in all_favorites:
            favorite_dictionary.append(favorite.serialize())
        print(favorite_dictionary)
    
    return jsonify(favorite_dictionary), 200



@api.route('/favorite/person/<int:user_id>/<int:person_id>', methods=['POST'])
def add_person(user_id, person_id):

    if request.method == "POST":
        favorites = Favorite.query.filter_by(user_id=user_id, person_id=person_id).first()
        if favorites is not None:
            return jsonify({"Message":"Already a favorite"}), 400
        else:
            try:
                favorites = Favorite(user_id=user_id, person_id=person_id)
                db.session.add(favorites)
                db.session.commit()
                return jsonify({"Message":"Person added!"}), 200
            except Exception as error:
                return jsonify(error.args[0]), error.args[1] if len(error.args) > 1 else 500

@api.route('/favorite/person/<int:user_id>/<int:person_id>', methods=['DELETE'])
def delete_person(user_id, person_id):

    if request.method == "DELETE":
        favorites = Favorite.query.filter_by(user_id=user_id, person_id=person_id).first()
        if favorites is None:
            return jsonify({"Message":"Favorite does not exist or already deleted"}), 400
        else:
            try:
                db.session.delete(favorites)
                db.session.commit()
                return jsonify({"Message":"Person deleted!"}), 200
            except Exception as error:
                return jsonify(error.args[0]), error.args[1] if len(error.args) > 1 else 500


@api.route('/favorite/planet/<int:user_id>/<int:planet_id>', methods=['POST'])
def add_planet(user_id, planet_id):

    if request.method == "POST":
        favorites = Favorite.query.filter_by(user_id=user_id, planet_id=planet_id).first()
        if favorites is not None:
            return jsonify({"Message":"Already a favorite"}), 400
        else:
            try:
                favorites = Favorite(user_id=user_id, planet_id=planet_id)
                db.session.add(favorites)
                db.session.commit()
                return jsonify({"Message":"Planet added!"}), 200
            except Exception as error:
                return jsonify(error.args[0]), error.args[1] if len(error.args) > 1 else 500

@api.route('/favorite/planet/<int:user_id>/<int:planet_id>', methods=['DELETE'])
def delete_planet(user_id, planet_id):

    if request.method == "DELETE":
        favorites = Favorite.query.filter_by(user_id=user_id, planet_id=planet_id).first()
        if favorites is None:
            return jsonify({"Message":"Favorite does not exist or already deleted"}), 400
        else:
            try:
                db.session.delete(favorites)
                db.session.commit()
                return jsonify({"Message":"Planet deleted!"}), 200
            except Exception as error:
                return jsonify(error.args[0]), error.args[1] if len(error.args) > 1 else 500