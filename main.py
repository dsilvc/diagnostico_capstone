import json
import os

def top_retweeted(tweets):
    tweets_set = set()
    for tweet in tweets:
        tweets_set.add(tweet["id"])

def top_users(tweets):

    return

def top_days(tweets):

    return

def top_hashtag(tweets):

    return

def main():

    farmers = [json.loads(line) for line in open('farmers_tweets.json','r')]
    return

main()