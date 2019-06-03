
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
# Aggregating data, tweets frequency per user
grouped_user = tweets.groupby(['city', 'user_screen_name'])
tweets_user = grouped_user['id'].count()
tweets_user.unstack(level=0).hist(bins=100)
plt.show()


######################################################
# Aggregating data, posting frequency per city
days = max(tweets['date']) - min(tweets['date'])
weeks = days.days / 7
months = days.days / 30
tweets_user = tweets_user.to_frame().reset_index()
tweets_user.columns = ['city', 'user_screen_name', 'tweets']
tweets_user['tweets'] = tweets_user['tweets'] / days.days
tweets_user['per_day'] = 'a'
tweets_user.loc[tweets_user['tweets'] >= months, 'per_day'] = 'b'
tweets_user.loc[tweets_user['tweets'] >= weeks, 'per_day'] = 'c' #'c. < 1 per day'
tweets_user.loc[tweets_user['tweets'] >= days.days, 'per_day'] = 'd'#'d. 1+ per day'
tweets_user.loc[tweets_user['tweets'] >= days.days * 2, 'per_day'] = 'e'#'e. 2+ per day'

# tweets_user = tweets_user.loc[tweets_user['tweets'] >= weeks]

tweets_cities_frequency = tweets_user.groupby(['city', 'per_day']).count()
# Pie charts per city showing the frequency of tweets per user per city
tweets_cities_frequency['tweets'].unstack(level=0).plot(kind='pie', subplots=True, labels=None)
a = mpatches.Patch(color='blue', label='Not even Monthly')
b = mpatches.Patch(color='orange', label='Monthly')
c = mpatches.Patch(color='green', label='Weekly')
d = mpatches.Patch(color='red', label='Daily')
e = mpatches.Patch(color='purple', label='Two+ tweets per day')
plt.legend(handles=[a, b, c, d, e], loc=2)
plt.show()

# Bar chart showing the frequency of tweets per user
tweets_cities_frequency.unstack(level=1).plot(kind='bar', y='tweets')
plt.legend(handles=[a, b, c, d, e])
plt.show()


print('Some examples shown')

