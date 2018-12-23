import tweepy
from credentials import *
from time import sleep
import urllib

#accessing OAuth and integrating with API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#reads lines from one book
book1 = open("C:\\Users\\Pete\\AppData\\Local\\Programs\\Python\\Python36-32\\Projects\\twitter_bot\\ernest.txt", 'r')
read_it = book1.readlines()
book1.close()

#reads lines from another book
book = open("C:\\Users\\Pete\\AppData\\Local\\Programs\\Python\\Python36-32\\Projects\\twitter_bot\\odyssey.txt", 'r')
file_lines = book.readlines()
book.close()

#tweet lines from book1
def tweet():
    for i in file_lines:
        try:
            print(i)
            if i != '/n':
                api.update_status(i)
            else:
                pass
        except tweepy.TweepError as e:
            print(e.reason)
            continue

        sleep(10)

        while sleep != True:
            for i in read_it:
                try:
                    print(i)
                    if i != '/n':
                        api.update_status(i)
                    else:
                        pass
                except tweepy.TweepError as e:
                    print(e.reason)
                    continue
            sleep(5)

tweet()
