
import re
import pandas as pd
import os
from datetime import datetime

pd.set_option('display.max_columns', None)

file_path='Sales_data'
#Creating Empty Dataframe
df=pd.DataFrame()
#Walking through the folder and appending the file to the Dateframe
for root,dirs,files in os.walk('Sales_data'):
    for file in files:
#Only taking file with extention .CSV from the folder
        if file.endswith('csv'):
            path=os.path.join(root ,file)
            
            Temp_DF=pd.read_csv(path)
            df=df.append(Temp_DF)
#Looking into the Data
print(df.head(5))
print(df.tail(5))
print('df shape is',df.shape)
print(df.info())
#Rename the Columns
print(df.columns)
df.columns=df.columns=['Order_Id','Product','Quantity','Price','Order_date','Purchase_Add']
#Data Cleaning
#There are no Null values
print(df.isnull().sum())
#droping NAN from Datafram
df=df.dropna(how='any')
print(df.isnull().sum())



