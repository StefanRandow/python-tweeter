import tweepy
import time
from datetime import datetime,timezone
import urllib

A_TOKEN = 'ENTER_YOUR_ACCESS_TOKEN'
A_SECRET = 'ENTER_YOUR_ACCESS_SECRET'
CO_TOKEN = 'ENTER_YOUR_CONSUMER_TOKEN'
CO_SECRET = 'ENTER_YOUR_CONSUMER_SECRET'
CL_TOKEN = 'ENTER_YOUR_CLIENT_TOKEN'
CL_SECRET = 'ENTER_YOUR_CLIENT_SECRET'

client = tweepy.Client(consumer_key=CO_TOKEN, consumer_secret=CO_SECRET, access_token=A_TOKEN, access_token_secret=A_SECRET)



def get_proton():
    # Set up the URL for the text file
    url = "https://services.swpc.noaa.gov/text/ace-swepam.txt"
    
    # Download the text file
    response = urllib.request.urlopen(url)
    data = response.read().decode()
    
    # Split the text file into lines
    lines = data.split("\n")

    # Extract the most recent solar wind data from the second-to-last line
    last_line = lines[-2]
    fields = last_line.split()

    # Extract the solar wind speed, density, and temperature from the fields
    s = float(fields[6])
    density = str(fields[7])
    speed = str(fields[8])
    temperature = str(fields[9])
    
    
    #returning values
    return s, speed, density, temperature

now_utc = str(datetime.now(timezone.utc))
s, speed, density, temperature = get_proton()
if s == 0 or s ==1 :
    tweet = 'The time is now: ' + now_utc + '\nThe current solar wind speed is: ' + speed + 'km/s' + '\nThe current solar wind density is: ' + density + 'p/cc' + '\nThe current solar wind tempurature is: ' + temperature + 'K'

else:
    tweet = 'The time is now: ' + now_utc + '\nLatest ACE Solar Wind Data is not available, for more information visit: https://services.swpc.noaa.gov/text/ace-swepam.txt'

response = client.create_tweet(text=tweet)
print(response)