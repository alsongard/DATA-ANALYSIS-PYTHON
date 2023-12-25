import urllib.request
import pandas as pd

"""
    download file
    use pandas to read file, view contents, get statistical data, get shape
"""
italy_covid_url = 'https://gist.githubusercontent.com/aakashns/f6a004fa20c84fec53262f9a8bfee775/raw/f309558b1cf5103424cef58e2ecb8704dcd4d74c/italy-covid-daywise.csv'

#urllib.request.urlretrieve(italy_covid_url, "data-Files/covid-data.csv")

#read
covid_df = pd.read_csv("./data-Files/covid-data.csv")
print(type(covid_df))
print(covid_df)

print("\n")

#get info
print(covid_df.info())

print("\n")

#statistical data
print("Statistical Data collected is : \n")
print(covid_df.describe())

#shape
print("\n")
print(covid_df.shape)