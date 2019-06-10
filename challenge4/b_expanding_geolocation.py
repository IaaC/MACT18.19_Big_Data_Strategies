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
import geopandas
plotting.register_matplotlib_converters()


######################################################
# Read the different files starting with the last file
neighbourhoods = geopandas.read_file('../data/opendatabcn/neighbourhoods_barcelona_wgs84.geojson')
geonames_bcn = geopandas.read_file('../data/geonames/geonames_bcn.geojson')
streets = pd.read_csv('../data/opendatabcn/CARRERER.csv')
tweets = pd.read_csv('../data/twitter/tweets.csv')

# we selected two elements for searching into text tweets
gnms_id = 6452887
street_name = ''

gnms_pattern = geonames_bcn.loc[geonames_bcn['geonameid'] == gnms_id, 'alternatenames'].max()
gnms_pattern = gnms_pattern.replace(',', '|').lower()
print('Text pattern: %s' % gnms_pattern)
# gnms_pattern = 'sagrada|sagrada familia'
gnms_lat = geonames_bcn.loc[geonames_bcn['geonameid'] == gnms_id, 'latitude'].max()
gnms_lon = geonames_bcn.loc[geonames_bcn['geonameid'] == gnms_id, 'longitude'].max()


# Finding text patterns within tweet text
tweets = tweets.loc[(tweets['city'] == 'Barcelona') & (pd.isnull(tweets['lat']))]
tweets['located_geonames'] = False
tweets.loc[(tweets['text'].str.lower().str.contains(gnms_pattern)) == True, 'located_geonames'] = True
tweets.loc[tweets['located_geonames'] == True, 'lat'] = gnms_lat
tweets.loc[tweets['located_geonames'] == True, 'lon'] = gnms_lon

located_tweets = tweets.loc[tweets['located_geonames'] == True]
located_tweets.to_csv('../data/twitter/located_tweets.csv')

print('Out of %i We found location for %i tweets using the pattern' % (len(tweets), len(located_tweets)))
