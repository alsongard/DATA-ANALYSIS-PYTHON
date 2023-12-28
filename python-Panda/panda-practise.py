import pandas as pd
from IPython.display import display

"""
    initial_tests = 935310
"""
#read file
covid_df  = pd.read_csv("./data-Files/covid-data.csv")
#check largest values above 1000
highest_cases = covid_df.new_cases > 1000
print("Boolean values for highest cases in the new_cases column:")
print(highest_cases)
print("\n")
# to list values that have highest_cases
print("to list values that have highest_cases")
with pd.option_context("display.max_rows", 100):
    display(covid_df[highest_cases])
    #display(covid_df[covid_df.new_cases > 1000])
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

#add the new column to the dataFrame
covid_df["positive_rates"]= covid_df.new_cases / covid_df.new_tests
#print all 248 lines with new column 
with pd.option_context("display.max_rows", 250):
    display(covid_df)

#to remove the new_column use the drop mthd
#covid_df.drop(column=['positive_reate], inplace=True)