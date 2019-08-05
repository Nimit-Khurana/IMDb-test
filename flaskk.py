# flask imports
from flask import Flask, request, render_template
from script import *
from flask_bootstrap import Bootstrap
# end flask imports
# form imports
from login_form import loginform
# end form imports

app = Flask(__name__)


app.config['SECRET_KEY'] = 'secret'


@app.route('/login',methods=['GET','POST'])
def Login():
    form = loginform()
    return render_template('login.html', form=form)

@app.route("/", methods=['GET'])
def data():
    return render_template()


# query Parameters used instead of complete url #
@app.route("/about", methods=['GET'])
def get_data():
    arg = request.args['query']
    return json.dumps(query(arg), indent=4)


@app.route('/moviesearch', methods=['GET'])
def create_strap():
    return render_template('imdb.html')

# Included jquery and ajax !!! #
# Request from ajax to flask--> check ajax_req.html

@app.route('/test')
def test():
    return render_template()    

'''
The term ‘web templating system’ refers to designing an HTML script in which the variable data can be inserted
dynamically. A web template system comprises of a template engine, some kind of data source and a template processor.

Flask uses jinja2 template engine. A web template contains HTML syntax interspersed placeholders for variables and
expressions (in these case Python expressions) which are replaced values when the template is rendered.

@app.route('/strap/<int:num>')                                {% for x in range(10) %}
def create_strap_intvar(num):                                   <h> {{x}} </h>
    return render_template('strap.html', x=num)               {%endfor%}
'''

if __name__ == "__main__":
    app.run(debug=True)
