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
import geopandas
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression   # Library scikit-learn
plotting.register_matplotlib_converters()


######################################################
# Read the different files starting with the last file
neighbourhoods = geopandas.read_file('../data/opendatabcn/neighbourhoods_barcelona_wgs84.geojson')
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



# Option A concat adding rows
index_concat = [irf_2007, irf_2008, irf_2009, irf_2010, irf_2011, irf_2012, irf_2013,
                irf_2014, irf_2015, irf_2016, irf_2017]
index_concat = pd.concat(index_concat)
index_concat.columns = ['year', 'district', 'name_district', 'neighbourhood', 'name_neighbourhood',
                        'population', 'index']
index_concat['index'] = index_concat['index'].apply(pd.to_numeric, errors='coerce')

# Fitting a model for  "Poble nou" id = 68
neighbourhood = index_concat.loc[index_concat['neighbourhood'] == 68, ['year', 'index']]
x = neighbourhood.loc[:, ['year']].values
y = neighbourhood.loc[:, ['index']].values

lm = LinearRegression()
lm.fit(x, y)

sns.lmplot(x='year', y='index', data=neighbourhood)
plt.show()

if lm.coef_[0, 0] > 0:
    print('positive trend')
else:
    print('negative trend')

print('Option regression done concat')


# Automatic generation of plot regression
neighbourhoods['trend'] = ''
neighbourhoods['index_2018'] = 0
neighbourhoods['BARRI'] = pd.to_numeric(neighbourhoods['BARRI'])
n_codes = neighbourhoods['BARRI'].unique()
for n in n_codes:
    label = 'reg_%i' % n
    neighbourhood = index_concat.loc[index_concat['neighbourhood'] == n, ['year', 'index']]
    x = neighbourhood.loc[:, ['year']].values
    y = neighbourhood.loc[:, ['index']].values
    lm = LinearRegression()
    lm.fit(x, y)

    # sns.lmplot(x='year', y='index', data=neighbourhood)
    # plt.savefig('../data/temp/%s.png' % label)
    if lm.coef_[0, 0] > 0:
        trend = 'positive trend'
    else:
        trend = 'negative trend'
    neighbourhoods.loc[neighbourhoods['BARRI'] == n, 'trend'] = trend
    neighbourhoods.loc[neighbourhoods['BARRI'] == n, 'index_2018'] = lm.predict([[2018]])

neighbourhoods.plot(column='trend', legend=True)
plt.show()

neighbourhoods.plot(column='index_2018', legend=True)
plt.show()

print('Map updated after linear model')