import models

from flask import Flask
from flaskr.extensions import db, migrate


def create_app():
    app = Flask(__name__)

    db.init_app(app)
    migrate.init_app(app, db, compare_type=True)

    return app
