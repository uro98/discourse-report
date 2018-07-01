import config
from text_blob_analysis import *
import tweepy
from tweepy import OAuthHandler
import time


import sys

sys.setdefaultencoding('utf8')

consumer_key = config.CONSUMER_KEY
consumer_secret = config.CONSUMER_SECRET
access_key = config.ACCESS_TOKEN
access_secret = config.ACCESS_TOKEN_SECRET
auth = OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_key, access_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)


politicians = ["Theresa May", "Jeremy Corbyn", "Nicola Sturgeon",  "Arlene Foster","Tim Farron", "Caroline Lucas"]
number = 100
includeRetweets = True

negatives={politician : 0 for politician in politicians}
totals={politician : 0 for politician in politicians}


while 1:
    if time.localtime()[4]==5 or time.localtime()[4]==30:
        ratios={key:round(100*negatives[key]/totals[key] , 2) for key in politicians}
        status="Negative tweets as percentage of overall: \n "

        for politician in politicians:
            status+="\n"+politician+": "+str(ratios[politician])+"%"

        print(status)

        api.update_status(status)
        for key in politicians:
            negatives[key]=0
            totals[key]=0

    for politician in politicians:
        [negative,total] = get_approval_ratio(politician, number, includeRetweets)

        negatives[politician]+=negative
        totals[politician]+=total

        print(politician ,negatives[politician], "/" ,totals[politician])

    time.sleep(60-time.localtime()[5])
