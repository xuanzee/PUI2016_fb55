from __future__ import print_function
import os
import tweepy
from tweepy import OAuthHandler
import json

''' Dumps to stdout my twitter timeline in JSON format

Author: Federica Bianco lifting code from 
https://marcobonzanini.com/2015/03/02/mining-twitter-data-with-python-part-1/
'''
N = 10 # numebr of tweets to parse. Be mindful of API rate limit of 1000/hour

def process_or_store(tweet):
    '''Dumps json format tweet stream
    Arguments: 
       tweet from api
    '''
    print(json.dumps(tweet))

# collects sectret inormation from environmental variables

consumer_key = os.getenv('PUITWITKEY')
consumer_secret = os.getenv('PUITWITSECRET')
access_token = os.getenv('PUITWITACTOKEN')
access_secret = os.getenv('PUITWITACSECRET')

if not (consumer_key and consumer_secret and access_token and access_secret ):
    print ('''ERROR: Must set  the following environmental variables:
    PUITWITKEY pointing to consumer API key
    PUITWITSECRET pointing to consumer API secret
    PUITWITACTOKEN pointing to access token
    PUITWITACSECRET pointing to access token sectret
    ''')

# authenticating via OAuth
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

# activating api
api = tweepy.API(auth)
    
# collecting N items and passing them to json dumping function
for status in tweepy.Cursor(api.home_timeline).items(N):
    process_or_store(status._json) 
