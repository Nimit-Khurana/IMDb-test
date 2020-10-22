import requests
import json
from bs4 import BeautifulSoup as soup


def jsonp_converter(url):
    try:
        req = requests.get(url)
        # convert p-json to json
        json_data = req.text.split("(", 1)[1].strip(")")

        data = json.loads(json_data)
        parsed_data = []
        # For no results !! #
        try:
            movies = data["d"]
        except KeyError:
            return parsed_data

        for movie in movies:
            new_movie_format = {}
            if "id" in movie.keys():
                new_movie_format["id"] = movie["id"]
            if "l" in movie.keys():
                new_movie_format["name"] = movie["l"]
            if "y" in movie.keys():
                new_movie_format["year"] = movie["y"]
            if "s" in movie.keys():
                new_movie_format["cast"] = movie["s"]
            if "i" in movie.keys():
                new_movie_format["image"] = movie["i"][0]
            parsed_data.append(new_movie_format)
        return json.dumps(parsed_data)
    except ConnectionError as c:
        return None


def movie_query(parameter):
    query_url = (
        "https://v2.sg.media-imdb.com/suggests/"
        + parameter[0]
        + "/"
        + parameter
        + ".json"
    )
    return jsonp_converter(query_url)


def imdb(url):
    import urllib.request

    response = urllib.request.urlopen(url)

    html = response.read()
    soup = soup(html, "html.parser")
    imdbData = {}

    try:
        description_found = (
            soup.find(attrs={"class": "summary_text"}).contents[0].strip()
        )
        imdbData["description"] = description_found
    except:
        imdbData["description"] = "Couldn't find content"

    try:
        rating_found = soup.find(attrs={"itemprop": "ratingValue"}).contents[0].strip()
        imdbData["rating"] = rating_found
    except:
        imdbData["rating"] = "-"

    try:
        summary_found = (
            soup.find(attrs={"class": "canwrap"})
            .find("p")
            .find("span")
            .contents[0]
            .strip()
        )
        imdbData["summary"] = summary_found
    except:
        imdbData["summary"] = "Couldn't find content"
    return imdbData


def twitter_profile():
    twitter_data = []
    username_list = [
        "PMOIndia",
        "narendramodi",
        "SrBachchan",
        "KanganaTeam",
        "akshaykumar",
        "iHrithik",
        "sachin_rt",
        "iamsrk",
    ]
    for account in username_list:
        url = "https://twitter.com/" + str(account)
        response = requests.get(url)
        html = response.text
        sou = soup(html, "html.parser")
        twitter_data.append({"username":"@"+account, "url":url})
        
    return twitter_data