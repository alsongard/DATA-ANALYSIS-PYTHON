import urllib.request
import pandas as pd
from IPython.display import display
#MERGING DATA FROM MULTIPLE SOURCES
# urllib.request.urlretrieve("https://gist.githubusercontent.com/aakashns/8684589ef4f266116cdce023377fc9c8/raw/99ce3826b2a9d1e6d0bde7e9e559fc8b6e9ac88b/locations.csv" ,"./data-Files/location.csv")

#readDate4rm file
location_df = pd.read_csv("./data-Files/location.csv")
print(location_df)
print('\n')
# print(location_df.info)
print(f"the shape of location_df is {location_df.shape}")
print("\n")
#to add data to our covid_df object we require 1 common column btwn covid_df & location_df
print("the covid_df dataframe :")
covid_df = pd.read_csv("./data-Files/covid-data.csv")
print(covid_df)
print("\n")
#convert covid_df.date frm object to data using pd.to_datetime()
covid_df['date'] = pd.to_datetime(covid_df.date)
print(f"after changing date frm object to date {covid_df.date.dtype}")
print(covid_df)
print("\n")
#adding new-columns to covid_df
covid_df['year'] = pd.DatetimeIndex(covid_df.date).year
covid_df['month'] = pd.DatetimeIndex(covid_df.date).month
covid_df['day'] = pd.DatetimeIndex(covid_df.date).day
covid_df['weekday'] = pd.DatetimeIndex(covid_df.date).weekday
print("After adding new columns of year,month,day and weekday")
print(covid_df)
print('\n')
#using cumsum() to find the cumulative sum of cases,tests and deaths up to each row
covid_df['total_test'] = covid_df.new_tests.cumsum()
covid_df['total_cases'] = covid_df.new_cases.cumsum()
covid_df['total_deaths'] = covid_df.new_deaths.cumsum()
print("after adding total_tests , total_cases and total_deaths column using cumsum where previous e.t.c")
print(covid_df)
print('\n')
#add a new column
covid_df['location'] = "Italy"
print('\n')
print("After adding italy as a column : ")
print(covid_df)
print('\n')
#with pd.option_context("display.max_rows", 250):
#     display(covid_df)
#merging
covid_merged_df = covid_df.merge(location_df, on="location")
print("After merging using merge(dataFrameObject , common column) ")
print(covid_merged_df)
# with pd.option_context("display.max_rows", 250):
#     display(covid_merged_df)
print('\n')


#after merging we can compute large data for millions of cases,deaths and test
initial_tests = 935310
total_tests = covid_df.new_tests.sum() + initial_tests
total_deaths = covid_df.new_deaths.sum()
total_cases = covid_df.new_cases.sum()
#or you could use the cumsum()
#get  cases, deaths, test per million
#the values below give the mean/average value
covid_merged_df['tests_per_million'] = covid_merged_df.total_test * 1e6 / covid_merged_df.population
covid_merged_df['cases_per_million'] = covid_merged_df.total_cases * 1e6 / covid_merged_df.population
covid_merged_df['deaths_per_million'] = covid_merged_df.total_deaths * 1e6 / covid_merged_df.population
print("After adding test,cases and death per million :")
print(covid_merged_df)
# print(covid_merged_df)