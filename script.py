import requests
import json


def jsonp_converter(url):
    req = requests.get(url)
    json_data = req.text.split("(",1)[1].strip(")")

    data = json.loads(json_data)

    return data

def query(param1 ,param2):
    query_url = "https://v2.sg.media-imdb.com/suggests/" + param1 + "/" + param2 + ".json"

    return jsonp_converter(query_url)