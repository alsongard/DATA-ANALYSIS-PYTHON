import pandas as pd
from urllib.request import urlretrieve
from IPython.display import display


"""
    Q1:How many countries does the dataframe have : use .shape method
    Q2:Retrieve a list of the continent from the dataframe : use .unique() method
    Q3:Total population of all countries in the data set
    Q4:Overall life expectancy accross the world
    Q5:Create a dataframe containing 10 countries with the hightes population
    Q6:Add a new column in countries_df to record the overall GDP per country (product of population & per capita GDP).
    Q7:Create a dataframe containing 10 countries with the lowest GDP per capita, among the counties with population greater than 100 million.
    Q8:Create a data frame that counts the number countries in each continent? : use grouby, select location column and aggregate using count
    Q9:
    Q10:
"""

#download the file
# urlretrieve('https://gist.githubusercontent.com/aakashns/28b2e504b3350afd9bdb157893f9725c/raw/994b65665757f4f8887db1c85986a897abb23d84/countries.csv', './myData/countries.csv')

countries_df = pd.read_csv("./myData/countries.csv")
print(countries_df)
with pd.option_context("display.max_rows", 250):
    display(countries_df)
print("\n")
#Q1:
# print("The number of countries are : ")
# print(countries_df.shape)
# print("Using the info on the dataframe object")
# print(countries_df.info)
# print("Another trial for shape with the loaction column selected")
country_number = countries_df.location.shape
print(f"the number of countries are {country_number}")
print("\n")


# Q2:
#the unique() method is used to return the elements from a list only oncce
continents = countries_df.continent.unique()
print(f"These are the  continents in the countries.csv file  {continents}")
#to print the number of content use the len() function
print(f"The number of continents is {len(continents)} ")
print("\n")

#Q3:
total_population = countries_df.population.sum()
print("the total population from all countries is {}".format(total_population))
print("\n")


#Q4:
overall_life_expectancy = countries_df.life_expectancy.mean()
print(f"the overall life expectancy of the world is {overall_life_expectancy}")
print("\n")

#Q5:
#try using sort method to sort the population
highest_number_population = countries_df.population.max()
print(f"the highest population is {highest_number_population }")
print("using sort")
print(countries_df.population.sort())
print("\n")