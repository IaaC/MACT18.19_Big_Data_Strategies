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
import re
plotting.register_matplotlib_converters()


######################################################
# Read the different files starting with the last file
tweets = pd.read_csv('../data/twitter/tweets.csv')

######################################################
# Formatting time data
tweets['datetime'] = pd.to_datetime(tweets['timestamp_ms'], unit='ms')
tweets['date'] = tweets['datetime'].dt.date
tweets['week'] = tweets['datetime'].dt.week
tweets['day_of_week'] = tweets['datetime'].dt.dayofweek


######################################################
# Counting tweets per city and language
lang_of_ing = ['en', 'es', 'ca', 'ja']
lang_pattern = '|'.join(lang_of_ing)
tweets = tweets.loc[:, ['language', 'city', 'text', 'datetime', 'date', 'week', 'day_of_week', 'user_screen_name']]
tweets['lang_of_int'] = ''
tweets['lang_of_int'] = tweets['language'].apply(lambda x: x if re.search(lang_pattern, x) else 'other')
tweets = tweets.loc[tweets['lang_of_int'] != 'other']

tweets['words'] = tweets['text'].str.strip().str.split('[\W_]+')

rows = list()
for row in tweets[['language', 'words']].iterrows():
    r = row[1]
    for word in r['words']:
        rows.append((r['language'], word))

words = pd.DataFrame(rows, columns=['language', 'word'])
words['word'] = words['word'].str.lower()
# Delete all strings without text
words = words[words['word'].str.len() > 4]
counts = words.groupby('language').word.value_counts().to_frame()
counts.columns = ['number_words']
counts = counts.reset_index()
top_words_en = counts.loc[counts['language'] == 'en'].sort_values(by='number_words', ascending=False)
top_words_en[0:100].plot(kind='barh', x='word', y='number_words')
plt.show()
top_words_es = counts.loc[counts['language'] == 'es'].sort_values(by='number_words', ascending=False)
top_words_es[0:100].plot(kind='barh', x='word', y='number_words')
plt.show()
top_words_ca = counts.loc[counts['language'] == 'ca'].sort_values(by='number_words', ascending=False)
top_words_ca[0:100].plot(kind='barh', x='word', y='number_words')
plt.show()

print('Some examples shown')
