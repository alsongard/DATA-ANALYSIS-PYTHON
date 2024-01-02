import urllib.request
import pandas as pd
from IPython.display import display
#MERGING DATA FROM MULTIPLE SOURCES
# urllib.request.urlretrieve("https://gist.githubusercontent.com/aakashns/8684589ef4f266116cdce023377fc9c8/raw/99ce3826b2a9d1e6d0bde7e9e559fc8b6e9ac88b/locations.csv" ,"./data-Files/location.csv")

#readDate4rm file
location_df = pd.read_csv("./data-Files/location.csv")

covid_df = pd.read_csv("./data-Files/covid-data.csv")

#convert covid_df.date frm object to data using pd.to_datetime()
covid_df['date'] = pd.to_datetime(covid_df.date)

#adding new-columns to covid_df
covid_df['year'] = pd.DatetimeIndex(covid_df.date).year
covid_df['month'] = pd.DatetimeIndex(covid_df.date).month
covid_df['day'] = pd.DatetimeIndex(covid_df.date).day
covid_df['weekday'] = pd.DatetimeIndex(covid_df.date).weekday

#using cumsum() to find the cumulative sum of cases,tests and deaths up to each row
covid_df['total_test'] = covid_df.new_tests.cumsum()
covid_df['total_cases'] = covid_df.new_cases.cumsum()
covid_df['total_deaths'] = covid_df.new_deaths.cumsum()

#add a new column
covid_df['location'] = "Italy"

#merging
covid_merged_df = covid_df.merge(location_df, on="location")



#after merging we can compute large data for millions of cases,deaths and test

#or you could use the cumsum()
#get  cases, deaths, test per million
#the values below give the mean/average value
covid_merged_df['tests_per_million'] = covid_merged_df.total_test * 1e6 / covid_merged_df.population
covid_merged_df['cases_per_million'] = covid_merged_df.total_cases * 1e6 / covid_merged_df.population
covid_merged_df['deaths_per_million'] = covid_merged_df.total_deaths * 1e6 / covid_merged_df.population
print("After adding test,cases and death per million : ")
print(covid_merged_df)
with pd.option_context("display.max_rows", 250):
    display(covid_merged_df)

#select the only required column and use the to_csv() option to write to a file
result_df = covid_merged_df[['date',
                       'new_cases', 
                       'total_cases', 
                       'new_deaths', 
                       'total_deaths', 
                       'new_tests', 
                       'total_test', 
                       'cases_per_million', 
                       'deaths_per_million', 
                       'tests_per_million']]

#result_df.to_csv("./data-Files/new-covid-date.csv",index=None)