# data in a wrong format : to fix this problem there are two way's : removing the rows or convert all the cells in the same format. 

import pandas as pd
a = pd.read_excel('dirty data.xlsx')
print(a.to_string())

# now let's try to convert all the cells in the date column in dates. via to_datetime()
"""a = pd.read_excel('dirty data.xlsx')
a["Date"] = pd.to_datetime(a["Date"])
print(a.to_string())"""
#this will not work because we don't have column named "Date" in our file this is only form learning perpose

#now let's try to convert the consumer column from our file from the float values to the integer values if possible only try 

import pandas as pd
a = pd.read_excel('dirty data.xlsx')
a["Consumer Total"] = pd.to_datetime(a["Consumer Total"])#it will change the format of the consumer total to the date time
# in some places it will show the NaT instead of NaN i.e it means the value you are trying to change is not a time
print(a.to_string())


# here we will remove the rows with a NULL value in the "Consumer Total" column. i.e It will remove te NaT

a = pd.read_excel('dirty data.xlsx')
a["Consumer Total"] = pd.to_datetime(a["Consumer Total"])
a.dropna(subset=["Consumer Total"],inplace=True) # we can observe that all the row's with the NaT value are removed after executing this
print(a.to_string()) #didn't understood actually