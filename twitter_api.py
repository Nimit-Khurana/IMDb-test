import requests
import os
import json
from requests_oauthlib import OAuth1
from twitter_keys import consumer_key, consumer_secretkey, access_secret, access_token


# To set your enviornment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'

def bearer_auth():
    return os.environ.get("BEARER_TOKEN")


def create_url(**kwargs):
    # Specify the usernames that you want to lookup below
    # You can enter up to 100 comma-separated values.
    usernames = kwargs.get("usernames","")
    user_fields = "user.fields=description,verified,profile_image_url,entities,public_metrics"
    username = kwargs.get("username","")
    #public_metrics.followers_count, public_metrics.following_count, public_metrics.tweet_count, profile_image_url, entities.url.urls.expanded_url
    # User fields are adjustable, options include:
    # created_at, description, entities, id, location, name,
    # pinned_tweet_id, profile_image_url, protected,
    # public_metrics, url, username, verified, and withheld
    if username != "":
        url = "https://api.twitter.com/2/users/by/username/{}?{}".format(username, user_fields)
    else:
        url = "https://api.twitter.com/2/users/by?{}&{}".format(usernames, user_fields)
    return url

def create_url_for_tweets(username):
    query = "from:" + str(username)
    # Tweet fields are adjustable.
    # Options include:
    # attachments, author_id, context_annotations,
    # conversation_id, created_at, entities, geo, id,
    # in_reply_to_user_id, lang, non_public_metrics, organic_metrics,
    # possibly_sensitive, promoted_metrics, public_metrics, referenced_tweets,
    # source, text, and withheld
    tweet_fields = "tweet.fields=author_id"
    url = "https://api.twitter.com/2/tweets/search/recent?query={}&{}".format(
        query, tweet_fields
    )
    return url


def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers


def connect_to_endpoint(url, oauth):
    response = requests.request("GET", url, auth=oauth)
    return response.json()

def auth(url):
    oauth = OAuth1(consumer_key, consumer_secretkey, access_token, access_secret)
    return oauth

def get_users_by_listof_usernames():
    usernames = "usernames=iamsrk,narendramodi,PMOIndia,SrBachchan,KanganaTeam,akshaykumar,iHrithik,sachin_rt"
    url = create_url(usernames=usernames)
    authorise = auth(url)
    json_response = connect_to_endpoint(url, authorise)
    return json.dumps(json_response, indent=4, sort_keys=True)

def get_user_by_username(username):
    user_url = create_url(username=username)
    auth_for_user = auth(user_url)
    json_response = connect_to_endpoint(user_url, auth_for_user)

    tweets_url = create_url_for_tweets(username)
    auth_for_user_tweets = auth(tweets_url)
    json_response_tweets = connect_to_endpoint(tweets_url, auth_for_user_tweets)
    print (type(json_response_tweets))
    print (json_response_tweets)
    user_data = json_response.update(json_response_tweets)
    return json.dumps(json_response_tweets, indent=4, sort_keys=True)

    
#print (get_user_by_username("username_richie"))
#def get_twitter_data():
    #oauth = OAuth1(consumer_key, consumer_secretkey, access_token, access_secret)

    #bearer_token = auth()
    #url = get_user_by_username()
    #url = get_users_by_listof_usernames()
    #headers = create_headers(bearer_token)
    #json_response = connect_to_endpoint(url, headers)
    #json_response = connect_to_endpoint(url, oauth)
    #return json.dumps(json_response, indent=4, sort_keys=True)