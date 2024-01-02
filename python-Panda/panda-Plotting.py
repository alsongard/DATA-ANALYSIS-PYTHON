import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display

location_df = pd.read_csv("./data-Files/location.csv")
covid_df = pd.read_csv("./data-Files/covid-data.csv")
covid_df['date'] = pd.to_datetime(covid_df.date)

covid_df['year'] = pd.DatetimeIndex(covid_df.date).year
covid_df['month'] = pd.DatetimeIndex(covid_df.date).month
covid_df['day'] = pd.DatetimeIndex(covid_df.date).day
covid_df['weekday'] = pd.DatetimeIndex(covid_df.date).weekday

covid_df['total_test'] = covid_df.new_tests.cumsum()
covid_df['total_cases'] = covid_df.new_cases.cumsum()
covid_df['total_deaths'] = covid_df.new_deaths.cumsum()

covid_df['location'] = "Italy"

covid_merged_df = covid_df.merge(location_df, on="location")

initial_tests = 935310
total_tests = covid_df.new_tests.sum() + initial_tests
total_deaths = covid_df.new_deaths.sum()
total_cases = covid_df.new_cases.sum()

covid_merged_df['tests_per_million'] = covid_merged_df.total_test * 1e6 / covid_merged_df.population
covid_merged_df['cases_per_million'] = covid_merged_df.total_cases * 1e6 / covid_merged_df.population
covid_merged_df['deaths_per_million'] = covid_merged_df.total_deaths * 1e6 / covid_merged_df.population

result_df = covid_merged_df[['date','new_cases', 'total_cases', 'new_deaths', 'total_deaths', 'new_tests', 'total_test', 'cases_per_million', 'deaths_per_million', 'tests_per_million']]
print(result_df)
print(f"the largest number of cases reported in a day is {result_df.new_cases.max()}") #returns 6557.0


#try to plot the data
# result_df.new_cases.plot()
# plt.show()

#set date as index insteat of number of rows
result_df.set_index("date", inplace=True)
# print(result_df)
# result_df.new_cases.plot()
# plt.show()

print(result_df.loc["2020-09-01"])

#compare 2 graphs for cases and deaths to understand the data
result_df.new_cases.plot()
result_df.new_deaths.plot()
plt.show()

print(f"the month with the highest number of cases is {result_df.new_cases.max()}")
print(f"the month with the highest number of death is {result_df.new_deaths.max()}")

#try to acquire the month from the data above
highest_death_number = result_df.new_deaths.max()
# result_df.new_deaths[highest_death_number]
##need to know how to retrieve data based on condition and return entire row

#draw a graph representing the death rate
death_rate = result_df.total_deaths / result_df.total_cases#return a new column
# print(death_rate)
with pd.option_context("display.max_rows", 250):
    display(death_rate)
death_rate.plot(title="death rate")
plt.show()

#als one can specify the type of graph e.g bar, line, pie chart
#groupdata
covid_month_data_df =  covid_df.groupby('month')[['new_tests', 'new_cases', 'new_deaths']].sum()

print(covid_month_data_df)
covid_month_data_df.new_tests.plot(title="New Tests", kind="bar")
plt.show()