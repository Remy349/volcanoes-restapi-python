import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    TESTING = False

    PROPAGATE_EXCEPTIONS = True
    API_TITLE = "Volcanoes REST API"
    API_VERSION = "v1"
    OPENAPI_VERSION = "3.0.3"

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    OPENAPI_URL_PREFIX = "/"
    OPENAPI_SWAGGER_UI_PATH = "/swagger-ui"
    OPENAPI_SWAGGER_UI_URL = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "data.db")


class TestingConfig(Config):
    TESTING = True

    SQLALCHEMY_DATABASE_URI = "sqlite:///"
