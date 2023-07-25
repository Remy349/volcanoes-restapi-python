import pytest
from config import TestConfig
from flaskr import create_app
from flaskr.extensions import db


@pytest.fixture()
def app():
    app = create_app(config_class=TestConfig)

    with app.app_context():
        db.create_all()

    yield app


@pytest.fixture()
def client(app):
    return app.test_client()
