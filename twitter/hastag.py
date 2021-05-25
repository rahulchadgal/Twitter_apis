
import pandas as pd
import tweepy


def printtweetdata(n, ith_tweet):
	print()
	print(f"Tweet {n}:")
	print(f"Username:{ith_tweet[0]}")
	print(f"Description:{ith_tweet[1]}")
	print(f"Location:{ith_tweet[2]}")
	print(f"Following Count:{ith_tweet[3]}")
	print(f"Follower Count:{ith_tweet[4]}")
	print(f"Total Tweets:{ith_tweet[5]}")
	print(f"Retweet Count:{ith_tweet[6]}")
	print(f"Tweet Text:{ith_tweet[7]}")
	print(f"Hashtags Used:{ith_tweet[8]}")


def scrape(words, date_since, numtweet):

	db = pd.DataFrame(columns=['username', 'description', 'location', 'following',
							'followers', 'totaltweets', 'retweetcount', 'text', 'hashtags'])

	tweets = tweepy.Cursor(api.search, q=words, lang="en",
						since=date_since, tweet_mode='extended').items(numtweet)


	list_tweets = [tweet for tweet in tweets]

	i = 1

	for tweet in list_tweets:
		username = tweet.user.screen_name
		description = tweet.user.description
		location = tweet.user.location
		following = tweet.user.friends_count
		followers = tweet.user.followers_count
		totaltweets = tweet.user.statuses_count
		retweetcount = tweet.retweet_count
		hashtags = tweet.entities['hashtags']


		try:
			text = tweet.retweeted_status.full_text
		except AttributeError:
			text = tweet.full_text
		hashtext = list()
		for j in range(0, len(hashtags)):
			hashtext.append(hashtags[j]['text'])

		ith_tweet = [username, description, location, following,
					followers, totaltweets, retweetcount, text, hashtext]
		db.loc[len(db)] = ith_tweet

		printtweetdata(i, ith_tweet)
		i = i+1
	filename = 'scraped_tweets.csv'

	db.to_csv(filename)


if __name__ == '__main__':

	consumer_key = "xeojdPxrvJBtaMdEq6bPjd19m"
	consumer_secret = "eHWbvS7sqOTeaU4MCoV4RtSsBAKJfAHUSfNFlk6QvrLrWk7Zk9"
	access_key = "1392409211846361089-q249t3asSAvrKVmqy0QQslgRjUofEp"
	access_secret = "fCUoDerE74yaDGsKgcWkjYT0aGRaTjcnUTGOrKU88i2vJ"
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)

    words = 'indawithpalentine'
    date_since= '2021-05-12'

	'''print("Enter Twitter HashTag to search for")
	words = input()
	print("Enter Date since The Tweets are required in yyyy-mm--dd")
	date_since = input()'''

	numtweet = 100
	scrape(words, date_since, numtweet)
	print('Scraping has completed!')
