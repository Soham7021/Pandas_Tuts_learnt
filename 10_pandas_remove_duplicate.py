# removing the duplucate values : first you need to discover the duplicate values via duplicated() method. 

import pandas as pd
a = pd.read_excel('dirty data.xlsx')
print(a.duplicated().to_string())# this will mark true in the places of the duplicated one's. 


# removing the dupliate from the data set. vai the drop_duplicates()

a = pd.read_excel('dirty data.xlsx')
a.drop_duplicates(inplace=True)