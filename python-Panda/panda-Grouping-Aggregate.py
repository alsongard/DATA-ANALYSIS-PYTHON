import pandas as pd
from  IPython.display import display

"""
    the grouping() method is useful for grouping a bunch of data together

"""
#read file
covid_df = pd.read_csv("./data-Files/covid-data.csv")
# print(covid_df) works
#convert date column to datetime
print(f"the dtype of covid_df.date is {covid_df.date.dtype}")#returns object
covid_df['date'] = pd.to_datetime(covid_df.date)
print(f"the dtype of covid_df.date is {covid_df.date.dtype}")#returns datetime64[ns]
#extract month,day,weekday for all cases using DatetimeIndex
covid_df['year'] = pd.DatetimeIndex(covid_df.date).year
covid_df['month'] = pd.DatetimeIndex(covid_df.date).month
covid_df['day'] = pd.DatetimeIndex(covid_df.date).day
covid_df['weekday'] = pd.DatetimeIndex(covid_df.date).weekday
#group data by month for new_cases,new_tests & new_deaths
covid_month_data_df =  covid_df.groupby('month')[['new_tests', 'new_cases', 'new_deaths']].sum()
print(covid_month_data_df)

#using cumsum() to find the cumulative sum of cases,tests and deaths up to each row
covid_df['total_test'] = covid_df.new_tests.cumsum()
covid_df['total_cases'] = covid_df.new_cases.cumsum()
covid_df['total_deaths'] = covid_df.new_deaths.cumsum()
# print(covid_df)
with pd.option_context("display.max_rows", 250):
    display(covid_df)