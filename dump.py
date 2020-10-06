import settings
import tweepy
import dataset
from textblob import TextBlob
import datafreeze #As of version dataset 1.0, module dataset is split into two packages, 
# with the data export features now extracted into a stand-alone package, datafreeze.

db = dataset.connect(settings.CONNECTION_STRING)

result = db[settings.TABLE_NAME].all()
datafreeze.freeze(result, format='csv', filename=settings.CSV_NAME)
