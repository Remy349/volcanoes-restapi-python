from flask import request
from flaskr import app,db
from flaskr.errors import error_response


def json_response():
    return request.accept_mimetypes["application/json"] >= \
        request.accept_mimetypes["text/html"]


@app.errorhandler(404)
def not_found_error(e):
    if json_response():
        return error_response(404)
    return "<h1>Error 404 - Not Found!</h1>", 404


@app.errorhandler(500)
def internal_error(e):
    db.session.rollback()
    if json_response():
        return error_response(500)
    return "<h1>Error 500 - Internal Server Error!</h1>", 500

