import tweepy
from tweepy import *

import pandas as pd
import csv
import re
import string
import preprocessor as p

consumer_key = "xeojdPxrvJBtaMdEq6bPjd19m"
consumer_secret = "eHWbvS7sqOTeaU4MCoV4RtSsBAKJfAHUSfNFlk6QvrLrWk7Zk9"
access_key= "1392409211846361089-q249t3asSAvrKVmqy0QQslgRjUofEp"
access_secret = "fCUoDerE74yaDGsKgcWkjYT0aGRaTjcnUTGOrKU88i2vJ"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

api = tweepy.API(auth,wait_on_rate_limit=True)

csvFile = open('file-name', 'a')
csvWriter = csv.writer(csvFile)

search_words = "beds ,bed, oxygen"      # enter your words
new_search = search_words + " -filter:retweets"

place =input("Enter the place : popular option are:Mumbai,Delhi,Bangalore and jammu");

if place.lower() == "mumbai" :
    for tweet in tweepy.Cursor(api.search,q=new_search,geocode="19.076090,72.877426,15km", count=15,lang="en",since_id=0,result_tpye = "popular").items(100):
        csvWriter.writerow([tweet.text.encode('utf-8'), tweet.user.location.encode('utf-8')])
        print (tweet.user.location.encode('utf-8'))

elif place.lower() == "delhi":
    for tweet in tweepy.Cursor(api.search,q=new_search,geocode="28.644800,77.216721,15km", count=15,lang="en",since_id=0,result_tpye = "popular").items(100):
        csvWriter.writerow([tweet.text.encode('utf-8'), tweet.user.location.encode('utf-8')])
        print (tweet.user.location.encode('utf-8'))

elif place.lower() == "banglore":
    for tweet in tweepy.Cursor(api.search,q=new_search,geocode="12.972442,77.580643,15km", count=15,lang="en",since_id=0,result_tpye = "popular").items(100):
        csvWriter.writerow([tweet.text.encode('utf-8'), tweet.user.location.encode('utf-8')])
        print (tweet.user.location.encode('utf-8'))

elif place.lower() == "jammu":
    for tweet in tweepy.Cursor(api.search,q=new_search,geocode="34.23763,75.07449,15km", count=15,lang="en",since_id=0,result_tpye = "popular").items(100):
        csvWriter.writerow([tweet.text.encode('utf-8'), tweet.user.location.encode('utf-8')])
        print (tweet.user.location.encode('utf-8'))

else:
    print ("write only from the options");


'''
for tweet in tweepy.Cursor(api.search,q=new_search,geocode="28.644800,77.216721,10km", count=15,lang="en",since_id=0,result_tpye = "popular").items(100):
    #if tweet.user.location.encode('utf-8') == b'New Delhi, India':
    csvWriter.writerow([tweet.text.encode('utf-8'), tweet.user.location.encode('utf-8')])
    print (tweet.user.location.encode('utf-8')) #tweet.created_at, tweet.user.screen_name.encode('utf-8'),
'''
