from flask import Flask
from config import Config
from flaskr.extensions import db, migrate

from flaskr.main.routes import bp as main_bp
from flaskr.api.routes import bp as api_bp


def create_app(config_class=Config):
    app = Flask(__name__)

    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db, compare_type=True)

    app.register_blueprint(main_bp)
    app.register_blueprint(api_bp, url_prefix="/api")

    return app


from flaskr import models
