import flaskr.models

from config import Config
from flask import Flask
from flaskr.extensions import db, migrate, api

from flaskr.resources.volcano import bp as volcano_bp


def create_app(testing_config=None):
    app = Flask(__name__)

    if testing_config is None:
        app.config.from_object(Config)
    else:
        app.config.from_object(testing_config)

    db.init_app(app)
    migrate.init_app(app, db, compare_type=True)
    api.init_app(app)

    api.register_blueprint(volcano_bp, url_prefix="/api")

    return app
