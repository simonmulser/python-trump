import credentials
import twitter
import csv

# 10.11.2016 to 09.04.2017
# first: Happy 241st... id=796797436752707585
# last: judge Gorsuch... id=850800045012201473
# amount: 762

oldest = 796797436752707585
newest = 850800045012201473

api = twitter.Api(consumer_key=credentials.consumer_key,
					consumer_secret=credentials.consumer_secret,
					access_token_key=credentials.access_token_key,
					access_token_secret=credentials.access_token_secret,
					tweet_mode='extended')


with open('tweets.csv', 'w') as file:
	writer = csv.writer(file, delimiter='|')
	writer.writerow(['created_at', 'text', 'source', 'retweet_count', 'favorite_count', 'link'])

with open('tweets.csv', 'a') as file:
	writer = csv.writer(file, delimiter='|')
	current = newest
	while current > oldest:
		print('{} > {}'.format(current, oldest))
		tweets = api.GetUserTimeline(user_id=25073877, since_id=796797436752707585 - 1, max_id=current, count=200)
		print('len tweets {}'.format(len(tweets)))
		for tweet in tweets:
			writer.writerow([tweet.created_at, tweet.full_text, tweet.source, tweet.retweet_count, tweet.favorite_count, 'https://twitter.com/realdonaldtrump/status/{}'.format(tweet.id)])
			current = tweet.id