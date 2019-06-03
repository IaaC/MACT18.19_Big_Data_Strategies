
# license: Creative Commons License
# Title: Big data strategies seminar. Challenge 1. www.iaac.net
# Created by: Diego Pajarito
#
# is licensed under a license Creative Commons Attribution 4.0 International License.
# http://creativecommons.org/licenses/by/4.0/
# This script uses pandas for data management for more information visit; pandas.pydata.org/
# This script uses seaborn to enhance and simplify the way to plot data
# thematic domains.

import pandas as pd
from pandas import plotting
import matplotlib.pyplot as plt
import seaborn as sns
plotting.register_matplotlib_converters()


######################################################
# Read the different files starting with the last file
tweets = pd.read_csv('../data/twitter/tweets.csv')

######################################################
# Formatting time data

# Raw data in milliseconds
print('This is an example of tweet text')
print(tweets['text'][100])

# Describing text using different metrics
print('Now the same text expressed in terms of length')
print('This text has %i characters' % len(tweets['text'][100]))
print('This text has %i words' % len(tweets['text'][100].split()))
print('This text uses %i characters per word' % (len(tweets['text'][100])/len(tweets['text'][100].split())))


######################################################
# Graphical representation of text features
tweets['text_total_words'] = tweets['text'].str.split().str.len()
tweets['text_total_characters'] = tweets['text'].str.len()
# tweets.plot(kind='scatter', x='text_total_characters', y='text_total_words')
# plt.show()


# Graphical representing adding color
languages = tweets['language'].unique()
#sns.lmplot('text_total_words', 'text_total_characters', data=tweets, hue='language', fit_reg=False)
tweets.plot(kind='hexbin', x='text_total_characters', y='text_total_words')
plt.show()


print('Some examples shown')


















print('Your data set has %i objects' % len(tweets))
print('Tweets are recorded between %s and %s)' % (str(tweets['datetime'].min()), str(tweets['datetime'].max())))

######################################################
# Aggregating data
grouped_city_day = tweets.groupby(['city', 'date'])


######################################################
# Creating simple graphs based on the grouped data
# the unstack function helps to use the indicated index as axes
grouped_city_day['id'].count().unstack(level=0).plot(kind='line')
grouped_city_day['id'].count().unstack(level=0).plot(kind='area', alpha=0.4)
grouped_city_day['id'].count().unstack(level=0).plot(kind='area', subplots=True)

grouped_city_day['id'].count().unstack(level=1).plot(kind='line', subplots=True)
grouped_city_day['id'].count().unstack(level=1).plot(kind='line')

print('Some examples shown')
