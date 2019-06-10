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
from shapely.geometry import Point
import matplotlib.pyplot as plt
import seaborn as sns
plotting.register_matplotlib_converters()


######################################################
# Read the different files starting with the last file
neighbourhoods = geopandas.read_file('../data/opendatabcn/neighbourhoods_barcelona_wgs84.geojson')
irf_2017 = pd.read_csv('../data/opendatabcn/2017_distribucio_territorial_renda_familiar.csv')


# Only using year
irf_2017.columns = ['year', 'district', 'name_district', 'neighbourhood', 'name_neighbourhood', 'pop_2017', 'idx_2017']
irf_2017 = irf_2017.loc[:, ['year', 'neighbourhood', 'pop_2017', 'idx_2017']]

neighbourhoods['neighbourhood'] = pd.to_numeric(neighbourhoods['BARRI'])

neighbourhoods = pd.merge(neighbourhoods, irf_2017, on=['neighbourhood'])

# Mapping family income
neighbourhoods.plot(column='idx_2017', legend=True)
plt.savefig('../data/temp/bcn_fIncomeIndex.pdf')
plt.show()


# Mapping population density
neighbourhoods['population_density'] = neighbourhoods['pop_2017'] / (neighbourhoods['AREA'] / 1000000)
neighbourhoods.plot(column='population_density', legend=True)
plt.savefig('../data/temp/bcn_popDensity.pdf')
plt.show()


sns.scatterplot(x='idx_2017', y='population_density', data=neighbourhoods)
plt.axvline(x=100)
plt.savefig('../data/temp/income_density.pdf')
plt.show()


print('Joining geodataframes')
