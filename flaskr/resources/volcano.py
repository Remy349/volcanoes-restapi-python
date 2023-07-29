from flask_smorest import Blueprint, abort
from flask.views import MethodView
from flaskr.schemas import VolcanoSchema, VolcanoUpdateSchema
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from flaskr.extensions import db

from flaskr.models import VolcanoModel

bp = Blueprint("volcanoes", __name__, description="Operations on volcanoes")


@bp.route("/volcano/<int:volcano_id>")
class Volcano(MethodView):
    @bp.response(200, VolcanoSchema)
    def get(self, volcano_id):
        volcano = db.get_or_404(VolcanoModel, volcano_id)
        return volcano

    @bp.arguments(VolcanoUpdateSchema)
    @bp.response(200, VolcanoSchema)
    def put(self, volcano_data, volcano_id):
        volcano = db.get_or_404(VolcanoModel, volcano_id)

        if volcano:
            volcano.name = volcano_data["name"]
            volcano.height = volcano_data["height"]
            volcano.last_eruption = volcano_data["last_eruption"]
            volcano.state = volcano_data["state"]
        else:
            volcano = VolcanoModel(id=volcano_id, **volcano_data)

        db.session.add(volcano)
        db.session.commit()

        return volcano

    @bp.response(204, example={"message": "Volcano deleted."})
    def delete(self, volcano_id):
        volcano = db.get_or_404(VolcanoModel, volcano_id)

        db.session.delete(volcano)
        db.session.commit()

        return {"message": "Volcano deleted."}


@bp.route("/volcano")
class VolcanoList(MethodView):
    @bp.response(200, VolcanoSchema(many=True))
    def get(self):
        return db.session.execute(db.select(VolcanoModel)).scalars().all()

    @bp.arguments(VolcanoSchema)
    @bp.response(201, VolcanoSchema)
    def post(self, volcano_data):
        volcano = VolcanoModel(**volcano_data)

        try:
            db.session.add(volcano)
            db.session.commit()
        except IntegrityError as e:
            abort(400, message=str(e))
        except SQLAlchemyError as e:
            abort(500, message=str(e))

        return volcano
