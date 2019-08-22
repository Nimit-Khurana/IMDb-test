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
        return '<Post {}>'.format(self.post)


def user_register(uname, fname, lname, email, password):
    user = User(username=uname, name=fname+" "+lname, email=email, password_hash=password)
    db.session.add(user)
    db.session.flush()
    db.session.commit()

    return "user created"

def user_query(args):
    user = args
    return user

def user_cookie(user_id):
    return User.query.get(int(user_id))

def user_if_exists(name):
    return User.query.filter_by(username=name).first()