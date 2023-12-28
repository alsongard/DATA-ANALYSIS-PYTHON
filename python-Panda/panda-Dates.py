import pandas as pd
from IPython.display import display
"""
    working with dates

"""
#read file data
covid_df = pd.read_csv("./data-Files/covid-data.csv")
print("the data frame object covid_df :")
print(covid_df)
print("the data type of covid_df is {}".format(type(covid_df)))
print("\n")
print("Date data in covid_df :")
print(covid_df.date)
print("the data type of covid_df.date is {}".format(type(covid_df.date)))
print("\n")
#convert the object or covid_df.date to datetime
print("convert covid_df.date to datetime")
covid_df['date'] = pd.to_datetime(covid_df.date)
print(covid_df.date.dtype)#returns datetime64[ns]
print('\n')
#extract data from the date column using DateTimeIndex()
covid_df['year'] = pd.DatetimeIndex(covid_df.date).year
covid_df['month'] = pd.DatetimeIndex(covid_df.date).month
covid_df['day'] = pd.DatetimeIndex(covid_df.date).day#day of the week in date
covid_df['weekday'] = pd.DatetimeIndex(covid_df.date).weekday#weekday is the day of the week
print(covid_df)
print('\n')
with pd.option_context("display.max_rows", 250):
    display(covid_df)

#query rows for May month
print("the data for the month of may :")
covid_df_may = covid_df[covid_df.month == 5]
print(covid_df_may)
print('\n')
#get new_deaths, new_tests, new_cases total
may_cases = covid_df_may['new_cases'].sum()
may_tests = covid_df_may['new_tests'].sum()
may_deaths = covid_df_may['new_deaths'].sum()
#print(my_cases)returns a list of may_cases
may_cases.sum()
print("the total number of cases in the month of may is {}".format(may_cases))
print("\n")

#however the above code  is tedious and more for efficiency use
may_data = covid_df_may[['new_tests', 'new_cases', 'new_deaths']]
print(may_data.sum())
print("\n")
# check if average number of cases in sunday and monday and total average sunday cases
sunday_avrg = covid_df[covid_df.weekday== 6].new_cases.mean()
#or sunday_data = covid_df[covid_df.weekday == 6]
#sundayAvrg = sunday_data.new_cases.sum()
print(sunday_avrg)
#check average/mean of new_cases in the whole covid period
new_cases_avrg = covid_df.new_cases.mean()
print(new_cases_avrg)