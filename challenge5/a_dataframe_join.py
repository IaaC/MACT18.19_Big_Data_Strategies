# license: Creative Commons License
# Title: Big data strategies seminar. Challenge 1. www.iaac.net
# Created by: Diego Pajarito
#
# is licensed under a license Creative Commons Attribution 4.0 International License.
# http://creativecommons.org/licenses/by/4.0/
# This script uses pandas for data management for more information visit; pandas.pydata.org/
# The tasks for joins and merges are here https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html
# The options for scatterplotw with seaborn https://seaborn.pydata.org/generated/seaborn.scatterplot.html
#

import pandas as pd
from pandas import plotting
import matplotlib.pyplot as plt
import seaborn as sns
plotting.register_matplotlib_converters()


######################################################
# Read the different files starting with the last file
irf_2007 = pd.read_csv('../data/opendatabcn/2007_distribucio_territorial_renda_familiar.csv')
irf_2008 = pd.read_csv('../data/opendatabcn/2008_distribucio_territorial_renda_familiar.csv')
irf_2009 = pd.read_csv('../data/opendatabcn/2009_distribucio_territorial_renda_familiar.csv')
irf_2010 = pd.read_csv('../data/opendatabcn/2010_distribucio_territorial_renda_familiar.csv')
irf_2011 = pd.read_csv('../data/opendatabcn/2011_distribucio_territorial_renda_familiar.csv')
irf_2012 = pd.read_csv('../data/opendatabcn/2012_distribucio_territorial_renda_familiar.csv')
irf_2013 = pd.read_csv('../data/opendatabcn/2013_distribucio_territorial_renda_familiar.csv')
irf_2014 = pd.read_csv('../data/opendatabcn/2014_distribucio_territorial_renda_familiar.csv')
irf_2015 = pd.read_csv('../data/opendatabcn/2015_distribucio_territorial_renda_familiar.csv')
irf_2016 = pd.read_csv('../data/opendatabcn/2016_distribucio_territorial_renda_familiar.csv')
irf_2017 = pd.read_csv('../data/opendatabcn/2017_distribucio_territorial_renda_familiar.csv')


# An example of merging, it shows you can use as much columns as you want
irf_2007.columns = ['year', 'district', 'name_district', 'neighbourhood', 'name_neighbourhood', 'pop_2007', 'idx_2007']
irf_2008.columns = ['year', 'district', 'name_district', 'neighbourhood', 'name_neighbourhood', 'pop_2008', 'idx_2008']
index_merge = pd.merge(irf_2007, irf_2008, on=['district', 'name_district', 'neighbourhood', 'name_neighbourhood'])


# Option B merge by columns / index
# We need to take care of column names to not getting confused
irf_2007.columns = ['year', 'district', 'name_district', 'neighbourhood', 'name_neighbourhood', 'pop_2007', 'idx_2007']
irf_2007 = irf_2007.loc[:, ['district', 'name_district', 'neighbourhood', 'name_neighbourhood', 'pop_2007', 'idx_2007']]

irf_2008.columns = ['year', 'district', 'name_district', 'neighbourhood', 'name_neighbourhood', 'pop_2008', 'idx_2008']
irf_2008 = irf_2008.loc[:, ['neighbourhood', 'pop_2008', 'idx_2008']]
index_merge = pd.merge(irf_2007, irf_2008, on=['neighbourhood'])

irf_2009.columns = ['year', 'district', 'name_district', 'neighbourhood', 'name_neighbourhood', 'pop_2009', 'idx_2009']
irf_2009 = irf_2009.loc[:, ['neighbourhood', 'pop_2009', 'idx_2009']]
index_merge = pd.merge(index_merge, irf_2009, on=['neighbourhood'])

# ...

irf_2017.columns = ['year', 'district', 'name_district', 'neighbourhood', 'name_neighbourhood', 'pop_2017', 'idx_2017']
irf_2017 = irf_2017.loc[:, ['neighbourhood', 'pop_2017', 'idx_2017']]
index_merge = pd.merge(index_merge, irf_2017, on=['neighbourhood'])

# A line x=y
x = range(1, 80)
plt.plot(x)

# A simple plot depends strongly on column names
sns.scatterplot(x='idx_2007', y='idx_2017',  hue='name_district', data=index_merge, s=50)
plt.show()


# Now using population
# A line x=y
x = range(1, 60000)
plt.plot(x)
# A simple plot depends strongly on column names
sns.scatterplot(x='pop_2007', y='pop_2017',  hue='name_district', data=index_merge, s=50)
plt.show()

print('Option A using concat')
