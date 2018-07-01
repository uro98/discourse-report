#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

lastratios=0;

politicians = ["Theresa May", "Jeremy Corbyn", "Nicola Sturgeon",  "Arlene Foster","Tim Farron",     "Caroline Lucas"]
blankspaces = ["           ", "       ",       "     ",            "          ",   "              ", "        "      ]
number = 100
includeRetweets = True

negatives={politician : 0 for politician in politicians}
totals={politician : 0 for politician in politicians}


while 1:
    if time.localtime()[4]==05 or or time.localtime()[4]==20 or time.localtime()[4]==35 or time.localtime()[4]==50:
        ratios={key:round(100*negatives[key]/totals[key] , 2) for key in politicians}
        status="Here's how many tweets about these people have been negative: \n "

        for i in range(0, len(politicians)):
            politician = politicians[i]
            if lastratios:
                if lastratios[politician]>ratios[politician]:
                    emoji="🔽"
                elif lastratios[politician]<ratios[politician]:
                    emoji= "🔼"
                else: emoji="➖"

            else:
                emoji=""


            status+="\n" + politician + ":" + blankspaces[i] + str(ratios[politician]) + "%" + emoji

        print(status)

        api.update_status(status)
        lastratios=ratios
        for key in politicians:
            negatives[key]=0
            totals[key]=0

    for politician in politicians:
        [negative,total] = get_approval_ratio(politician, number, includeRetweets)

        negatives[politician]+=negative
        totals[politician]+=total

        print(politician ,negatives[politician], "/" ,totals[politician])

    time.sleep(60-time.localtime()[5])
