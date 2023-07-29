import pytest
from flaskr import create_app
from config import TestingConfig
from flaskr.extensions import db


@pytest.fixture()
def app():
    app = create_app(testing_config=TestingConfig)

    with app.app_context():
        db.create_all()

    yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture()
def client(app):
    return app.test_client()
