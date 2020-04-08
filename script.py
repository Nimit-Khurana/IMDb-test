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


def movie_query(parameter):
    query_url = "https://v2.sg.media-imdb.com/suggests/" + parameter[0] + "/" + parameter + ".json"
    return jsonp_converter(query_url)

def youtube(query):
    import urllib.request
    from bs4 import BeautifulSoup

    text = urllib.parse.quote(query)
    url = "https://www.youtube.com/results?search_query=" + text + "trailer"
    response = urllib.request.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    text_found = soup.find(attrs={'class':'yt-uix-tile-link'})['href']
    return text_found[9:]

def imdb(url):
    import urllib.request
    from bs4 import BeautifulSoup
    
    
    response = urllib.request.urlopen(url)
    
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    imdbData = {}

    try:
        description_found = soup.find(attrs={'class':'summary_text'}).contents[0].strip()
        imdbData["description"] = description_found
    except:
        imdbData["description"] = "Couldn't find content"
    
    try:
        rating_found = soup.find(attrs={'itemprop':'ratingValue'}).contents[0].strip()
        imdbData["rating"] = rating_found
    except:
        imdbData["rating"] = "-"
        
    try:
        summary_found = soup.find(attrs={'class':'canwrap'}).find("p").find("span").contents[0].strip()
        imdbData["summary"] = summary_found
    except:
        imdbData["summary"] = "Couldn't find content"    
    return imdbData
