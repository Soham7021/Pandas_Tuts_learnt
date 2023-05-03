# JSON : Big data set's are normally stored and extracted as JASON . it is a plain text but it has a format of an object. 

# Loading the jason into a dataframe

import pandas as pd
df = pd.read_json('data.json')
print(df.to_string())


# Dictionary as a JSON :  if your JSON code is not in a file , but in a python dictionary , then you can do all below:


data = {
    "Duratin":{
        "0":60,
        "1":60,
        "2":60,
        "3":60,
        "4":45,
        "5":60
        },
    "Pulse":{
        "0":160,
        "1":560,
        "2":450,
        "3":110,
        "4":245,
        "5":150
        },
    "max_pulse":{
        "0":260,
        "1":510,
        "2":445,
        "3":110,
        "4":785,
        "5":450
        },
    "calories":{
        "0":260.12,
        "1":510.4,
        "2":445.45,
        "3":110.12,
        "4":785.78,
        "5":450.45
        }
    }#this is the format of the json file

dfnew = pd.DataFrame(data)
print(dfnew)

#this is the output
"""   Duratin  Pulse  max_pulse  calories
0       60    160        260    260.12
1       60    560        510    510.40
2       60    450        445    445.45
3       60    110        110    110.12
4       45    245        785    785.78
5       60    150        450    450.45"""