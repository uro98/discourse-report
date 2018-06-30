import requests
import twitter
import json


api = twitter.Api(consumer_key='',
                  consumer_secret='',
                  access_token_key='',
                  access_token_secret='')


search=api.GetSearch(term='theresa may', count=100, result_type="recent")

stext=[s.text for s in search]

' '.join(stext)

payload={'text':' '.join(stext)}

analysisreq = requests.post("http://text-processing.com/api/sentiment/", data=payload)

analysis=json.loads(analysisreq.text)
print(analysis['probability']['neg'])


update= "beep boop I'm a bot jane's making, theresa may's negativity is at: " + str(analysis['probability']['neg'])

api.PostUpdate(update)
