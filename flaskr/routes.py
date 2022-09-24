from flaskr import app


@app.route("/", methods=["GET"])
def index():
    return "OK!!!"

