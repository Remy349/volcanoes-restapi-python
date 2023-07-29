import sqlalchemy as sa
from flaskr.extensions import db


class VolcanoModel(db.Model):
    __tablename__ = "volcanoes"

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(100), nullable=False, unique=True)
    height = sa.Column(sa.String(50), nullable=False, unique=False)
    last_eruption = sa.Column(sa.String(80), nullable=False, unique=True)
    state = sa.Column(sa.String(20), nullable=False, unique=True)
