# cleaning data : it meanss the fixing the bad data in your data set. bad data could be : empty cell, data in wrong format, duplicate data and wrong data. 
# effecive way of cleaning data is removing that row from the data and analysing it from the remaining data
# empty cells will give you wrong result alway's thus we will have to remove the rows always that contain the bad data.
# loading and reading the original dataframe 
import pandas as pd
a = pd.read_excel('dirty data.xlsx')
print(a.to_string())
# here we will return a new dataframe with no empty cell. 

a = pd.read_excel('dirty data.xlsx')
b = a.dropna()# it will remove the empty cell's and give the remaining 
print(b.to_string())

# if at any case you want to change the original dataframe, than   use the inplace = True argument. it will remove the rows containing the NULL(NaN) values.

a = pd.read_excel('dirty data.xlsx')
a.dropna(inplace=True)#this will directly make the changes in the original file which is not a good practice thus it is not recomended
print(a.to_string())

# replacing the empty value : we will use fillna() method which will allow us to replace the empty value

a = pd.read_excel('dirty data.xlsx')
a.fillna(130,inplace=True) #this will put the value 130 in the places of the "NaN" i.e it will fill the empty space with the 130 number, where 130 is not a fixed we can change it accordingly
print(a.to_string())


# to replace only the emptyl value for one column, you need to specify the column name.

a = pd.read_excel('dirty data.xlsx')
a["Consumer"].fillna(130,inplace=True)
print(a.to_string())


# here we can also replace the empty cell using mean(), median() or mode(). 
# Calculate the Mean() and replace the empty values with it. 

a = pd.read_excel('dirty data.xlsx')
b = a["Consumer Total"].mean()
a["Consumer Total"].fillna(b,inplace=True)# it will fill the empty cell's of the consumer total by the mean of the table only empty cell's of the Consumer total
print(a.to_string())


# calculate the median and replace any empty values in it: 
a = pd.read_excel('dirty data.xlsx')
b = a["Consumer Total"].median()
a["Consumer Total"].fillna(b,inplace=True)# it will fill the empty cell's of the consumer total by the median of the table only empty cell's of the Consumer total
print(a.to_string())



# calculate the MODE and replace the empty cell with it : 
a = pd.read_excel('dirty data.xlsx')
b = a["Consumer Total"].mode()[0]
a["Consumer Total"].fillna(b,inplace=True)# it will fill the empty cell's of the consumer total by the mode(mode: mostly occured value) of the table i.e is mostly occured vlaue will be put up in the empty cell only empty cell's of the Consumer total
print(a.to_string())