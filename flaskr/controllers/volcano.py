from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from flask_smorest import abort
from flaskr.extensions import db

from flaskr.models import VolcanoModel


class VolcanoController:
    def get_volcanoes(self):
        return db.session.execute(db.select(VolcanoModel)).scalars().all()

    def get_volcano(self, volcano_id):
        volcano = db.get_or_404(VolcanoModel, volcano_id)
        return volcano

    def create_volcano(self, volcano_data):
        volcano = VolcanoModel(**volcano_data)

        try:
            db.session.add(volcano)
            db.session.commit()
        except IntegrityError:
            abort(400, message="Volcan already registered.")
        except SQLAlchemyError as e:
            abort(500, message=str(e))

        return volcano

    def update_volcano(self, volcano_data, volcano_id):
        volcano = db.get_or_404(VolcanoModel, volcano_id)

        if volcano:
            volcano.name = volcano_data["name"]
            volcano.height = volcano_data["height"]
            volcano.last_eruption = volcano_data["last_eruption"]
            volcano.state = volcano_data["state"]

        try:
            db.session.add(volcano)
            db.session.commit()
        except IntegrityError:
            abort(400, message="Volcano already registered.")
        except SQLAlchemyError as e:
            abort(500, message=str(e))

        return volcano

    def delete_volcano(self, volcano_id):
        volcano = db.get_or_404(VolcanoModel, volcano_id)

        db.session.delete(volcano)
        db.session.commit()

        return {"message": "Volcano deleted."}
