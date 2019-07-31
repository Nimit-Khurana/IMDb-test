from flask import Flask, request, render_template
from script import *
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)


# search for movie **complete given url #
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

'''
The term ‘web templating system’ refers to designing an HTML script in which the variable data can be inserted
dynamically. A web template system comprises of a template engine, some kind of data source and a template processor.

Flask uses jinga2 template engine. A web template contains HTML syntax interspersed placeholders for variables and
expressions (in these case Python expressions) which are replaced values when the template is rendered.

@app.route('/strap/<int:num>')                                {% for x in range(10) %}
def create_strap_intvar(num):                                   <h> {{x}} </h>
    return render_template('strap.html', x=num)               {%endfor%}
'''

if __name__ == "__main__":
    app.run(debug=True)
