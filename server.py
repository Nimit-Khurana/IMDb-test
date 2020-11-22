from datetime import datetime
import json
from script import movie_query, imdb, twitter_profile
from wuhan import VirusData
from flask import Flask, request, render_template, redirect, url_for
from twitter_api import get_user_by_username, get_users_by_listof_usernames
from dbconfig import DBconfig
from movie_db import (
    db,
    cache_search_results,
    clear_cache,
    if_search_cache_exists,
    get_results_from_cache,
    check_update_time,
)

app = Flask(__name__)

app.config["SECRET_KEY"] = "secret"
app.config.from_object(DBconfig)


@app.route("/")
def root():
    return render_template("imdb.html")


@app.route("/movieJsonDataEndpoint", methods=["GET"])
def movieJsonDataEndpoint():
    arg = request.args["query"]

    if if_search_cache_exists(arg) == None:
        data = movie_query(arg)
        if data != None:
            data_load = json.loads(data)
            data_dump = json.dumps(data)
            for i in range(len(data_load)):
                if "image" not in data_load[i].keys():
                    data_load[i]["image"] = ""

                upload = cache_search_results(
                    search=arg,
                    name=data_load[i]["name"],
                    movieid=data_load[i]["id"],
                    image=data_load[i]["image"],
                )
            print("Getting from IMDB api")
            return json.dumps(data, indent=4)
        else:
            return {}

    time_now = datetime.now()
    time_diff = time_now - check_update_time(arg)
    if divmod(time_diff.total_seconds(), 60)[0] > 600:
        data = movie_query(arg)
        data_load = json.loads(data)

        # clear the stored movie search
        clear_cache(search=arg)
        for i in range(len(data_load)):
            if "image" not in data_load[i].keys():
                data_load[i]["image"] = ""
            update = cache_search_results(
                name=data_load[i]["name"],
                movieid=data_load[i]["id"],
                image=data_load[i]["image"],
                search=arg,
            )
            print(update)
        print("Getting from database after update")
        return json.dumps(json.dumps(get_results_from_cache(arg)))
    else:
        print("Getting from database")
        return json.dumps(json.dumps(get_results_from_cache(arg)))


@app.route("/<moviename>")
def movie(moviename):
    try:
        title_arg = request.args["t"]
        poster_arg = request.args["i"]
        if title_arg.startswith("nm"):
            url = "https://imdb.com/name/" + title_arg
        else:
            url = "https://imdb.com/title/" + title_arg

        imdb_data = imdb(url)
        if imdb_data == False:
            return render_template("error.html")
        imdb_link = "https://www.imdb.com/title/" + str(title_arg)
        data = {"movie": moviename, "image": poster_arg, "imdbLink": imdb_link}
        data.update(imdb_data)
        return render_template("movie.html", data=data)
    except KeyError:
        return moviename

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/wuhan")
def wuhan():
    x = VirusData(url="https://covid-india-cases.herokuapp.com/states/")
    covid_data = [
        ["Total cases", x.total_cases()],
        ["Total cured", x.total_cured()],
        ["Total deaths", x.total_deaths()],
    ]
    state_data = x.state_wise_data()
    return render_template("wuhan.html", data=covid_data, state_data=state_data)

@app.route("/india")
def india():
    f = open("data.txt", "r")
    data = json.loads( f.read() )

    twitter_data = twitter_profile()
    return render_template("india.html", data = data, twitter_data = twitter_data )

@app.route("/india/api.html")
def india_api():
    f = open("data.txt", "r")
    return f.read()

@app.route("/test")
def error():
    x = VirusData(url="https://covid-india-cases.herokuapp.com/states/")
    covid_data = [
        ["Total cases", x.total_cases()],
        ["Total cured", x.total_cured()],
        ["Total deaths", x.total_deaths()],
    ]
    state_data = x.state_wise_data()
    return render_template("test.html", data=covid_data, state_data=state_data)

@app.route("/twitter")
def twitter():
    json_data = json.loads(get_users_by_listof_usernames())
    return render_template("twitter.html", data=json_data)

@app.route("/twitterJsonDataEndpoint", methods=["GET"])
def twitterJsonDataEndpoint():
    arg = request.args["query"]
    return get_user_by_username(arg)
    

if __name__ == "__main__":
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(debug=True)
