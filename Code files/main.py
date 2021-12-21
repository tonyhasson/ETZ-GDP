import imports

import os

from bs4 import BeautifulSoup
import pandas
import pandas as pd
import requests
#import imports
# Made By Eytan






df5 =df1.merge(df2, on=['Year','Country'], how='outer')
df6 =df3.merge(df4, on=['Year','Country'], how='outer')
df_total=df5.merge(df6, on=['Year','Country'], how='outer')
df_total.sort_values(['Country','Year'], axis=0, ascending=True, inplace=True)
df_total.drop(['Unnamed: 0_x_x','Unnamed: 0_y_x','Unnamed: 0_x_y','Unnamed: 0_y_y'],axis=1,inplace=True)

#TODO:
#1. Function For merging the dataframe by country and year
#2. Function to reformat the CSV's to be in Year,Country format