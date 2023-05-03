#pandsa series is like a column in a table. it is 1d array which holds date of any type
#here we will create a simple pandas series

import pandas as pd 
a = [1,4,50]
b = pd.Series(a)
print(b)#it gives the index and the values 

#labeling - it can be used to acces the specified value 
a = [1,5,6]
b = pd.Series(a)
print(b[2])

#with create labels you can create your own labels : 
a = [1,5,6]
b = pd.Series(a, index=["x","y","z"])
print(b)
print(b["x"])#we can change the index of the array and also call it using the changed indexes


#you can allso use value obj like a dictionary , when creating the a series

#here we will create the simple pandas series from a dictionary

a = {"day1":420,"day2":23,"day3":456}
b = pd.Series(a)
print(b)

#now we will crate a series using only data from day1 and day2
a = {"day1":420,"day2":23,"day3":456}
b = pd.Series(a, index=["day1","day2"])
print(b)


#Data frame : Data sets in pandas are usualy multidimentional tables and they are called data frames .
# Sereis are like coloums and the dataframes is the whole table

#we will craete a datafrmae from 2 series 

a = {"cal":[2,5,65],"duration":[5,4,7]}
b = pd.DataFrame(a)
print(b)