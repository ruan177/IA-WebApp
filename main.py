from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from index.index import index_blueprint

db= SQLAlchemy

def create_app():
    app = Flask(__name__)

    app.config.from_object(
        "config.DevelopmentConfig")

    app.register_blueprint(index_blueprint)

    app.run(host="0.0.0.0", port=5000)


if __name__ == "__main__":
    create_app()