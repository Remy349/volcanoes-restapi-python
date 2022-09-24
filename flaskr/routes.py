from flaskr import app
from flask import jsonify


@app.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Nicaragua Volcanoes REST API"})


@app.route("/api/volcanoes", methods=["GET"])
def get_volcanoes():
    pass


@app.route("/api/volcanoes/<int:volcano_id>", methods=["GET"])
def get_volcano_id(volcano_id):
    pass


@app.route("/api/volcanoes/<string:volcano_name>", methods=["GET"])
def get_volcano_name(volcano_name):
    pass


@app.route("/api/volcanoes", methods=["POST"])
def add_volcanoes():
    pass


@app.route("/api/volcanoes/<int:volcano_id>", methods=["PUT"])
def update_volcano_id(volcano_id):
    pass


@app.route("/api/volcanoes/<int:volcano_id>", methods=["DELETE"])
def delete_volcano_id(volcano_id):
    pass

