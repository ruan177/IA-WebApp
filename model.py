from main import db


class Character(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    level = db.Column(db.Integer, nullable=False)
    exp = db.Column(db.db.String(30), nullable=True)
    life = db.Column(db.Integer, nullable=True)
    damage = db.Column(db.Integer, nullable=True)
    classe = db.Column(db.String(15), nullable=True)
