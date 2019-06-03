
# license: Creative Commons License
# Title: Big data strategies seminar. Challenge 1. www.iaac.net
# Created by: Diego Pajarito
#
# is licensed under a license Creative Commons Attribution 4.0 International License.
# http://creativecommons.org/licenses/by/4.0/
# This script uses pandas for data management for more information visit; pandas.pydata.org/
# This script uses data from google trends https://trends.google.com/trends/explore?date=all&q=big%20data,data%20science

import pandas as pd
from pandas import plotting
import matplotlib.pyplot as plt
import seaborn as sns
plotting.register_matplotlib_converters()


######################################################
# Read the files
trends = pd.read_csv('data/big_data_trends.csv', skiprows=2)

######################################################
# Build a nice bar chart

trends.plot(kind='line', x='Month', title='Web interest index by Google')
plt.show()


print('Some examples shown')



