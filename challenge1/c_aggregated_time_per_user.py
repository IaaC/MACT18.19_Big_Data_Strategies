
# license: Creative Commons License
# Title: Big data strategies seminar. Challenge 1. www.iaac.net
# Created by: Diego Pajarito
#
# is licensed under a license Creative Commons Attribution 4.0 International License.
# http://creativecommons.org/licenses/by/4.0/
# This script uses pandas for data management for more information visit; pandas.pydata.org/
# The concept of dimension is usually applied to space and time. It can also be extended to other
# thematic domains.

import pandas as pd
from pandas import plotting
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
plotting.register_matplotlib_converters()


######################################################
# Read the different files starting with the last file
tweets = pd.read_csv('../data/twitter/tweets.csv')

######################################################
# Formatting time data
tweets['datetime'] = pd.to_datetime(tweets['timestamp_ms'], unit='ms')
tweets['date'] = tweets['datetime'].dt.date
tweets['week'] = tweets['datetime'].dt.week
tweets['hour'] = tweets['datetime'].dt.hour
tweets['day_of_week'] = tweets['datetime'].dt.dayofweek


######################################################
# Aggregating data, posting frequency per week/day
grouped_date = tweets.groupby(['city', 'date'])
grouped_date = grouped_date['id'].count()
grouped_date.unstack(level=0).hist(bins=20)
plt.show()

grouped_dow = tweets.groupby(['city', 'day_of_week'])
grouped_dow = grouped_dow['id'].count()
grouped_dow.unstack(level=0).plot(kind='bar', subplots=True)
plt.show()

grouped_hour = tweets.groupby(['city', 'hour'])
grouped_hour = grouped_hour['id'].count()
grouped_hour.unstack(level=0).plot(subplots=True)
plt.show()


# Aggregating data, posting frequency per user
tweets_length = tweets.groupby(['city', 'user_screen_name']).agg({'date': lambda x: x.max() - x.min(), 'id': 'count'})
tweets_length.columns = ['days_tweeting', 'tweets']
tweets_length['days_tweeting'] = tweets_length['days_tweeting'].dt.days
tweets_length['tweets_per_day'] = tweets_length['tweets'] / tweets_length['days_tweeting']
tweets_length.plot(kind='scatter', x='days_tweeting', y='tweets')
plt.show()
tweets_length.plot(kind='scatter', x='days_tweeting', y='tweets_per_day')
plt.show()


print('Some examples shown')

