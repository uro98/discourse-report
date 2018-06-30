import tweepy
from tweepy import OAuthHandler
import csv
from textblob import TextBlob
import sys

reload(sys)
sys.setdefaultencoding('utf8')

consumer_key = ''
consumer_secret = ''
access_key = ''
access_secret = ''
auth = OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_key, access_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

def get_approval_ratio(person, number):
    tweets = api.search(person,'en',count = number)

    positive = 0
    neutral = 0
    negative = 0
    for tweet in tweets:
        text = TextBlob(tweet.text)
        polarity = text.sentiment.polarity
        if polarity>0:
            positive += 1
        elif polarity<0:
            negative += 1
        else:
            neutral += 1

    if negative==0:
        negative = 1
    ratio = (positive*100.0)/(positive+negative)

    return [positive, neutral, negative, ratio]
