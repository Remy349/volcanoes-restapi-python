import flaskr.models

from config import Config
from flask import Flask
from flaskr.extensions import db, migrate, api

from flaskr.resources.volcano import bp as volcano_bp


def create_app(config_class=Config):
    app = Flask(__name__)

    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db, compare_type=True)
    api.init_app(app)

    api.register_blueprint(volcano_bp, url_prefix="/api")

    return app
