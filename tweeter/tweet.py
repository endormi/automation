"""

author: @endormi

Automated tweeter

"""

import tweepy
import os


auth = tweepy.OAuthHandler(os.getenv("TWITTER_API_KEY"), os.getenv("TWITTER_API_SECRET_KEY"))
auth.set_access_token(os.getenv("TWITTER_ACCESS_TOKEN"), os.getenv("TWITTER_ACCESS_TOKEN_SECRET"))

api = tweepy.API(auth)
tweet = str(input("Tweet: \n"))

try:
    api.update_status(tweet)
    print("Tweeted!")
except tweepy.TweepError as error:
    if error.api_code == 187:
        print('Tweet already exists.')
    else:
        raise error
