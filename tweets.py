import tweepy 
import csv

#twitter API credentials
consumer_key = "osRJEPEzaRosZCvB6fjknpgYW"
consumer_secret = "awJeYW3pV3zUE2R9bw44po1fANGhtkcKy6OCmEQhz7Q2NLG7Nv"
access_key = "984073643885031424-fHKjG32Dj3EXPXxGblUloAxaBQAEMTF"
access_secret = "Myevw0DMUunrBA7h98BDBJWOqpEp3G7pgcyewqrs1dU4e"


def get_all_tweets(screen_name):

#authorize twitter,initialize tweepy
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_key,access_secret)
api = tweepy.API(auth)


#initialize a list to hold all the tweepy Tweets
alltweets = []

#make initial request for most recent tweets
new_tweets = api.user_timeline(screen_name = screen_name, count=200)
#save the most recent tweets,the extend() method does not return any value but add the content to existing list
alltweets.extend(new_tweets) 
#the negative index means it counts start from the end, so the -1 index is the last item of this list
#save the id of the oldest tweet minus one
oldest = alltweets[-1].id - 1

#keep grabbing tweets until there is no other tweets to be grab
while len(new_tweets) > 0:
  print("getting tweets before %s" % oldest)   #print message passing parameter
  new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
  #max_id – Returns only statuses with an ID less than (that is, older than) or equal to the specified ID.so this is for avoiding the duplication
  alltweets.extend(new_tweets)
  oldest = alltweets[-1].id - 1
  print("...%s tweets downloaded so far" % (len(alltweets)))
  
  #transform the tweepy tweets into a 2D array that will populate the csv
  outtweets = [[tweet.id_str,tweet.ceated_at,tweet.text.encode("utf-8"),tweet.retweet_count,tweet.favorite_count] for tweet in alltweets]
  
  #write the csv
  with open('%s_tweets_csv' % screen_name,'w') as f:
    writer = csv.ariter(f)  #assume that a file object called f has already been created.
    writer.writerow(["id","created_at","text","retweet_count","favorite_count"])
    writer.writerows(outtweets)
  pass    #It is used when a statement is required syntactically but you do not want any command or code to execute.

if __name__ == '__main__':
  #pass in the username of the account you want to download
  get_all_tweets("realDonaldTrump")
 
 
  
  
  
  


