
# license: Creative Commons License
# Title: Data management with pandas www.iaac.net
# Created by: Diego Pajarito
#
# is licensed under a license Creative Commons Attribution 4.0 International License.
# http://creativecommons.org/licenses/by/4.0/
# This script uses pandas for data management for more information visit; pandas.pydata.org/
# Merging and joining data frames is a very important task in data science check out the docs
# Join: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.join.html
# Merge: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.merge.html
#

import pandas as pd
import matplotlib.pyplot as plt
from pandas import plotting


plotting.register_matplotlib_converters()


######################################################
# Reading csv files from different topics
listings_012018 = pd.read_csv('../data/airbnb_listings/listings_012018.csv')
listings_022018 = pd.read_csv('../data/airbnb_listings/listings_022018.csv')
listings_042018 = pd.read_csv('../data/airbnb_listings/listings_042018.csv')
listings_052018 = pd.read_csv('../data/airbnb_listings/listings_052018.csv')
listings_062018 = pd.read_csv('../data/airbnb_listings/listings_062018.csv')
listings_072018 = pd.read_csv('../data/airbnb_listings/listings_072018.csv')
listings_082018 = pd.read_csv('../data/airbnb_listings/listings_082018.csv')
listings_092018 = pd.read_csv('../data/airbnb_listings/listings_092018.csv')
listings_102018 = pd.read_csv('../data/airbnb_listings/listings_102018.csv')
listings_112018 = pd.read_csv('../data/airbnb_listings/listings_112018.csv')
listings_122018 = pd.read_csv('../data/airbnb_listings/listings_122018.csv')
listings_012019 = pd.read_csv('../data/airbnb_listings/listings_012019.csv')
listings_022019 = pd.read_csv('../data/airbnb_listings/listings_022019.csv')
listings_032019 = pd.read_csv('../data/airbnb_listings/listings_032019.csv')
listings_042019 = pd.read_csv('../data/airbnb_listings/listings_042019.csv')

incidents_2010 = pd.read_csv('../data/incidents/2010_incidents_gestionats_gub.csv')
incidents_2011 = pd.read_csv('../data/incidents/2011_incidents_gestionats_gub.csv')
incidents_2012 = pd.read_csv('../data/incidents/2012_incidents_gestionats_gub.csv')
incidents_2013 = pd.read_csv('../data/incidents/2013_incidents_gestionats_gub.csv')
incidents_2014 = pd.read_csv('../data/incidents/2014_incidents_gestionats_gub.csv')
incidents_2015 = pd.read_csv('../data/incidents/2015_incidents_gestionats_gub.csv')
incidents_2016 = pd.read_csv('../data/incidents/2016_incidents_gestionats_gub.csv')
incidents_2017 = pd.read_csv('../data/incidents/2017_incidents_gestionats_gub.csv')
incidents_2018 = pd.read_csv('../data/incidents/2018_incidents_gestionats_gub.csv')


######################################################
# Setting up a common way to refer to time units
listings_012018['month'] = '2018-01'
listings_022018['month'] = '2018-02'
listings_042018['month'] = '2018-04'
listings_052018['month'] = '2018-05'
listings_062018['month'] = '2018-06'
listings_072018['month'] = '2018-07'
listings_082018['month'] = '2018-08'
listings_092018['month'] = '2018-09'
listings_102018['month'] = '2018-10'
listings_112018['month'] = '2018-11'
listings_122018['month'] = '2018-12'
listings_012019['month'] = '2019-01'
listings_022019['month'] = '2019-02'
listings_032019['month'] = '2019-03'
listings_042019['month'] = '2019-04'

incidents_2010['month'] = incidents_2010['year'].astype(str) + '-' + incidents_2010['month_num'].astype(str)
incidents_2011['month'] = incidents_2011['year'].astype(str) + '-' + incidents_2011['month_num'].astype(str)
incidents_2012['month'] = incidents_2012['year'].astype(str) + '-' + incidents_2012['month_num'].astype(str)
incidents_2013['month'] = incidents_2013['year'].astype(str) + '-' + incidents_2013['month_num'].astype(str)
incidents_2014['month'] = incidents_2014['year'].astype(str) + '-' + incidents_2014['month_num'].astype(str)
incidents_2015['month'] = incidents_2015['year'].astype(str) + '-' + incidents_2015['month_num'].astype(str)
incidents_2016['month'] = incidents_2016['year'].astype(str) + '-' + incidents_2016['month_num'].astype(str)
incidents_2017['month'] = incidents_2017['year'].astype(str) + '-' + incidents_2017['month_num'].astype(str)
incidents_2018['month'] = incidents_2018['year'].astype(str) + '-' + incidents_2018['month_num'].astype(str)

######################################################
# Merging or concatenating variables into a single variable
listings = pd.concat([listings_012018, listings_022018, listings_042018, listings_052018, listings_062018,
                      listings_072018, listings_082018, listings_092018, listings_102018, listings_112018,
                      listings_122018, listings_012019, listings_022019, listings_032019, listings_042019])

incidents = pd.concat([incidents_2010, incidents_2011, incidents_2012, incidents_2013, incidents_2014,
                       incidents_2015, incidents_2016, incidents_2017, incidents_2018])


######################################################
# Working with incidents data

# Calculate the total number of incidents per month
inc_month = incidents.groupby(['month', ])
incidents_total = inc_month['total_incidents'].sum()
incidents_total = incidents_total.to_frame()
incidents_total.columns = ['total_incidents']
incidents_total.plot()

######################################################
# Working with listing data
# Cleaning data from price
listings['price_num'] = pd.to_numeric(listings['price'].str.replace('$', '').str.replace(',', ''))


# Calculate the average price per neighbourhood
nbh_group = listings.groupby(['month', 'neighbourhood'])
price_mean = nbh_group['price_num'].mean()
price_mean = price_mean.to_frame()
price_mean.columns = ['price_mean']
price_mean.plot()



######################################################
# Saving the new merged datasets
price_mean.to_csv('../data/price_mean.csv')
incidents_total.to_csv('../data/incidents_total.csv')