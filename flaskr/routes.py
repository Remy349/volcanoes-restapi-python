from flaskr import app, db
from flask import jsonify, request
from flaskr.errors import bad_request

from flaskr.models import Volcano


@app.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Nicaragua Volcanoes REST API"})


@app.route("/api/volcanoes", methods=["GET"])
def get_volcanoes():
    volcanoes = Volcano.query.all()

    data = {
        "country": "Nicaragua",
        "volcanoes": [v.to_dict() for v in volcanoes]
    }

    return jsonify(data)


@app.route("/api/volcanoes/<int:volcano_id>", methods=["GET"])
def get_volcano_id(volcano_id):
    return jsonify(Volcano.query.get_or_404(volcano_id).to_dict())


@app.route("/api/volcanoes", methods=["POST"])
def add_volcanoes():
    data = request.get_json() or {}

    if "name" not in data or "state" not in data or "height" not in data \
            or "last_eruption" not in data:
        return bad_request(
            "Must include name, state, height and last eruption fields!")
    if Volcano.query.filter_by(name=data["name"]).first():
        return bad_request("Name already registered!")

    volcano = Volcano()
    volcano.from_dict(data)

    db.session.add(volcano)
    db.session.commit()

    response = jsonify(volcano.to_dict())
    response.status_code = 201

    return response


@app.route("/api/volcanoes/<int:volcano_id>", methods=["PUT"])
def update_volcano_id(volcano_id):
    data = request.get_json() or {}

    volcano = Volcano.query.get_or_404(volcano_id)

    if "name" in data and data["name"] != volcano.name and \
            Volcano.query.filter_by(name=data["name"]).first():
        return bad_request("Name already registered!")

    if "name" in data or "state" in data or "height" in data or \
            "last_eruption" in data:
        volcano.from_dict(data)

        db.session.commit()

        return jsonify(volcano.to_dict())
    else:
        return bad_request(
            "Must include name, state, height or last eruption fields!")


@app.route("/api/volcanoes/<int:volcano_id>", methods=["DELETE"])
def delete_volcano_id(volcano_id):
    volcano = Volcano.query.get_or_404(volcano_id)

    db.session.delete(volcano)
    db.session.commit()

    return "", 204

