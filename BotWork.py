import requests
import twitter
import json
import config


api = twitter.Api(consumer_key=config.CONSUMER_KEY,
                  consumer_secret=config.CONSUMER_SECRET,
                  access_token_key=config.ACCESS_TOKEN,
                  access_token_secret=config.ACCESS_TOKEN_SECRET)


search=api.GetSearch(term='theresa may', count=100, result_type="recent")

negCount = 0

for s in search:
    analysisreq = requests.post("http://text-processing.com/api/sentiment/", data=s.text)

analysisreq = requests.post("http://text-processing.com/api/sentiment/", data=payload)

analysis=json.loads(analysisreq.text)

update= "beep boop I'm a bot, theresa may's negativity is at: " + str(analysis['probability']['neg'])

api.PostUpdate(update)
