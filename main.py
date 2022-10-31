from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    import datetime
    app = Flask(__name__)
    app.config.from_object(
        "config.DevelopmentConfig")

    db.init_app(app)

    from index.routes import index_blueprint
    app.register_blueprint(index_blueprint)

    from character.routes import character_blueprint
    app.register_blueprint(character_blueprint)

    from login.routes import login_blueprint
    app.register_blueprint(login_blueprint)

    from login import login_manager
    login_manager.init_app(app)

    if app.config["TESTING"]:
        with app.app_context():
            db.drop_all()
            db.create_all()

            db.session.add(User(
                name="fulano de tal",
                email="fulano@gmail.com",
                password="123456",
                birthdate=datetime.date(year=1990, month=2, day=1)
            ))
            db.session.commit()

    return app


from model import *

if __name__ == "__main__":
    app = create_app()
    print(app.url_map)
    app.run(host="0.0.0.0", port=5000)
