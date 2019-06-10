
# license: Creative Commons License
# Title: Big data strategies seminar. Challenge 1. www.iaac.net
# Created by: Diego Pajarito
#
# is licensed under a license Creative Commons Attribution 4.0 International License.
# http://creativecommons.org/licenses/by/4.0/
# This script uses pandas for data management for more information visit; pandas.pydata.org/
# This script uses seaborn to enhance and simplify the way to plot data
# This script uses regular expressions and the re library
# thematic domains.

import pandas as pd
from pandas import plotting
import matplotlib.pyplot as plt
import seaborn as sns
import re
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

# Counting tweets per city and language
lang_of_int = ['en', 'es', 'ca', 'ja', 'fr', 'pt', 'und'] # ['en', 'es', 'ca', 'ja', 'de', 'fr', 'it', 'pt', 'ar', 'ko', 'und']
lang_pattern = '|'.join(lang_of_int)
tweets_lang = tweets.loc[:, ['language', 'city']]
tweets_lang['lang_of_int'] = tweets_lang['language']
tweets_lang.loc[(tweets_lang['lang_of_int'].str.contains(lang_pattern)) == False, 'lang_of_int'] = 'other'
grouped_city_lang = tweets_lang.groupby(['city', 'lang_of_int'])
grouped_city_lang = grouped_city_lang['lang_of_int'].count()
grouped_city_lang.unstack(level=0).plot(kind='bar')
plt.show()

# Tweets size and words
tweets = tweets.loc[:, ['id', 'city', 'text', 'language']]
tweets['text_total_words'] = tweets['text'].str.split().str.len()
tweets['text_total_characters'] = tweets['text'].str.len()

languages = tweets['language'].unique()
tweets['lang_of_int'] = ''
tweets['lang_of_int'] = tweets['language'].apply(lambda x: x if re.search(lang_pattern, x) else 'other')

grouped_words_len = tweets.groupby(['city', 'lang_of_int', 'text_total_words', 'text_total_characters'])
grouped_words_len = grouped_words_len['id'].count()
grouped_words_len = grouped_words_len.reset_index()
grouped_words_len.columns = ['city', 'language', 'words', 'characters', 'tweets']
sns.scatterplot(x='characters', y='words', alpha=0.3, hue='language', size=1, data=grouped_words_len)
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
