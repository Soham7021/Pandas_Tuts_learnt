# read csv files : (comma seperated file) it is a simple way to store the big and biggest data sets. thus csv file are used widely and csv file contains the plain text.



# loading the csv file into a dataframe
import pandas as pd
df = pd.read_csv('data.csv')
print(df.to_string())# to string means printing all the data set's from the csv if we only do the print(df) then it will show the limited data only or it may show the few first data only thus if want to see the whole data from the file use the to_string() function

#let's see the example of loading without the to_string() 
df = pd.read_csv('data.csv')
print(df)
#this will be the output of this code wihtout to_string()
"""0      2021  ...  ANZSIC06 divisions A-S (excluding classes K633...
1      2021  ...  ANZSIC06 divisions A-S (excluding classes K633...
2      2021  ...  ANZSIC06 divisions A-S (excluding classes K633...
3      2021  ...  ANZSIC06 divisions A-S (excluding classes K633...
4      2021  ...  ANZSIC06 divisions A-S (excluding classes K633...
...     ...  ...                                                ...
41710  2013  ...  ANZSIC06 groups C111, C112, C113, C114, C115, ...
41711  2013  ...  ANZSIC06 groups C111, C112, C113, C114, C115, ...
41712  2013  ...  ANZSIC06 groups C111, C112, C113, C114, C115, ...
41713  2013  ...  ANZSIC06 groups C111, C112, C113, C114, C115, ...
41714  2013  ...  ANZSIC06 groups C111, C112, C113, C114, C115, ...

[41715 rows x 10 columns]"""


# max_rows : you can check your system's maximum rows with : 

print(pd.options.display.max_rows) #the output is 60

print(" ")

# yes, we can increase the max no of rows of the system to display the entire dataframe without using to_string()

"""pd.options.display.max_rows = 9999
df = pd.read_csv('data.csv')
print(df)""" #this is not the current techniqu to read the data thus alway's use to_string() to read the complete data
