from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    lastname = db.Column(db.String(30))
    name = db.Column(db.String(30))
    username = db.Column(db.String(30), unique=True, nullable=False)
    favorites = db.relationship('Favorite', backref='user')

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
            "is_active": self.is_active,
            "lastname": self.lastname,
            "name": self.name,
            "username": self.username
        }

class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    person_id = db.Column(db.Integer, db.ForeignKey("person.id"), nullable=True)
    planet_id = db.Column(db.Integer, db.ForeignKey("planet.id"), nullable=True)

    def __repr__(self):
        return f'<Favorite {self.user_id}>'
    
    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "person_id": self.person_id,
            "planet_id": self.planet_id
        }

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    birth_year = db.Column(db.Integer)
    eye_color = db.Column(db.String)
    gender = db.Column(db.String)
    height = db.Column(db.Integer)
    name = db.Column(db.String)
    skin_color = db.Column(db.String)

    def __repr__(self):
        return f'<Person {self.user_id}>'
    
    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "birth_year": self.birth_year,
            "eye_color": self.eye_color,
            "gender": self.gender,
            "height": self.height,
            "name": self.name,
            "skin_color": self.skin_color
        }

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    name = db.Column(db.String(30))
    population = db.Column(db.Integer)
    terrain = db.Column(db.String)

    def __repr__(self):
        return f'<Planet {self.user_id}>'

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "name": self.name,
            "population": self.population,
            "terrain": self.terrain
        }