import tweepy
import time
from datetime import datetime,timezone
import urllib

A_TOKEN = '1661120084021051392-8BwcJoJO91n965L0Fq0HqxcEkrToZf'
A_SECRET = 'BYwPFKwRZJOfN3WJByKKZEScgSLYgXmv1jFjAxjqSZ1b6'
CO_TOKEN = 'RE8dThVaC4ocBSUy7KAhuwXKo'
CO_SECRET = 'O5EiSAIjP1qfVwi88drRJ0b991xSqd3Nh4i5vjhLaHIYBRhpUA'
CL_TOKEN = 'V3BmclhSa250cE9VT1RWYVNnVXE6MTpjaQ'
CL_SECRET = 'wsETWgspKnnhnSgQmqv-cU6kqJAAPTsZPUJF3vw4Yb9AAwpy3C'

client = tweepy.Client(consumer_key=CO_TOKEN, consumer_secret=CO_SECRET, access_token=A_TOKEN, access_token_secret=A_SECRET)


now_utc = str(datetime.now(timezone.utc))

tweet = 'The time is now: ' + now_utc + '\nThe Daily Space Weather Forecast Discussion has been published. \nFor more Information please visit: \nhttps://services.swpc.noaa.gov/text/discussion.txt'

response = client.create_tweet(text=tweet)
print(response)
