from flaskr.controllers.volcano import VolcanoController
from werkzeug.exceptions import BadRequest, NotFound


def test_get_volcanoes_empty(app):
    volcano_controller = VolcanoController()
    volcanoes = volcano_controller.get_volcanoes()

    assert len(volcanoes) == 0


def test_get_volcanoes(app):
    volcano_controller = VolcanoController()

    for index in range(2):
        volcano_controller.create_volcano(
            {
                "name": f"Volcano name {index + 1}",
                "height": "1,500m",
                "last_eruption": "2023",
                "state": "Active",
            }
        )

    volcanoes = volcano_controller.get_volcanoes()

    assert len(volcanoes) == 2


def test_get_volcano_not_found(app):
    volcano_controller = VolcanoController()

    volcano_controller.create_volcano(
        {
            "name": "Volcano name 1",
            "height": "1,500m",
            "last_eruption": "2023",
            "state": "Active",
        }
    )

    try:
        volcano_controller.get_volcano(2)
    except NotFound as e:
        assert e.name == "Not Found"
        assert e.code == 404


def test_do_not_register_the_volcano_name_twice(app):
    volcano_controller = VolcanoController()

    try:
        for _ in range(2):
            volcano_controller.create_volcano(
                {
                    "name": "Volcano name 1",
                    "height": "1,500m",
                    "last_eruption": "2023",
                    "state": "Active",
                }
            )
    except BadRequest as e:
        assert e.name == "Bad Request"
        assert e.code == 400


def test_get_volcano(app):
    volcano_controller = VolcanoController()

    volcano_controller.create_volcano(
        {
            "name": "Volcano name 1",
            "height": "1,500m",
            "last_eruption": "2023",
            "state": "Active",
        }
    )

    volcano = volcano_controller.get_volcano(1)

    assert volcano.id == 1
    assert volcano.name == "Volcano name 1"


def test_create_volcano(app):
    volcano_controller = VolcanoController()

    volcano = volcano_controller.create_volcano(
        {
            "name": "Volcano name 1",
            "height": "1,500m",
            "last_eruption": "2023",
            "state": "Active",
        }
    )

    assert volcano is not None


def test_update_volcano(app):
    volcano_controller = VolcanoController()

    volcano = volcano_controller.create_volcano(
        {
            "name": "Volcano name 1",
            "height": "1,500m",
            "last_eruption": "2023",
            "state": "Active",
        }
    )

    assert volcano.name == "Volcano name 1"

    volcano_update = volcano_controller.update_volcano(
        volcano_data={
            "name": "Volcano name 2",
            "height": "1,500m",
            "last_eruption": "2023",
            "state": "Inactive",
        },
        volcano_id=1,
    )

    assert volcano_update.name == "Volcano name 2"
    assert volcano_update.state == "Inactive"


def test_delete_volcano(app):
    volcano_controller = VolcanoController()

    for index in range(2):
        volcano_controller.create_volcano(
            {
                "name": f"Volcano name {index + 1}",
                "height": "1,500m",
                "last_eruption": "2023",
                "state": "Active",
            }
        )

    volcano = volcano_controller.delete_volcano(1)
    volcanoes = volcano_controller.get_volcanoes()

    assert volcano.get("message") == "Volcano deleted."
    assert len(volcanoes) == 1
