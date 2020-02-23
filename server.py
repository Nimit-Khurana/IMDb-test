from datetime import datetime
import json
from script import movie_query

from flask import Flask, request, render_template, redirect, url_for

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


@app.route("/moviejson", methods=["GET"])
def movie_json():
    arg = request.args["query"]

    if if_search_cache_exists(arg) == None:
        data = movie_query(arg)
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


@app.route("/moviejson/post", methods=["GET", "POST"])
def movie_json_post():
    q = None
    content = request.form.get("contents")
    if request.method == "POST":
        return render_template(
            "post_movie.html", q=json.dumps(movie_query(content), indent=4)
        )
    return render_template("post_movie.html")


if __name__ == "__main__":
    db.init_app(app)
    app.run(debug=True)
