from datetime import datetime
from flask_login import UserMixin
from flaskk import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    name = db.Column(db.String(64), index=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return self.name  


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return self.post
    
    def post_post(self):
        return self.post
    def post_time(self):
        return str(self.timestamp)
    def post_userid(self):
        return str(User.query.filter_by( id=self.user_id).first() )


def user_register(uname, fname, lname, email, password):
    user = User(username=uname, name=fname+" "+lname, email=email, password_hash=password)
    db.session.add(user)
    db.session.flush()
    db.session.commit()
    return "user created"

def DBrollback():
    return db.session.rollback()

def user_cookie(user_id):
    return User.query.get(int(user_id))

def user_exists(name):
    return User.query.filter_by(username=name).first()


def post_submit(post_input, current_userid):
    user_post = Post(post=post_input, user_id=current_userid)
    db.session.add(user_post)
    db.session.flush()
    db.session.commit()
    return "post created"

def get_user_post(current_userid):
    return Post.query.filter_by(user_id=current_userid).all()

def get_user_post_all():
    post_list = []

    posts = Post.query.all()
    for post in posts:
        post_list.append( [Post.post_userid(post), Post.post_time(post), Post.post_post(post)] )
    return post_list
