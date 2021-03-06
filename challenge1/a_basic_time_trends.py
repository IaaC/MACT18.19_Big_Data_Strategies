
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
plotting.register_matplotlib_converters()


######################################################
# Read the different files starting with the last file
tweets = pd.read_csv('../data/twitter/tweets.csv')

######################################################
# Formatting time data

# Raw data in milliseconds
print('This is an example time data in milliseconds')
print(tweets['timestamp_ms'][10])

# Using pandas function to transform ms into readable datetime values (be careful with the units
print('Now the same example in a human-readable datetime format')
print(pd.to_datetime(tweets['timestamp_ms'][10], unit='ms'))

# We now add a column for data in the datetime format
tweets['datetime'] = pd.to_datetime(tweets['timestamp_ms'], unit='ms')
tweets['date'] = tweets['datetime'].dt.date


######################################################
# Using some functions to describe your data
print('Your data set has %i objects' % len(tweets))
print('Tweets are recorded between %s and %s)' % (str(tweets['datetime'].min()), str(tweets['datetime'].max())))

######################################################
# Aggregating data
grouped_city_day = tweets.groupby(['city', 'date'])


######################################################
# Creating simple graphs based on the grouped data
# the unstack function helps to use the indicated index as axes
grouped_city_day['id'].count().unstack(level=0).plot(kind='line')
plt.show()
grouped_city_day['id'].count().unstack(level=0).plot(kind='area', alpha=0.4)
grouped_city_day['id'].count().unstack(level=0).plot(kind='area', subplots=True)

grouped_city_day['id'].count().unstack(level=1).plot(kind='line', subplots=True)
grouped_city_day['id'].count().unstack(level=1).plot(kind='line')

print('Some examples shown')
