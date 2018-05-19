import tweepy
import csv
import time
import sys


accountvar - "realDonaldTrump"
print("serching for followers of" + accountvar)

consumer_key = "osRJEPEzaRosZCvB6fjknpgYW"
consumer_secret = "awJeYW3pV3zUE2R9bw44po1fANGhtkcKy6OCmEQhz7Q2NLG7Nv"
access_token = "984073643885031424-fHKjG32Dj3EXPXxGblUloAxaBQAEMTF"
access_token_secret = "Myevw0DMUunrBA7h98BDBJWOqpEp3G7pgcyewqrs1dU4e"

auth = tweepy.OAutHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api =tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

#Passing parameters into the API method,we can not pass the parameters directly into the method. Instead we pass the parameters into the Cursor
users = tweepy.Cursor(api.followers,screen_name = accountvar).items()  #api.followers is a method
count = 0
errorCount = 0
outputfilecsv = accountvar +"followers.csv"
fc = csv.writer(open(outputfilecsv.'w'))
fc.writerow(["screen_name","followers_count","statuses_count","location","geo_enabled"])
while True:
  try:
       user = next(users)
       count+=1
    #use count-break during dev to avoid twitter restrictionship
  except tweepy.TweepError:
        print("sleeping"...)
        time.sleep(60*16)
        user = next(users)
  except StopItreation:
         break
  try:
         print ("@" + user.screen_name + " has " + str(user.followers_count) +\
              " followers, has made "+str(user.statuses_count)+" tweets and location=" +\
              user.location+" geo_enabled="+str(user.geo_enabled)+" count="+str(count))
              
         fc.writerow([user.screen_name, str(user.followers_count), str(user.statuses_count), user.location, str(user.geo_enabled)])
    except UnicodeEncodeError:
        errorCount += 1
        print ("UnicodeEncodeError,errorCount ="+str(errorCount))

print("Completed,errorCount=" +str(errorCount)+"total users="+str(count))

   
   
        
    
    
