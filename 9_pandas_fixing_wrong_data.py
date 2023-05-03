# Wrong Data :  it's simply wrong

import pandas as pd
a = pd.read_excel('dirty data.xlsx')
print(a.to_string())

#here we will set "Consumer Total" = 45 in row 5

a = pd.read_excel('dirty data.xlsx')
a.loc[4,'Consumer Total'] = 45
print(a.to_string())


# for large data set : now here we will loop through all the values in "Consumer Total" column, if the value is higher than 120 then set it to 120. 

a = pd.read_excel('dirty data.xlsx')
for i in a.index : 
    if a.loc[i,'Consumer Total'] > 120:
        a.loc[i,'Consumer Total'] = 55
print(a.to_string())# here all the values in the consumer total table which are greater than the 120 will be set to the 120

#You can also remove the row in larger dataset.
a = pd.read_excel('dirty data.xlsx')
for i in a.index : 
    if a.loc[i,'Consumer Total'] > 120:
        a.dropna(i, inplace=True)
print(a.to_string())# this will directly remove the row