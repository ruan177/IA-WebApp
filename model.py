import hashlib

from flask_login import UserMixin

from main import db

from datetime import date


class User(db.Model, UserMixin):
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False, primary_key=True)
    _password = db.Column(db.String(64), nullable=False)
    birthdate = db.Column(db.Date, nullable=False)

    def get_id(self):
        return self.email

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        hash = hashlib.sha256()
        hash.update(value.encode("UTF-8"))
        self._password = hash.hexdigest()

    def verify_password(self, password):
        hash = hashlib.sha256()
        hash.update(str(password).encode())
        return hash.hexdigest() == self.password

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    level = db.Column(db.Integer, nullable=False)
    exp = db.Column(db.db.String(30), nullable=True)
    life = db.Column(db.Integer, nullable=True)
    damage = db.Column(db.Integer, nullable=True)
    classe = db.Column(db.String(15), nullable=True)
