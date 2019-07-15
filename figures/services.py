import datetime
import numpy as np

import tweepy

from . import tweepy_keys
from .models import Comparison

auth = tweepy.OAuthHandler(tweepy_keys.consumer_key, tweepy_keys.consumer_secret)
auth.set_access_token(tweepy_keys.access_token, tweepy_keys.access_token_secret)

api = tweepy.API(auth)
num_tweets = 25

def check_user_exists(user):
    try:
        api.get_user(user)
        return True
    except:
        return False

def get_tweets(username):
    ret = ''
    user = api.get_user(username)
    statuses = tweepy.Cursor(api.user_timeline, id=user.id).items(num_tweets)
    for status in statuses:
        if 'RT @' not in status.text:
            ret += status.text
    return ret
            
def get_tweet_stats(username):
    ret = []
    user = api.get_user(username)
    statuses = tweepy.Cursor(api.user_timeline, id=user.id).items(num_tweets)
    for status in statuses:
        if 'RT @' not in status.text:
            ret.append({'rts': status.retweet_count,'favs': status.favorite_count})
    return ret

def process_users(user1, user2):
    user1_stats = get_tweet_stats(user1)
    user2_stats = get_tweet_stats(user2)
    Comparison.objects.create(user1=user1, user2=user2, user1_stats=user1_stats, user2_stats=user2_stats)
