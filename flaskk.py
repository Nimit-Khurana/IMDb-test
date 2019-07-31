from flask import Flask, request, render_template
from script import *
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/strap')
def create_strap():
    return render_template('strap.html')


@app.route("/")
def data():

    return(jsonp_converter("https://v2.sg.media-imdb.com/suggests/a/avengers.json"))

@app.route("/get" , methods = ['GET'])
def get_data():
    arg = request.args['q']
    return json.dumps(query(arg), indent=4)


if __name__ == "__main__":
    app.run(debug=True)
