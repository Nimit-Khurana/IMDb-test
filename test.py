from script import movie_query
import json

data = movie_query("avengers")

#print (type(data))
#print (data[0])
#print ("##"*10)
#print (type(json.loads(data)))
print (json.loads(data))
#print (type(json.dumps(data)))
#print (type(data))

from movie_db import movie,return_search_data
from flaskk import db

print (return_search_data("avengers"))
