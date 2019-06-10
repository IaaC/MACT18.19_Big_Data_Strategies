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
from sklearn.linear_model import LinearRegression
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

# Automatic generation of plot regression
neighbourhoods['neighbourhood'] = pd.to_numeric(neighbourhoods['BARRI'])
years = index_concat['year'].unique()
for y in years:
    label = 'idx_%i' % y
    index_year = index_concat.loc[index_concat['year'] == y, ['neighbourhood', 'index']]
    idx_year = pd.merge(neighbourhoods, index_year, on=['neighbourhood'])
    idx_year.plot(column='index', legend=True)
    plt.savefig('../data/temp/%s.png' % label)

print('Maps saved')
