# Viewing the data : one of the most used method for a quick overview of the dataframe is head() method. this method returns the header's and a specified number of rows.

# here we will print the first 10 rows in the dataframe.

import pandas as pd
a = pd.read_csv('data.csv')
print(a.head(10)) #this will give the first 10 lines of that data file
print(" ")
print(a.head())#this is default

# here we will print the last 10 rows in the dataframe

a = pd.read_csv('data.csv')
print(a.tail(10)) #this will give the last 10 lines of that data file
print(" ")
print(a.tail())#this is default


#what if you want the information about the data in the dataframe : via info()

a = pd.read_csv('data.csv')
print(a.info()) #it will give the basic info of the file 
#below is ouput of the info()
"""<class 'pandas.core.frame.DataFrame'>
RangeIndex: 41715 entries, 0 to 41714
Data columns (total 10 columns):
#   Column                       Non-Null Count  Dtype 
---  ------                       --------------  ----- 
 0   Year                         41715 non-null  int64 
 1   Industry_aggregation_NZSIOC  41715 non-null  object
 2   Industry_code_NZSIOC         41715 non-null  object
 3   Industry_name_NZSIOC         41715 non-null  object
 4   Units                        41715 non-null  object
 5   Variable_code                41715 non-null  object
 6   Variable_name                41715 non-null  object
 7   Variable_category            41715 non-null  object
 8   Value                        41715 non-null  object
 9   Industry_code_ANZSIC06       41715 non-null  object
dtypes: int64(1), object(9)
memory usage: 3.2+ MB
None"""