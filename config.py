import os
import mysql


class Config(object):
    TESTING = False
    DEBUG = False


class ProductionConfig(Config):
    DATABASE_URI = os.getenv("Database_URI")
    SQLALCHEMY_DATABASE_URI = DATABASE_URI


class DevelopmentConfig(Config):
    SECRET_KEY = "MY-SUPER-SECRET-KEY"

    TESTING = DEBUG = True

    DATABASE_URI = "mysql+mysqlconnector://root:residentevil6@127.0.0.1/rick_and_morty"

    SQLALCHEMY_DATABASE_URI = DATABASE_URI

    SESSION_PROTECTION = "strong"