from flask import Blueprint

bp = Blueprint("api", __name__)


@bp.get("/volcanoes")
def get_volcanoes():
    pass


@bp.get("/volcanoes/<int:id>")
def get_volcano(id):
    pass


@bp.post("/volcanoes")
def create_volcano():
    pass


@bp.put("/volcanoes/<int:id>")
def update_volcano(id):
    pass


@bp.delete("/volcanoes/<int:id>")
def delete_volcano(id):
    pass
