# INTRODUCTION TO PANDAS

## Features

### urllib.request
the urllib.request is used to download files from the internet to your machine.
``import urllib.request``
syntax for using the command is: 
``urlllib.request.retreive ( web-url, file-name-location)``

### pandas module
the pandas module offers various functions and is used for dataframes object
syntax : ``import pandas as pd ``  
alias used in the prgm is pd

To read data frm fiile use 
``covid_df = pd.read_csv("file_path")``
Data is read and stored in a DataFrame structure which is a core object	in Pandas library. Most variables have a suffix variableName_df
``print(type(covid_df))`` it return DataFrame structure
print(covid_df) returns the dataframe object which consist of the data from the csv file.

### info()
Syntax : ``dataFrameVariable.info()``
``covid_df.info()``
the statement above is used to provide some basic information about the data frame such as the number of columns, row count and data types

### describe()
Syntax : ``dataFrameVariable.describe()``
``covid_df.describe()``
the describe() method is used to provide statistical information about numerical columns such as mean, standard deviation, max/min values and the number of non-empty values 

### columns()
Suntax : 
```
	dataFrameVariable.colums()
	covid_df.columns()
```
the columns method is used to return the header columns within the dataFrame variable

### shape()
Syntax : 
```
	dataFrameVariable.shape()
	covid_df.shape()
```
the shape return the number of rows and columns of the df object


# RETRIEVING DATA FROM A DATA FRAME
	dataFrames in panda store data similar to a dictionary, incase of retreiving data
	example : 
	# Pandas format is simliar to this
