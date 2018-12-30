import tweepy
from credentials import *
from time import sleep

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

        while sleep != False:
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

#follows anyone who follows me
for follower in tweepy.Cursor(api.followers).items():
    follower.follow()

#looks up a specific users followers and follows them
ids = []
for page in tweepy.Cursor(api.followers_ids, screen_name="any_screen_name").pages():
    ids.extend(page)
    sleep(30)
    #makes userID list into text file
    with open('user_ids.txt', 'w') as file:
        for i in ids:
            file.write("%s\n" % i)

user_list = open("textfile.txt", "r")
open_user = user_list.readlines()
user_split = user_list.read().splitlines()

for i in open_user:
    api.create_friendship(i)
user_list.close()

#trying to get the screen anmes from user id list
#this isn't working yet
def screen_name():
    for i in open_user:
        names = list(api.get_user(i))
        with open('screen_names.txt', 'w') as f:
            for item in names:
                f.write("%s\n" % item)

api.followers(screen_name)
#tweets one random user once a day the current date and datetime
def send_date():
    i = random.choice(user_split)
    api.update_status("@"i " %s")
