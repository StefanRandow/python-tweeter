import tweepy
import time
from datetime import datetime,timezone
import urllib

A_TOKEN = 'ENTER_INFO_HERE'
A_SECRET = 'ENTER_INFO_HERE'
CO_TOKEN = 'ENTER_INFO_HERE'
CO_SECRET = 'ENTER_INFO_HERE'
CL_TOKEN = 'ENTER_INFO_HERE'
CL_SECRET = 'ENTER_INFO_HERE'

client = tweepy.Client(consumer_key=CO_TOKEN, consumer_secret=CO_SECRET, access_token=A_TOKEN, access_token_secret=A_SECRET)


now_utc = str(datetime.now(timezone.utc))

tweet = 'The time is now: ' + now_utc + '\nThe Daily Space Weather Forecast Discussion has been published. \nFor more Information please visit: \nhttps://services.swpc.noaa.gov/text/discussion.txt'

response = client.create_tweet(text=tweet)
print(response)
