import settings
import tweepy
import dataset
from textblob import TextBlob 
from sqlalchemy.exc import ProgrammingError
import json

db = dataset.connect(settings.CONNECTION_STRING)

class StreamListener(tweepy.StreamListener):

	def on_status(self,status):
		if (status.retweeted) or ('RT' in status.text):
		#if status.retweeted == True:
			return
		print(status.text)
		description = status.user.description
		loc = status.user.location
		text = status.text
		name = status.user.screen_name
		id_str = status.id_str
		created = status.created_at
		favorites = status.favorite_count
		retweets = status.retweet_count
		blob = TextBlob(text)
		sent = blob.sentiment

		table = db[settings.TABLE_NAME]
		try:
			table.insert(dict(
				id_str=id_str,
				user_name=name,
				user_description=description,
				user_location=loc,
				user_created=created,
				favorite_count= favorites,
				retweet_count=retweets,
				text=text,
				polarity=sent.polarity,
				subjectivy=sent.subjectivity))
		
		except ProgrammingError as err:
			print(err)
	def on_error(self, status_code):
		if status_code ==420:
			return False # return False in on_data disconnects the stream

auth = tweepy.OAuthHandler(settings.TWITTER_APP_KEY, settings.TWITTER_APP_SECRET)
auth.set_access_token(settings.TWITTER_KEY, settings.TWITTER_SECRET)
api = tweepy.API(auth)

stream_listener = StreamListener()
stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
stream.filter(track=settings.TRACK_TERMS)