# nicaragua-volcanoes-restapi-python

Simple REST API about some Nicaraguan volcanoes, developed with Python(Flask), SQLite, Flask-Migrate and Flask-SQLAlchemy.

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
