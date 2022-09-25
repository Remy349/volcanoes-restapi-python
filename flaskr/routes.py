from flaskr import app
from flask import jsonify, request

volcanoes = [
    {
        "id": 1,
        "name": "Maderas volcano",
        "state": "Inactive",
        "height": "1,394m",
        "last_eruption": "3,000 years ago"
    },
    {
        "id": 2,
        "name": "Mombacho volcano",
        "state": "Inactive",
        "height": "1,345m",
        "last_eruption": "Unknown"
    },
    {
        "id": 3,
        "name": "Masaya volcano",
        "state": "Active",
        "height": "635m",
        "last_eruption": "2003"
    }
]


@app.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Nicaragua Volcanoes REST API"})


@app.route("/api/volcanoes", methods=["GET"])
def get_volcanoes():
    return jsonify(
        {"volcanoes": volcanoes, "country": "Nicaragua"})


@app.route("/api/volcanoes/<int:volcano_id>", methods=["GET"])
def get_volcano_id(volcano_id):
    volcano_found = {}

    for volcano in volcanoes:
        if volcano["id"] == volcano_id:
            volcano_found = volcano

    if volcano_found:
        return jsonify({"volcano": volcano_found})

    response = jsonify({"error": "ID not found!"})
    response.status_code = 404

    return response


@app.route("/api/volcanoes", methods=["POST"])
def add_volcanoes():
    data = request.get_json() or {}

    if "name" not in data or "state" not in data or "height" not in data \
            or "last_eruption" not in data:
        response = jsonify({"error": "Bad request!"})
        response.status_code = 400

        return response

    data["id"] = len(volcanoes) + 1

    volcanoes.append(data)

    response = jsonify({"volcano": data})
    response.status_code = 201

    return response


@app.route("/api/volcanoes/<int:volcano_id>", methods=["PUT"])
def update_volcano_id(volcano_id):
    data = request.get_json() or {}

    volcano_found = {}

    for volcano in volcanoes:
        if volcano["id"] == volcano_id:
            volcano_found = volcano

    if volcano_found:
        if "name" in data:
            volcano_found["name"] = data["name"]
        if "state" in data:
            volcano_found["state"] = data["state"]
        if "height" in data:
            volcano_found["height"] = data["height"]
        if "last_eruption" in data:
            volcano_found["last_eruption"] = data["last_eruption"]

        return jsonify({"volcano": volcano_found})

    response = jsonify({"error": "ID not found!"})
    response.status_code = 404

    return response


@app.route("/api/volcanoes/<int:volcano_id>", methods=["DELETE"])
def delete_volcano_id(volcano_id):
    volcano_found = {}

    for volcano in volcanoes:
        if volcano["id"] == volcano_id:
            volcano_found = volcano

    if volcano_found:
        volcanoes.remove(volcano_found)
        return jsonify({"volcanoes": volcanoes})

    response = jsonify({"error": "ID not found!"})
    response.status_code = 404

    return response

