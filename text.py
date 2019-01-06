import tweepy
from credentials import *
from time import sleep
import random
from datetime import datetime as dt

#accessing OAuth and integrating with API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#reads lines from one book
book1 = open("C:\\your_directory\\ernest.txt", 'r')
read_it = book1.readlines()
book1.close()

#reads lines from another book
book = open("C:\\your_directory\\odyssey.txt", 'r')
file_lines = book.readlines()
book.close()

#tweet lines from book
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

        sleep(250)
def tweet2():
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
    sleep(100)


#follows anyone who follows me
for follower in tweepy.Cursor(api.followers).items():
    follower.follow()

#looks up a specific users followers and follows them
ids = []
for page in tweepy.Cursor(api.followers_ids, screen_name="any_user").pages():
    ids.extend(page)
    sleep(30)
    #makes userID list into text file
    with open('user_ids.txt', 'w') as file:
        for i in ids:
            file.write("%s\n" % i)

user_list = open('C:\\directory\\user_ids.txt', "r")
open_user = user_list.readlines()
user_split = user_list.read().splitlines()

for i in open_user:
    api.create_friendship(i)
user_list.close()

#adds screen names to text doc
my_followers = []
def screen_name():
    for i in open_user:
        names = api.get_user(i)
        handels = names.screen_name
        print(handels)
        my_followers.append(handels)
        with open('screen_names.txt', 'w') as f:
            for i in my_followers:
                f.write(i+"\n")
        #sleep(10)

#unneccessary to do this but possibly needed later on
sn = open('C:\\screen_names.txt', "r")
snpick = sn.readlines()

#tweets one random user once a day the current date and datetime
def send_date():
    while True:
        g= datetime.now()
        i = random.choice(my_followers)
        api.update_status("@%s" "\n%s" % (i, g))
        sleep(86400)

#Running functions created above
tweet1()
tweet2()
screen_name()
send_date()
