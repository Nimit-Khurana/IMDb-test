from datetime import datetime
import json
from flask_sqlalchemy import SQLAlchemy
from dbconfig import DBconfig

db = SQLAlchemy()


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    searchString = db.Column(db.String(64), index=True)
    movie_name = db.Column(db.String(64), index=True)
    image_url = db.Column(db.String(128), index=True)
    movieid = db.Column(db.Integer, index=True)
    update_time = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return {"name": self.movie_name, "image": self.image_url, "id": self.movieid}


def clear_cache(search):
    Movie.query.filter_by(searchString=search).delete()
    db.session.commit()


def check_update_time(name):
    ret = Movie.query.filter_by(searchString=name).first()
    return ret.update_time


def cache_search_results(search, name, image, movieid):
    varSearch = Movie(
        searchString=search, movie_name=name, image_url=image, movieid=movieid
    )
    db.session.add(varSearch)
    db.session.flush()
    db.session.commit()
    return "movie stored"


def db_rollback():
    return db.session.rollback()


def if_search_cache_exists(name):
    return Movie.query.filter_by(searchString=name).first()


def get_results_from_cache(name):
    result = Movie.query.filter_by(searchString=name).all()
    db_list_movie = []
    # db_list_movie.append(str(result))
    # return result
    for r in result:
        db_list_movie.append(
            {"name": r.movie_name, "image": r.image_url, "id": r.movieid}
        )
    return db_list_movie
