from flask_smorest import Blueprint
from flask.views import MethodView
from flaskr.schemas import VolcanoSchema, VolcanoUpdateSchema
from flaskr.controllers.volcano import VolcanoController

bp = Blueprint("volcanoes", __name__, description="Operations on volcanoes")

volcano_controller = VolcanoController()


@bp.route("/volcano/<int:volcano_id>")
class Volcano(MethodView):
    @bp.response(200, VolcanoSchema)
    def get(self, volcano_id):
        """ Create a volcano by ID """
        return volcano_controller.get_volcano(volcano_id)

    @bp.arguments(VolcanoUpdateSchema)
    @bp.response(200, VolcanoSchema)
    def put(self, volcano_data, volcano_id):
        """ Update a volcano by ID """
        return volcano_controller.update_volcano(volcano_data, volcano_id)

    @bp.response(204, example={"message": "Volcano deleted."})
    def delete(self, volcano_id):
        """ Delete a volcano by ID """
        return volcano_controller.delete_volcano(volcano_id)


@bp.route("/volcano")
class VolcanoList(MethodView):
    @bp.response(200, VolcanoSchema(many=True))
    def get(self):
        """ Get a list of all volcanoes """
        return volcano_controller.get_volcanoes()

    @bp.arguments(VolcanoSchema)
    @bp.response(201, VolcanoSchema)
    def post(self, volcano_data):
        """ Create a new volcano """
        return volcano_controller.create_volcano(volcano_data)
