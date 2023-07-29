from flaskr.models import VolcanoModel
from flaskr.extensions import db


def add_test_volcano(volcano_data):
    volcano = VolcanoModel(**volcano_data)

    db.session.add(volcano)
    db.session.commit()


def test_get_volcanoes_empty(client):
    response = client.get("/api/volcano")

    assert response.status_code == 200
    assert response.json == []


def test_get_volcanoes(client, app):
    with app.app_context():
        add_test_volcano(
            {
                "name": "volcano 1",
                "height": "1,210m",
                "last_eruption": "2023",
                "state": "Active",
            }
        )
        add_test_volcano(
            {
                "name": "volcano 2",
                "height": "1,510m",
                "last_eruption": "2023",
                "state": "Inactive",
            }
        )

    response = client.get("/api/volcano")

    assert response.status_code == 200
    assert len(response.json) == 2


def test_get_volcano_not_found(client):
    response = client.get("/api/volcano/1")

    assert response.status_code == 404
    assert response.json["status"] == "Not Found"


def test_get_volcano(client, app):
    with app.app_context():
        add_test_volcano(
            {
                "name": "volcano 1",
                "height": "1,210m",
                "last_eruption": "2023",
                "state": "Active",
            }
        )

    response = client.get("/api/volcano/1")

    assert response.status_code == 200
    assert response.json["name"] == "volcano 1"


def test_add_volcano(client, app):
    volcano_data = {
        "name": "volcano 1",
        "height": "1,210m",
        "last_eruption": "2023",
        "state": "Active",
    }

    response = client.post("/api/volcano", json=volcano_data)

    assert response.status_code == 201
    assert response.json["name"] == "volcano 1"

    with app.app_context():
        volcano = db.session.execute(
            db.select(VolcanoModel).filter_by(name="volcano 1")
        ).scalar_one()

        assert volcano is not None


def test_update_volcano(client, app):
    with app.app_context():
        add_test_volcano(
            {
                "name": "volcano 1",
                "height": "1,210m",
                "last_eruption": "2023",
                "state": "Active",
            }
        )

    volcano_data = {
        "name": "update volcano name",
        "height": "1,210m",
        "last_eruption": "2023",
        "state": "Inactive",
    }

    response = client.put("/api/volcano/1", json=volcano_data)

    assert response.status_code == 200

    with app.app_context():
        volcano = db.session.execute(
            db.select(VolcanoModel).filter_by(id=1)
        ).scalar_one()

        assert volcano.name == "update volcano name"
        assert volcano.state == "Inactive"


def test_delete_volcano(client, app):
    with app.app_context():
        add_test_volcano(
            {
                "name": "volcano 1",
                "height": "1,210m",
                "last_eruption": "2023",
                "state": "Active",
            }
        )

    response = client.delete("/api/volcano/1")

    assert response.status_code == 204

    with app.app_context():
        volcano = db.session.execute(
            db.select(VolcanoModel).filter_by(name="volcano 1")
        ).first()

        assert volcano is None
