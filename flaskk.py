import json
from script import movie_query
# flask imports
from flask import Flask, request, render_template, redirect, url_for
## flask form EXTENTION imports
#from login_form import loginform
#from register_form import registerform
## Flask login EXTENTION
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
# flask sqlalchemy EXTENSION import
from dbconfig import DBconfig
from flask_sqlalchemy import SQLAlchemy
#from models import *
from movie_db import *
# image/file upload by user
#from werkzeug.utils import secure_filename


app = Flask(__name__)

#login_manager = LoginManager()
#login_manager.init_app(app)
# login_view will redirect to "login" instead of showing unauth user which comes when user is not logged in
# i.e if user not logged in, then it will redirect to a route, in this case login.
#login_manager.login_view = 'login'

app.config['SECRET_KEY'] = 'secret'
app.config.from_object(DBconfig)

db = SQLAlchemy(app)

#ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def root():
    return render_template("home.html")

# check if user(id) is logged in-- (flask-login EXT.)
#Flask-Login stores the user ID in a cookie. When it reads that cookie, it takes the user
#ID and calls the query in the user_loader to find the user associated with that cookie.
'''@login_manager.user_loader
def load_user(id):
    return user_cookie(id)

@app.route('/login',methods=['GET','POST'])
def login():
    # CHECK if already user is logged in from a client #
    if current_user.is_active and current_user.is_authenticated:
        return redirect( url_for('home') )

    error = None
    form = loginform()

    remember_me = request.form.get('remember')
    uname = request.form.get('username')
    user = user_exists(uname)

    if form.validate_on_submit():
        if not user:
            error = "Username not found!"
            return render_template('login.html', form=form, error=error)
        else:
            if request.form.get('password') == user.password_hash :
                ## Doesn't work <======== remember me ========>
                login_user(user, remember=remember_me)
                return redirect( url_for('home')  )
            else:
                error = "Wrong Password"
                return render_template('login.html', form=form, error=error)
 
    return render_template('login.html', form=form, error=error)


@app.route("/home", methods=['GET','POST'])
@login_required
def home():
    message = None
    if request.method == 'POST':
        post_submitted = post_submit(request.form['post_input'], current_user.get_id())
    # TO-DO-- CHECK return type for 'posts' : message not working #
    
        # to DO--- reset form after submission #
    return render_template("user_page.html", html_message=message, name=current_user.name)

@app.route("/allposts", methods=['GET'])
@login_required
def allposts():
    post = None
    post = get_user_post_all()
    # post gets a list return type #
    if post==None:
        return "No user posts!!"
    return render_template("allPosts.html", posts=post, name=current_user.name)

@app.route("/userposts", methods=['GET'])
@login_required
def userposts():
    posts = None
    # GET user posts HERE #
    posts = get_user_post(current_user.get_id())
    # post gets a list return type #
    if posts==None:
        return "No user posts!!"
    return render_template("userPost.html", posts=posts, name=current_user.name)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect( url_for('login') )


@app.route('/register',methods=['GET','POST'])
def register():
    error = None
    form = registerform()

    def allowed_file(filename):
        return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    if request.method == 'POST':
        reg_result = user_register(request.form['username'], request.form['fname'], request.form['lname'], request.form['email'], request.form['password'])
        if not reg_result:
            # for invalid request error on Database
            DBrollback()
            redirect( url_for('register') )
        else:
            return redirect(url_for('login') )
        

    return render_template('register.html', regform=form)
'''

# query Parameters used instead of complete url #
@app.route("/moviejson", methods=['GET'])
def movie_json():
    arg = request.args['query']
    if not if_search_exists(arg):
        data = movie_query(arg)
        data_load = json.loads(data)
        data_dump = json.dumps(data)
        for i in range(len(data_load)):
            upload = search_cache(search=arg,name=data_load[i]['name'],id=data_load[i]['id'],image=data_load[i]['image'])
            if not upload:
                # for invalid request error on Database
                DBrollback()
                redirect( url_for('movie_json') )
            return json.dumps(data, indent=4)
    else:
        return json.dumps(json.dumps(return_search_data(arg)))
        


@app.route("/moviejson/post", methods=['GET', 'POST'])
def movie_json_post():
    q = None
    content = request.form.get('contents')
    if request.method == 'POST':
        return render_template('post_movie.html', q =json.dumps(movie_query(content), indent=4))
    return render_template('post_movie.html')


@app.route('/moviesearch', methods=['GET'])
def imdb():
    return render_template('imdb.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

# Included jquery and ajax !!! #
# Request from ajax to flask--> check ajax_req.html
@app.route('/test')
def test():
    return render_template('test.html')


'''
The term ‘web templating system’ refers to designing an HTML script in which the variable data can be inserted
dynamically. A web template system comprises of a template engine, some kind of data source and a template processor.

Flask uses jinja2 template engine. A web template contains HTML syntax interspersed placeholders for variables and
expressions (in these case Python expressions) which are replaced values when the template is rendered.

@app.route('/strap/<int:num>')                                {% for x in range(10) %}
def create_strap_intvar(num):                                   <h> {{x}} </h>
    return render_template('strap.html', x=num)               {%endfor%}
'''

def printname():
    for name, func in app.view_functions.items():
        print(name)


if __name__ == "__main__":
    app.run(debug=True)
