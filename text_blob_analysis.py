import tweepy
from tweepy import OAuthHandler
import csv
from textblob import TextBlob
import sys

reload(sys)
sys.setdefaultencoding('utf8')

consumer_key = config.CONSUMER_KEY
consumer_secret = config.CONSUMER_SECRET
access_key = config.ACCESS_TOKEN
access_secret = config.ACCESS_TOKEN_SECRET
auth = OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_key, access_secret)

api = tweepy.API(auth)

def get_approval_ratio(person, number, includeRetweets):
    tweets = api.search(person,'en',count = number)

    if not includeRetweets:
        indices = []
        i = 0
        for tweet in tweets:
            text = tweet.text.encode('utf-8')
            try:
                start = text[0:4]
            except:
                start = ""
            if start=="RT @":
                indices.append(i)
            i += 1
        tweets = [i for j, i in enumerate(tweets) if j not in indices]

    posCount = 0
    negCount = 0
    for tweet in tweets:
        text = TextBlob(tweet.text)
        polarity = text.sentiment.polarity
        if polarity < 0:
            negCount += 1

    return [negCount, len(tweets)]
