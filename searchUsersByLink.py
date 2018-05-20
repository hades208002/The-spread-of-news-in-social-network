import tweepy
import csv
import json
import sys

consumer_key = "osRJEPEzaRosZCvB6fjknpgYW"
consumer_secret = "awJeYW3pV3zUE2R9bw44po1fANGhtkcKy6OCmEQhz7Q2NLG7Nv"
access_token = "984073643885031424-fHKjG32Dj3EXPXxGblUloAxaBQAEMTF"
access_token_secret = "Myevw0DMUunrBA7h98BDBJWOqpEp3G7pgcyewqrs1dU4e"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api =tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

link='http://www.affaritaliani.it/economia/guido-maria-brera-italia-vicina-alla-svolta-ma-la-politica-non-faccia-danni-541054.html'
tweetCount = 100
results = api.search(q=link, count=tweetCount)

outputfilecsv = "searched_link.csv"
fc = csv.writer(open(outputfilecsv,'w'))
fc.writerow(["id","screen_name","location","description"])
for tweet in results:
        fc.writerow([tweet.user.id,tweet.user.screen_name,tweet.user.location,tweet.user.description])
