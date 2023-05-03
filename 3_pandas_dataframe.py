#Data frame : it is a 2d data structure like 2d array with table including the rows and the coloums.

import pandas as pd
a = {"cal":[45,12,45],"dur":[4,565,54]}
b = pd.DataFrame(a)
print(b)

#    cal  dur
# 0   45    4
# 1   12  565
# 2   45   54
#this is the output of this above code

#locate row: pandas use the loc attribute to return one or more specified row.

a = {"cal":[45,12,45],"dur":[4,565,54]}
b = pd.DataFrame(a)
print(b.loc[0])
# cal    45
# dur     4
#this the ouput of above code of loc 
print(" ")
#example of returning row 0 and 1 at a time it will done as below

a = {"cal":[45,12,45],"dur":[4,565,54]}
b = pd.DataFrame(a)
print(b.loc[[0,1]])
# print(b.loc[0,1]) we cant do like this to get the first two rows we will have to use two square brakets

print(" ")

# Named Index: with the index arg, you can name your own index

a = {"cal":[45,12,45],"dur":[4,565,54]}
b = pd.DataFrame(a,index=["day1","day2","day3"])
print(b)

#locate the named indexes : 
print(" ")

a = {"cal":[45,12,45],"dur":[4,565,54]}
b = pd.DataFrame(a,index=["day1","day2","day3"])
print(b.loc["day1"])
print(" ")
print(b.loc[["day1","day2"]])


# Load the data from the CSV file into dataframe i.e Data.csv 

fileload = pd.read_csv('data.csv')#we can load the files in pandas using the read attribute this will not work now because we dont have any file to load as csv in our folder we will see this in detaill in the next chapter.
print(fileload)