import pandas as pd
from IPython.display import display

"""
    querry data and perform some basic data analysing from the covid-data.csv doc
    initial_tests = 935310
"""
#read file
covid_df = pd.read_csv("./data-Files/covid-data.csv")
print(covid_df)
#Check days we had more than 1000 cases reported
high_new_cases =  covid_df.new_cases > 1000
print(high_new_cases)#return boolen values for the cases which are higher as True and False for lower vals
print(covid_df[high_new_cases])#return only the data rows which have a true value in the high cases above
#similar code to the above
high_cases_df = covid_df[covid_df.new_cases > 1000]
print(high_cases_df)#returns only data rows whose case is above 1000 or have the boolen True
#also it can be seen that 72 rows are present

with pd.option_context('display.max_rows', 100):
    display(covid_df[covid_df.new_cases > 1000])
print("\n")

initial_tests = 935310
total_tests = covid_df.new_tests.sum() + initial_tests
print(f"the number of total tests performed is : {total_tests}")
positive_rate = covid_df.new_cases.sum() / total_tests
print("the positive rate which is the ratio of new cases to total tests is {}\n".format(positive_rate))
print("\n")
print("the cases which have a higher positive rate that the average positive rate in Boolen Values :")
positive_case_rates = covid_df.new_cases / covid_df.new_tests > positive_rate
print(positive_case_rates)
print("\n")
with pd.option_context("display.max_rows", 250):
    display(positive_case_rates)
    display(covid_df[positive_case_rates])
print(covid_df.loc[111:128])
print("\n\n\n")
print("the result of performing an operation between 2 columns :")
positive_rate_data = covid_df.new_cases / covid_df.new_tests
print(positive_rate_data)
covid_df["positive_rates"]= covid_df.new_cases / covid_df.new_tests
with pd.option_context("display.max_rows", 250):
    display(covid_df)

print("\n")
print("Getting data using sort_valeus() method : ")
print("10 days in which the number of cases were high ")
# high_cases_df = covid_df.sort_values("new_cases", ascending=True).head(10) this returns the days in which cases were low
high_cases_df = covid_df.sort_values("new_cases", ascending=False).head(10) 
print("the following data represents the days in which covid cases were high")
print(high_cases_df) #it can be seen the month of march has the highest cases