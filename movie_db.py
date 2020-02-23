from datetime import datetime
from flaskk import db

class movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    searchString = db.Column(db.String(64), index=True)
    movie_name = db.Column(db.String(64), index=True, unique=True)
    image_url = db.Column(db.String(128), index=True)
    movieid = db.Column(db.Integer, index=True, unique=True)

    #def __repr__(self):
    #    return self.movieid
    def __repr__(self):
        return {"name":self.movie_name, "image":self.image_url, "id":self.movieid}

def search_cache(search, name, image, id):
    varSearch = movie(searchString=search,movie_name=name, image_url=image, movieid=id)
    db.session.add(varSearch)
    db.session.flush()
    db.session.commit()
    return "movie stored"

def DBrollback():
    return db.session.rollback()

def if_search_exists(name):
    return movie.query.filter_by(searchString=name).first()

def return_search_data(name):
    result = movie.query.filter_by(searchString=name).all()
    db_list_movie = []
    for r in result:
        db_list_movie.append({'name':r.searchString, 'image':r.image_url, 'id':r.movieid})
        return db_list_movie