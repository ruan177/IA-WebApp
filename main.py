from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(
        "config.DevelopmentConfig")

    from index.index import index_blueprint
    app.register_blueprint(index_blueprint)

    from character.routes import character_blueprint
    app.register_blueprint(character_blueprint)

    db.init_app(app)

    if app.config["TESTING"]:
        with app.app_context():
            db.drop_all()
            db.create_all()

    return app


from model import *

if __name__ == "__main__":
    create_app().run(host="0.0.0.0", port=5000)
