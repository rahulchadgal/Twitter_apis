import tweepy,json
access_token="1392409211846361089-q249t3asSAvrKVmqy0QQslgRjUofEp"
access_token_secret="fCUoDerE74yaDGsKgcWkjYT0aGRaTjcnUTGOrKU88i2vJ"
consumer_key="xeojdPxrvJBtaMdEq6bPjd19m"
consumer_secret="eHWbvS7sqOTeaU4MCoV4RtSsBAKJfAHUSfNFlk6QvrLrWk7Zk9"
auth= tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

tweet_list=[]
class MyStreamListener(tweepy.StreamListener):
    def __init__(self,api=None):
        super(MyStreamListener,self).__init__()
        self.num_tweets=0
        self.file=open("tweet.txt","w")
    def on_status(self,status):
        tweet=status._json
        self.file.write(json.dumps(tweet)+ '\n')
        tweet_list.append(status)
        self.num_tweets+=1
        if self.num_tweets<1000:
            return True
        else:
            return False
        self.file.close()

l = MyStreamListener()
stream =tweepy.Stream(auth,l)
stream.filter(track=[''])

tweets_data_path='tweet.txt'
tweets_data=[]
tweets_file=open(tweets_data_path,"r")

for line in tweets_file:
    tweet=json.loads(line)
    tweets_data.append(tweet)
tweets_file.close()
print(tweets_data[0])
