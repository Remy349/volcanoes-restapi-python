from flask import Blueprint, jsonify
from flaskr.extensions import db

from flaskr.models import Volcano

bp = Blueprint("api", __name__)


@bp.get("/volcanoes")
def get_volcanoes():
    query = db.session.execute(db.select(Volcano)).all()

    response = jsonify([data.to_dict() for data in query])
    response.status_code = 200

    return response


@bp.get("/volcanoes/<int:id>")
def get_volcano(id):
    query = db.get_or_404(Volcano, id)

    response = jsonify(query.to_dict())
    response.status_code = 200

    return response


@bp.post("/volcanoes")
def create_volcano():
    pass


@bp.put("/volcanoes/<int:id>")
def update_volcano(id):
    pass


@bp.delete("/volcanoes/<int:id>")
def delete_volcano(id):
    pass
