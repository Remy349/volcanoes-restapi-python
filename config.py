import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))

load_dotenv(os.path.join(basedir, ".env"))


class Config(object):
    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = "sqlite:////" + os.path.join(basedir, "app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///"
    TESTING = True
