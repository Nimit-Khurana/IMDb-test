import requests
import json


def jsonp_converter(url):
    req = requests.get(url)
    #convert p-json to json
    json_data = req.text.split("(", 1)[1].strip(")")

    data = json.loads(json_data)
    parsed_data = []
    # For no results !! #
    try:
        movies = data['d']
    except KeyError:
        return parsed_data

    for movie in movies:
        new_movie_format = {}
        if 'id' in movie.keys():
            new_movie_format['id'] = movie["id"]
        if 'l' in movie.keys():
            new_movie_format["name"] = movie["l"]
        if 'y' in movie.keys():
            new_movie_format["year"] = movie["y"]
        if 's' in movie.keys():
            new_movie_format["cast"] = movie["s"]
        if 'i' in movie.keys():
            new_movie_format["image"] = movie["i"][0]
        parsed_data.append(new_movie_format)
    return json.dumps(parsed_data)


def query(parameter):
    query_url = "https://v2.sg.media-imdb.com/suggests/" + parameter[0] + "/" + parameter + ".json"
    return jsonp_converter(query_url)
