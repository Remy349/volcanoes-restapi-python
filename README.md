# volcanoes-restapi-python

Simple REST API about volcanoes. You can get some information about volcanoes by entering data such as name, last eruption date, height and status.

The REST API was developed using Python, Flask, Flask-SQLALchemy, Flask-Migrate, and Flask-Smorest. Flask-Smorest helped me to better develop the REST API and to integrate Swagger UI.

## Table of Contents

- [Preview image](#preview-image)
- [REST API routes](#rest-api-routes)
- [How to use the REST API?.](#how-to-use-the-rest-api)
- [Database migrations](#database-migrations)

## Preview image

![PREVIEW](./preview/preview.png)

## REST API routes

| HTTP Method | Resource URL                | Notes                           |
| ----------- | --------------------------- | ------------------------------- |
| `GET`       | `/api/volcano`              | Obtain a list of all volcanoes. |
| `GET`       | `/api/volcano/{volcano_id}` | Obtain a single record.         |
| `POST`      | `/api/volcano`              | Add a new record.               |
| `PUT`       | `/api/volcano/{volcano_id}` | Update a record.                |
| `DELETE`    | `/api/volcano/{volcano_id}` | Delete a record.                |

## How to use the REST API?

1. Clone the repository on your computer:

```shell
$ git clone https://github.com/Remy349/volcanoes-restapi-python.git

$ cd volcanoes-restapi-python/
```

2. Create a virtual environment using Python and install dependencies:

  - If you have Pipenv you can do it in the following way:
```shell
$ pipenv shell

$ pipenv install -r requirements.txt
```

  - If you do not have Pipenv you can do it this way. These are for Linux/macOS, on Windows they might be a little different:
```shell
$ python3 -m venv venv

$ . venv/bin/activate

$ pip install -r requirements.txt
```

3. Run the REST API and go to http://localhost:5000/swagger-ui:

```shell
$ flask run
* Serving Flask app 'application.py'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 168-842-935
```

## Database migrations

The project has a database made on SQLite called *data.db*, where all the records will be stored.

If you want to delete it and create it again, execute the following commands provided by Flask-Migrate for handling database migrations. Always with your virtual environment active:

```shell
$ flask db upgrade
```

**NOTE**: If you delete the migrations folder you will have to create it again, create the migration and add the changes. This whole process can be done in the following way:

```shell
# Creates the folder for migrations.
$ flask db init

# Create the migration. This must be done every time you update or add a model.
$ flask db migrate

# Add the changes.
$ flask db upgrade
```

### Developed by Santiago de Jesús Moraga Caldera - Remy349(GitHub)
