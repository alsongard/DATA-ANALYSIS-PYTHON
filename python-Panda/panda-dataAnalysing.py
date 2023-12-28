import pandas as pd
"""
analyse the data to give relevant information from the covid-data.csv file
Q1: What are the total number of reported cases and deaths related to Covid-19 in Italy
Q2: What is the overall death rate (ratio of reported deaths to reported cases)
Q3: What is the overall number of tests conducted? A total of 935310 tests were conducted before daily test numbers were reported.**
Q4: What fraction of tests returned a positive result

"""
#read file
covid_df = pd.read_csv("./data-Files/covid-data.csv")
print(covid_df)

#Q1
total_cases = covid_df.new_cases.sum()
print(f"the total number of cases is {total_cases}\n")
total_deaths = covid_df.new_deaths.sum()
print(f"the total number of deaths is {total_deaths}\n")

#Q2
death_ratio = total_deaths/total_cases
print(f"the death ratio is {death_ratio}\n")

#Q3
initial_tests = 935310
total_tests = initial_tests + covid_df.new_tests.sum()
print("the total number of test is {}".format(total_tests))

#Q4
positive_rate = total_cases / total_tests
print(f"the positive rate is {positive_rate}")
