TRACK_TERMS = ['trump','biden', 'donald trump', 'joe biden']
CONNECTION_STRING = "sqlite:///tweets.db"
CSV_NAME = "tweets.csv"
TABLE_NAME = "election"
# You should input your own keys and secrets from Twitter API
TWITTER_APP_KEY = 'twitter api key' 
TWITTER_APP_SECRET = 'twitter app secret'
TWITTER_KEY = 'key'
TWITTER_SECRET = 'secret'

try:
	from private import *
except Exception:
	pass
