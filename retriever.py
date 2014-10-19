from nytimesarticle import articleAPI
import json
from secret import APIKey
api = articleAPI(APIKey)

testfile = open("foo.txt","ab")

for i in range(1,101):
	articles = api.search(q='ebola',page=i)
	articles =json.dumps(articles)
	testfile.write(articles)











