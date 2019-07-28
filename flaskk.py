from flask import Flask, jsonify, request
from script import *

app = Flask(__name__)

@app.route("/")
def data():
    return(jsonp_converter("https://v2.sg.media-imdb.com/suggests/a/avengers.json"))

@app.route("/get" , methods = ['GET'])
def get_data():
    arg1 = request.args['letter']
    arg2 = request.args['word']

    return (query(arg1, arg2))


if __name__ == "__main__":
    app.run(debug=True)