covid_data_dict = {
    'date':       ['2020-08-30', '2020-08-31', '2020-09-01', '2020-09-02', '2020-09-03'],
    'new_cases':  [1444, 1365, 996, 975, 1326],
    'new_deaths': [1, 4, 6, 8, 6],
    'new_tests': [53541, 42583, 54395, None, None]
    'keys': ['values'//list of items of sametype]
} 
	this is the same as the dataFrameVariableObject covid_df = pd.read_csv("./file-Data/covid-data.csv")
print(covid_df)
           date  new_cases  new_deaths  new_tests //these are the keys
0    2019-12-31        0.0         0.0        NaN //these are values
1    2020-01-01        0.0         0.0        NaN //these are values
2    2020-01-02        0.0         0.0        NaN //these are values
3    2020-01-03        0.0         0.0        NaN
4    2020-01-04        0.0         0.0        NaN
..          ...        ...         ...        ...
243  2020-08-30     1444.0         1.0    53541.0
244  2020-08-31     1365.0         4.0    42583.0
245  2020-09-01      996.0         6.0    54395.0
246  2020-09-02      975.0         8.0        NaN
247  2020-09-03     1326.0         6.0        NaN


	Example of retrieving data from column  new_deaths by using the indexing notation
``print(covid_df["new_deaths"])``
	the data returned above will be of the key new_deaths and values which are lists containing the same data type

```
print(type(covid_df["new_deaths"]))
<class 'pandas.core.series.Series'>
```
	return a Series 
	each column in a dataFrame object /dataFrame is called a Series which is essentially a nump array with the same mthds and properties
	np.array(arrayName or [list_of_values])

#accessing a value based on its index
``print(covid_df['new_deaths'][110])``

### at() method
pandas provide a similar method to the above by using the at[]method takes 2 arguments
```
	print(covid_df.at[row_number, column_data])
	print(covid_df.at[243, new_deaths or any column data])
```
### column_name
another way to access a dataFrame column is using the name of that colum in our case
```
	print(covid_df.new_deaths)
	print(covid_df.new_cases)
	print(covid_df.new_test)
```
however this only works for column names which have no spaces or special characters

### retrieving several columns of data by
```
	case_df = covid_df[['date' , 'new_cases' ]]
	print(case_df)
	print(case_df.shape / type(case_df) / case_df.description() / case_df.info() )
```
the case_df dataFrame variable uses the same memory as that of the covid_df dataFrame variable, hence changing either values affect the other dataframeVariable, however these enable efficient memory use .

### copy()
the copy() methd is used to copy data from 1 dataframe object to another and changing either value doesn't affect each other
```
	covid_df_copy = covid_df.copy()
	print(covid_df_copy)
```
### loc[]
the .loc[] method is used to return  the entire row data based on the given index
Example
```
	print(dataFrame.loc[index_number])
	print(covid_df.loc[243])
```
Using loc[] method to retrieve data : 
date          2020-08-30
new_cases         1444.0
new_deaths           1.0
new_tests        53541.0
Name: 243, dtype: object
	it return all the data of that row including the keys/header and with their values
print(type(covid_df.loc[234]))
### head() #tail()
	the head method is used to return a the first 5 lines of the dataFrame object or the given number of lines
print(covid_df.head() or covid_df.head(5))
	the tail method is the vice versa of the head() method
print(covid_df.tail() or covid_df.tail())
### first_valid_index()
	the method above returns the row number/index that has a valid index number and not Nan
	Nan results when the row of the comma seperated value file has no value it's empty  and not zero
print(covid_df.new_test.first_valid_index())
111 //it has returned the index 111
### loc[]
	one can also use the .loc[] to print the range of the values
print(covid_df.loc[108:133])
	returns a range of values
### sample()
	this methd return random numbers of the dataFrame Object and it takes in an argument which is the number of rows to return
print(covid_df.sample(10))

			#ANALYZING DATA FROM DATA FRAMES
total number of reported cases and deaths related in italy from the covid_df object
### read data from file
covid_df = pd.read_csv("./myDAta/covid-results.csv")

#cases select row cases
total_cases = covid_df.new_cases.sum()
total_deaths = covid_df.new_deaths.sum()

#overall death rate(ration of deaths to cases)
death_rate = (covid_df.new_deaths.sum() / covid_df.new_cases.sum())

#overall number of test conducted given prior covid test is 935410 test
initial_tests = 935410
total_covid_tests = initial_tests + covid_df.new_tests.sum()

#number of tests that were positive and negative

#total for the whole tests
negative = covid_df.tests.sum() - covid_df.new_cases.sum()
positive = covid_df.new_cases.sum()
#fraction of cases returned a positive result
positive_rate = covid_df.new_cases.sum() / covid_df.tests.sum()
	

			#QUERY AND SORTING DATA
#READ FILE
import pandas as pd
covid_df = pd.read_csv("file-path")
#get values that are above 1000 for new_cases
high_new_cases = covid_df.new_cases > 1000
print(high_new_cases)
#it return true and false values depending on the new_cases value for each row, however with a few rows 
print(covid_df[high_new_cases])
#to display more use
from IPython.display import display or import display
with pd.option_context("display.max_rows", 100):
	display(covid_df.new_cases[high_new_cases])
	display(covid_df[covid_df.new_cases > 1000])
#complex queries ratio of cases to test is  higher than the positive rate
positive_rate = covid_df.new_cases.sum() / covid_df.total_tests
print(positive_rate) #return boolean values
print(covid_df[positive_rate])#return only values that  have true
with pd.option_context("display.max_rows", 100):
	display(covid_df[positive_rate])
	
#the result of performing an operation between 2 columns is a new column
positive_rate_data = covid_df.new_cases / covid_df.new_tests
#to add column to data
covid_df["positive_rates"] = covid_df.new_cases / covid_df.new_tests
with pd.option_context("display.max_rows", 250):
	display(covid_df)
#to remove the new_column use the drop mthd
#covid_df.drop(column=['positive_rate], inplace=True)

also one can sort data in rows using the .sort_values() method which takes in the "column", order(which can be ascending or descending)
E.g 
	covid_df.sort_values("new_cases", ascending=False).head(10)
	month of march has the highest cases the largest being 6557.0
	
	
			#WORKING WITH DATES
the pandas library offers many methods to work with dates
#read file
import pandas as pd
covid_df = pd.read_csv("file-location")
print(covid_df)
#read the date column 
print(covid_df.date)
print(type(covid_df.date))
#convert the object or covid_df.date to datetime
#to convert the  date data column to date data type use the pd.to_datetime[dataFrameObject.column]
#remember we use pd.to_datetime(dateFrameObject.column4date)
covid_df['date'] = pd.to_datetime(covid_df.date)
print(covid_df.date)
print(type(covid_df.date))
#extract different parts the date using DateTimeIndex()
dataFrameObject['new_column'] = pd.DateTimeIndex(dataFrameObject.column4Date).year/day/month/weekday
covid_df['year'] = pd.DateTimeIndex(covid_df.date).year
covid_df['week'] = pd.DateTimeIndex(covid_df.date).weekday
covid_df['month'] = pd.DateTimeIndex(covid_df.date).month
covid_df['day'] = pd.DateTimeIndex(covid_df.date).day
print(covid_df)
print(dtype(covid_df.date.dtype))#returns datetime64[ns]
#performing overall metrics for a month
#procedures are : select the month, choose a the subset of columns adn use the sum method
#query rows for May
covid_df_May = covid_df[covid_df.month == 5]
#query for year
covid_df_year = covid_df[covid_df.year == 2023]
#selecting the subset of columns
covid_df_may_metrics = covid_df_may[['new_cases', 'new_deaths', 'new_tests']]
covid_may_totals = covid_df_may_metrics.sum()
print(covid_may_totals)
print(f"the type of {type(covid_may_totals)} and the dtype is {covid_may_totals.dtype}")
all the above operations can be combined to one single statement using 
covid_df[covid_df.month == 5][['new_cases', 'new_deaths', 'new_tests']].sum()
#check if number of cases is Sunday is higher than the mean
cases_average = covid_df.new_cases.mean()
print(cases_average)
sunday_cases = covid_df[covid_df.day == 6].new_cases.mean()
or
sunday_cases = covid_df[covid_df.day == 6]
average_cases_sunday = sunday_cases.new_cases.mean()
print(average_cases_sunday)

			#GROUPING & AGGREGATION
			
#groupby() method
#get sum for each month and then group the data by month
covid_month_data_df = covid_df.groupby('month')[['new_cases','new_deaths','new_tests']].sum()
covid_year_data_df = covid_df.groupby('year')[['new_cases', 'new_deaths', 'new_tests']].sum()#when data is huge
print(covid_month_data_df)

the month represents which element in the covid_df (dataFrame Object) will be used for grouping data
#get mean of  daily new cases, deaths and tests for each month and then group data by month
covid_mean_data_df = covid_df.groupby('month')[['new_cases', 'new_deaths', 'new_tests']].mean()

#cumsum()
acquire the cumulative sum of cases,tests and deaths up to each row's date
covid_df['total_cases'] = covid_df.new_cases.cumsum()
covid_df['total_tests'] = covid_df.new_test.cumsum()
covid_df['total_deaths'] = covid_df.new_deaths.cumsum()
#the data above is added after each row
print(covid_df)

		#MERGING DATA FRM MULTIPLE SOURCES
import pandas as pd
from IPython.display import display
import urllib.request
urllib.request.urlretrieve("url", locationFileName)
url.request.urlretrieve('https://gist.githubusercontent.com/aakashns/8684589ef4f266116cdce023377fc9c8/raw/99ce3826b2a9d1e6d0bde7e9e559fc8b6e9ac88b/locations.csv', "./data-Files/location.csv")
#convert file to dataFrameObject
location_df = pd.read_csv(locationFileName)
print(location_df)
#print data on italy only
italy_df = location_df[location_df.location == "Italy"]
print(location_df[location_df.location == "italy"])      

#merging operation
#to perform a merging operation we require to 2 or more columns however in our case we are using 2 in which one column must have a common value.
#to do this we add the location which is italy to our covid_df object
covid_df["location"] = "Italy"
print(covid_df) #return a new_raw of data
#to add columns from location_df to covid_df using .merge()
merged_df = covid_df.merge(location_df, on="location")
print(merged_df)
#the merge functions takes 2 arguments, one being dataFrameObject frm which data is to be merged and which column is common
covid_merge_df = covid_df.merge(location_df, on="location")

			#OUTPUT TO FILE
result_df = merged_df[['date',
                       'new_cases', 
                       'total_cases', 
                       'new_deaths', 
                       'total_deaths', 
                       'new_tests', 
                       'total_tests', 
                       'cases_per_million', 
                       'deaths_per_million', 
                       'tests_per_million']]
                       
                       
print(result_df)
#to write data to a file use the to_csv() function/method which takes 2 arg one the dataframeObject, second the index of the dataFrame by default
result_df.to_csv("results.csv", index=None)


						#BASIC PANDA PLOTTING
						
#pandas offers a way to plot data using .plot() method which takes a dataFrame variable,column to plot 
#also for one to use panda u must import the matplotlib
import matplotlib.pyplot as plt
result_df.new_cases.plot()
plt.show()
#however the plot doesn't show dates with relation to the new_cases in the graph, it uses the number of rows on the x-axis which is 250, to change to dates use:
result_df.set_index('date', inPlace="True")
#from this part it can be seen that the data uses the dates as the index and one can request the entire row of data based on the date
#based on one plot for comparisons
result_df.new_cases.plot()
result_df.new_deaths.plot()

#bases on 1 plot for comparisons
result_df.total_cases.plot()
result_df.total_deaths.plot()

#death rate and positive vary over time

death_rate = result_df.total_deaths / result_df.total_cases
#diviving 2 columns of data expect a new column of data
print(death_rate)
death_rate.plot(title="Death Rete")

positive_rate = result_df.total_cases / result_df.total_tests
print(positive_rate)
positive_rate.plot(title="Positive Rate")

#plotting use bar chart
#for new_cases
covid_month_data_df.new_cases.plot(kind="bar")
##using groupby to group data based on the group(element)
#also for test
covid_month_data_df.new_tests.plot(kind="bar")






