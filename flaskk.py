import json
from script import movie_query
# flask imports
from flask import Flask, request, render_template, redirect, url_for
# flask form EXTENTION imports
from login_form import loginform
from register_form import registerform
# Flask login EXTENTION
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
# flask sqlalchemy EXTENSION import
from dbconfig import DBconfig
from flask_sqlalchemy import SQLAlchemy
from models import *

app = Flask(__name__)

login_manager = LoginManager()
login_manager.init_app(app)
# login_view will redirect to "login" instead of showing unauth user which comes when user is not logged in
# i.e if user not logged in, then it will redirect to a route, in this case login.
login_manager.login_view = 'login'

app.config['SECRET_KEY'] = 'secret'
app.config.from_object(DBconfig)

db = SQLAlchemy(app)


@app.route('/')
def root():
    return render_template("home.html")

# check if user(id) is logged in-- (flask-login EXT.)
#Flask-Login stores the user ID in a cookie. When it reads that cookie, it takes the user
#ID and calls the query in the user_loader to find the user associated with that cookie.
@login_manager.user_loader
def load_user(id):
    return user_cookie(id)

@app.route('/login',methods=['GET','POST'])
def login():
    error = None
    form = loginform()

    remember_me = request.form.get('remember')
    uname = request.form.get('username')
    user = user_if_exists(uname)
    if form.validate_on_submit():
        if not user:
            error = "Username not found!"
            return render_template('login.html', form=form, error=error)
        else:
            if request.form.get('password') == user.password_hash :
                ## Doesn't work <======== remember me ========>
                login_user(user, remember=remember_me )
                return redirect( url_for('home', logged_in_user_name=current_user.name)  )
            else:
                error = "Wrong Password"
                return render_template('login.html', form=form, error=error)
 
    return render_template('login.html', form=form, error=error)


@app.route("/home/<logged_in_user_name>")
@login_required
def home(logged_in_user_name):
    return render_template("user_page.html", name=logged_in_user_name)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect( url_for('login') )


@app.route('/register',methods=['GET','POST'])
def register():
    error = None
    form = registerform()
    if request.method == 'POST':
        return user_register(request.form['username'], request.form['fname'], request.form['lname'], request.form['email'], request.form['password'])
        

    return render_template('register.html', regform=form)


# query Parameters used instead of complete url #
@app.route("/moviejson", methods=['GET'])
def movie_json():
    arg = request.args['query']
    return json.dumps(movie_query(arg), indent=4)


@app.route("/moviejson/post", methods=['GET', 'POST'])
def movie_json_post():
    q = None
    content = request.form.get('contents')
    if request.method == 'POST':
        return render_template('post_movie.html', q =json.dumps(query(content), indent=4))
    return render_template('post_movie.html')


@app.route('/moviesearch', methods=['GET'])
def imdb():
    return render_template('imdb.html')

# Included jquery and ajax !!! #
# Request from ajax to flask--> check ajax_req.html
@app.route('/test')
def test():
    return render_template('home.html')


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