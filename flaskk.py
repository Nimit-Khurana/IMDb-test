from flask import Flask, request, render_template
from script import *
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)


# search for movie **given url #
@app.route("/")
def data():
    return jsonp_converter("https://v2.sg.media-imdb.com/suggests/a/avengers.json")


# query Parameters used instead of complete url #
@app.route("/get", methods=['GET'])
def get_data():
    arg = request.args['q']
    return json.dumps(query(arg), indent=4)


# Included Bootstrap here !!! #
@app.route('/strap')
def create_strap():
    return render_template('strap.html')


if __name__ == "__main__":
    app.run(debug=True)
