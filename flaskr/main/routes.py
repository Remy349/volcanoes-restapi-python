from flask import Blueprint, jsonify

bp = Blueprint("main", __name__)


@bp.get("/")
def index():
    response = jsonify(
        {
            "message": "REST API of Nicaragua's volcanoes - Flask",
        }
    )
    response.status_code = 200

    return response
