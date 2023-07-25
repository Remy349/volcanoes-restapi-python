from flask import Flask
from config import Config


def create_app(config_class=Config):
    app = Flask(__name__)

    app.config.from_object(config_class)

    return app

# from flask import Flask
# from config import Config
# from flask_migrate import Migrate
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)

# app.config.from_object(Config)

# db = SQLAlchemy(app)
# migrate = Migrate(app, db, compare_type=True)

# from flaskr import routes
# from flaskr import errors
# from flaskr import models
# from flaskr import handlers

