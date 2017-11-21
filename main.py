import matplotlib
import tweepy
from textblob import TextBlob
import pandas as pd
import numpy as np
import re
# For plotting and visualization:
from IPython.display import display
import matplotlib.pyplot as plt
import seaborn as sns
#  Twitter infos from API
auth = tweepy.OAuthHandler('rYWoIkm6Z4fYmaSEv4vt0XubV', 'VLNUUJhZAuJ8i6HmX8a9EMcGFPsGbblJysmWvz0HNJaJbwaaj4')
auth.set_access_token('932538987759017984-6c4TqU6xhrxwUWpPwqkplEg04ZpJos6', 'D10qcxLv4ZJaI3hvuQ7nW6WYNcEcThkYvoHqhAtEuFzcG')
# Python terminal display settings to show all output
pd.set_option('display.height', 10000)
pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 100000)
pd.set_option('display.width', 10000)

api = tweepy.API(auth)
# Get the tweets from the API
public_tweets = api.search('realDonaldTrump')
# Get text of the tweet and then analyse it
number = 0
tweets = api.user_timeline(screen_name="realDonaldTrump", count=200)
for t in tweets[:10]:
    number+=1
    print(number)
    print(t.text)
    analyser = TextBlob(t.text)
    print(analyser.sentiment)
# Create a pandas dataframe to hold the tweets
data = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])
# We add relevant data:
data['user']  = np.array([tweet.user.name for tweet in tweets])
data['Date'] = np.array([tweet.created_at for tweet in tweets])
data['Source'] = np.array([tweet.source for tweet in tweets])
data['Likes']  = np.array([tweet.favorite_count for tweet in tweets])
data['RTs']    = np.array([tweet.retweet_count for tweet in tweets])
# We display the first 10 elements of the dataframe:
display(data.head(10))
# Let's get the most likes and rts
num_likes = np.max(data['Likes'])
num_RTs  = np.max(data['RTs'])

most_likes = data[data.Likes == num_likes].index[0]
most_retweets  = data[data.RTs == num_RTs].index[0]

# Max FAVs:
print("Most liked tweets: \n{}".format(data['Tweets'][most_likes]))
print("Likes ")
print(num_likes)

# Max RTs:
print("Most retweeted tweet \n{}".format(data['Tweets'][most_retweets]))
print("Retweets")
print(num_RTs)

