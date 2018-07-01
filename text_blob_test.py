from text_blob_analysis import *
import tweepy
from tweepy import OAuthHandler
import time
from statistics import mean
import sys

sys.setdefaultencoding('utf8')

consumer_key = config.CONSUMER_KEY
consumer_secret = config.CONSUMER_SECRET
access_key = config.ACCESS_TOKEN
access_secret = config.ACCESS_TOKEN_SECRET
auth = OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_key, access_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)


politicians = ["Theresa May", "Jeremy Corbyn", "Boris Johnson", "Nicola Sturgeon", "Sadiq Khan", "Philip Hammond", "John Bercow", "Michel Barnier", "Arlene Foster"]
number = 100
includeRetweets = True

negatives={"Theresa May":0, "Jeremy Corbyn":0, "Boris Johnson":0, "Nicola Sturgeon":0, "Sadiq Khan":0, "Philip Hammond":0, "John Bercow":0, "Michel Barnier":0}
totals={"Theresa May":0, "Jeremy Corbyn":0, "Boris Johnson":0, "Nicola Sturgeon":0, "Sadiq Khan":0, "Philip Hammond":0, "John Bercow":0, "Michel Barnier":0}



while 1:
    for politician in politicians:
        [negative,total] = get_approval_ratio(politician, number, includeRetweets)

        negatives[polititcan]+=neg
        totals[politician]+=total

    if time.localtime()['tm_min']==0 or time.localtime()['tm_min']==30:
        ratios=[round(negatives['key']/totals['key'] , 2) for key in politician]
        status="Theresa May: {}\n Jeremy Corbyn:{}\nBoris Johnson:{}\nNicola Sturgeon:{}\nSadiq Khan:{}\nPhilip Hammond:{}\nJohn Bercow:{}\nMichel Barnier".format()

        print(status)

        for key in politicians:
            negatives[key]=0
            totals[key]=0
    time.sleep(60)
