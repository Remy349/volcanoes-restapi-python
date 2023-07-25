# nicaragua-volcanoes-restapi-python

## Updating....

Simple REST API about some Nicaraguan volcanoes, developed with Python(Flask), SQLite, Flask-Migrate and Flask-SQLAlchemy.

- [How to use the API?](#how-to-use-the-api)

## How does it work?
If you want to test the functionality of the REST API, follow these steps:
- NOTE: You must have Python installed on your computer.

1. Download the repository:
```Shell
$ git clone https://github.com/Remy349/nicaragua-volcanoes-restapi-python.git

$ cd nicaragua-volcanoes-restapi-python
```

2. Once inside the repository create and activate a virtual environment:
```Shell
# For Linux
$ python3 -m venv venv
# Now activate the virtual enviroment
$ . venv/bin/activate

# For Windows(py -3 -m venv venv or...)
$ python -m venv venv
# Now activate the virtual enviroment
$ venv\Scripts\activate
```

3. Install the requirements:
```Shell
# For Windows could be just "pip"
(venv) $ pip3 install -r requirements.txt
```

4. OPTIONAL: it has a SQLite database with some values already registered in order to have a better experience but if you want to create a new database, delete the database and run the following in the terminal:
```Shell
# Adding table models to the database
(venv) $ flask db upgrade
```

5. Run the server:
```Shell
(venv) $ flask run
* Serving Flask app 'application.py'
* Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
```

## How to use the API?
The API has "HTTPie", a command-line HTTP client written in Python that makes it easy to send API requests. Now you can make the API requests from the terminal

| HTTP Method | Resource URL        | Notes                                   |
| ----------- | ------------------- | --------------------------------------- |
| `GET`       | */api/volcanoes*    | Return the collection of all volcanoes. |
| `GET`       | */api/volcanoes/id* | Return a volcano.                       | 
| `POST`      | */api/volcanoes*    | Register a new volcano.                 |
| `PUT`       | */api/volcanoes/id* | Modify the values of a volcano.         |
| `DELETE`    | */api/volcanoes/id* | Delete a volcano from the collection    |

Now that you know which requests are available, try making the calls from the terminal or a service such as Postman:

1. GET /api/volcanoes:
```Shell
(venv) $ http GET http://localhost:5000/api/volcanoes
HTTP/1.1 200 OK
Connection: close
Content-Length: 636
Content-Type: application/json
Date: Mon, 26 Sep 2022 17:51:13 GMT
Server: Werkzeug/2.2.2 Python/3.9.6

{
    "country": "Nicaragua",
    "volcanoes": [
        {
            "height": "1,394m",
            "id": 1,
            "last_eruption": "3,000 years ago",
            "name": "Maderas volcano",
            "state": "Inactive"
        },
        {
            "height": "1,345m",
            "id": 2,
            "last_eruption": "Unknown",
            "name": "Mombacho volcano",
            "state": "Inactive"
        },
        .................
    ]
}
```

2. GET /api/volcanoes/id:
```Shell
(venv) $ http GET http://localhost:5000/api/volcanoes/1
HTTP/1.1 200 OK
Connection: close
Content-Length: 126
Content-Type: application/json
Date: Mon, 26 Sep 2022 17:55:10 GMT
Server: Werkzeug/2.2.2 Python/3.9.6

{
    "height": "1,394m",
    "id": 1,
    "last_eruption": "3,000 years ago",
    "name": "Maderas volcano",
    "state": "Inactive"
}
```

3. POST /api/volcanoes
```Shell
(venv) $ http POST http://localhost:5000/api/volcanoes name="value" state="value" height="value" last_eruption="value"
HTTP/1.1 201 CREATED
Connection: close
Content-Length: 102
Content-Type: application/json
Date: Mon, 26 Sep 2022 18:01:17 GMT
Server: Werkzeug/2.2.2 Python/3.9.6

{
    "height": "value",
    "id": 5,
    "last_eruption": "value",
    "name": "value",
    "state": "value"
}
```

4. PUT /api/volcanoes/id
```Shell
# It is not necessary to enter all the fields, just enter the one you are interested in modifying.
(venv) $ http PUT http://localhost:5000/api/volcanoes/5 name="value changed"
HTTP/1.1 200 OK
Connection: close
Content-Length: 110
Content-Type: application/json
Date: Mon, 26 Sep 2022 18:06:18 GMT
Server: Werkzeug/2.2.2 Python/3.9.6

{
    "height": "value",
    "id": 5,
    "last_eruption": "value",
    "name": "value changed",
    "state": "value"
}
```

5. DELETE /api/volcanoes/id
```Shell
(venv) $ http DELETE http://localhost:5000/api/volcanoes/5
HTTP/1.1 204 NO CONTENT
Connection: close
Content-Type: text/html; charset=utf-8
Date: Mon, 26 Sep 2022 18:07:37 GMT
Server: Werkzeug/2.2.2 Python/3.9.6
```

### Developed by Santiago de Jesús Moraga Caldera - Remy349(GitHub)
