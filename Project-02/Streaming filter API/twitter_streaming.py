# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

# Import the tweepy library
import tweepy

# Variables that contains the user credentials to access Twitter API 
ACCESS_TOKEN = '1045159915944378368-CoUDIOQDWQvyYWPI3wlYcZrhPQjia2'
ACCESS_SECRET = '0010BxYCdhfEiOUsQ1zLgD2cjMWQ4uRBXi8M8QelTEOdR'
CONSUMER_KEY = '1045159915944378368-CoUDIOQDWQvyYWPI3wlYcZrhPQjia2'
CONSUMER_SECRET = 'aIcZojOlY4L82INaflsEWVinP7PBDgegrWsjXh4iNS2gc43PGH'

# Setup tweepy to authenticate with Twitter credentials:

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

# Create the api to connect to twitter with your creadentials
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)
#---------------------------------------------------------------------------------------------------------------------
# wait_on_rate_limit= True;  will make the api to automatically wait for rate limits to replenish
# wait_on_rate_limit_notify= Ture;  will make the api  to print a notification when Tweepyis waiting for rate limits to replenish
#---------------------------------------------------------------------------------------------------------------------


#---------------------------------------------------------------------------------------------------------------------
# The following loop will print most recent statuses, including retweets, posted by the authenticating user and that user’s friends. 
# This is the equivalent of /timeline/home on the Web.
#---------------------------------------------------------------------------------------------------------------------

#for status in tweepy.Cursor(api.home_timeline).items(200):
#	print(status._json)

tweepy.Cursor(api.search, q="crypto", since="2016-12-01", until="2018-12-01", count=100).items()
	
#---------------------------------------------------------------------------------------------------------------------
# Twitter API development use pagination for Iterating through timelines, user lists, direct messages, etc. 
# To help make pagination easier and Tweepy has the Cursor object.
#---------------------------------------------------------------------------------------------------------------------

# Get the tweets in English that include the term “bitcoin”
# class StreamListener(tweepy.StreamListener):

#    def on_status(self, status):
#        print(status.text)
        
#    def on_error(self, status_code):
#        if status_code == 420:
#            return False

#stream_listener = StreamListener()
#stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
#stream.filter(track=["bitcoin"],languages=["en"])