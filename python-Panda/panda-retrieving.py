#read data 
import pandas as pd
covid_df = pd.read_csv("./data-Files/covid-data.csv")
print(covid_df)
print('\n')

#retrieving a specific column
print("column in new_deaths :\n")
print(covid_df['new_deaths'])
print(type(covid_df['new_deaths']))
print('\n')

#retrievind specific row of data in new_cases index 243
print("retrieve index 111 of new_cases : \n")
print(covid_df["new_cases"][243])
print('\n')

#using at() method
print("using at() method to retrieve data :\n")
print(covid_df.at[111, "new_cases"])
print('\n')

#another way to print column data with its key
print("another method of printing column data")
print("new_cases in covid_df var : \n")
print(covid_df.new_cases)
print("\n")

#retrieval of several data columns
print("retrieval of several data columns")
print(covid_df[["new_cases", "new_deaths"]])
print('\n')

#copy data
covid_df_copy = covid_df.copy()
print("Copied Data : \n ")
print(covid_df_copy)
print('\n')

#using loc[] method
print("Using loc[] method to retrieve data : \n")
print(covid_df.loc[243])
print('\n')
#using loc[] for ranges
print("range values using loc[] :\n")
print(covid_df.loc[108:113])
print('\n')

#using head() & tail()
print("Using head and tail methods")
print("for head values : \n")
print(covid_df.head(10))
print("for tail values : \n")
print(covid_df.tail(10))
print('\n')

#in the head value for covid_df.head(10) new_tests are NaN since no data in covid-data.csv
#to check for first data use first_valid_index()
print("check for valid data in new_tests :\n")
print(covid_df.new_tests.first_valid_index())
print('\n')

#range of values
print(covid_df.loc[108:113])
print('\n')

#sample()
print("using sample() methd :\n")
print(covid_df.sample(10))