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
from shapely.geometry import Point
import matplotlib.pyplot as plt
import seaborn as sns
plotting.register_matplotlib_converters()


######################################################
# Read the different files starting with the last file
neighbourhoods = geopandas.read_file('../data/opendatabcn/neighbourhoods_barcelona_wgs84.geojson')
geonames_bcn = geopandas.read_file('../data/geonames/geonames_bcn.geojson')
geonames_es = pd.read_csv('../data/geonames/ES.txt', sep='\t', header=None)
streets = pd.read_csv('../data/opendatabcn/CARRERER.csv')


######################################################
# Visualising Geospatial data
neighbourhoods.plot()
plt.show()

######################################################
# Formatting a geo-dataframe
# Since there are no column names for geonames we need to set them up
# Info from http://download.geonames.org/export/dump/readme.txt
geonames_es.columns = ['geonameid', 'name', 'asciiname', 'alternatenames', 'latitude', 'longitude', 'feature class',
                       'feature code', 'country code', 'cc2', 'admin1 code', 'admin2 code', 'admin3 code',
                       'admin4 code', 'population', 'elevation', 'dem', 'timezone', 'modification date']

# To create a geometry we need to transform coordinates stored in columns into a shapely Point
geonames_geometry = [Point(xy) for xy in zip(geonames_es.longitude, geonames_es.latitude)]
geonames_geo = geopandas.GeoDataFrame(geonames_es, geometry=geonames_geometry)

# Use the commented lines to plot all point the dataframe objects
# geonames_geo.plot(color='red')
# plt.show()

# We will use only these geonames inside Barcelona. They were obtained using QGIS
geonames_bcn.plot(marker='*', color='blue', markersize=5)
plt.show()

# We can also overlay two layers
base = neighbourhoods.plot(color='white', edgecolor='black')
geonames_bcn.plot(ax=base, marker='o', color='green', markersize=2)
plt.show()

# There are also options for visualising choropleth maps
neighbourhoods.plot(column='NOM')
plt.show()

# We can also overlay two layers
base = neighbourhoods.plot(color='white', edgecolor='grey')
geonames_bcn.plot(ax=base, marker='o', column='feature_code', markersize=2, legend=True)
plt.show()

print('This is an example of map visualisation')
