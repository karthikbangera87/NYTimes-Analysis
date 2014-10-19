from nytimesarticle import articleAPI
import json
api = articleAPI('5cd14aa7c4f0c21e6773773aec5271cc:5:70018051')

testfile = open("foo.txt","ab")

for i in range(1,101):
	articles = api.search(q='ebola',page=i)
	articles =json.dumps(articles)
	testfile.write(articles)











