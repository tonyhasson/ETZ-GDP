import numpy as np
import pandas as pd
import math
from imports import *

def load_dataset(df, label_column):

    TRAINING_FEATURES = df.columns[df.columns != label_column]
    TARGET_FEATURE = label_column

    X = df[TRAINING_FEATURES]
    y = df[TARGET_FEATURE]

    return X,y



def linear_regres(first_year,dataset,label_column):
    X,y=load_dataset(dataset,label_column)
    #m=linear_model.LinearRegression().fit(X,y)
    arr_data=[]
    for year in range(1960,first_year):
        print(m.predict(year))
        arr_data.append(m.predict(year))
    return arr_data

def check_year_lr(dataframe, country):
    country="Andorra"
    for year in (1990,2019):
        data_year_country = dataframe[(dataframe["Year"] == year) & (dataframe["Country"] == country)]["Education Ranking"].values

        if len(data_year_country) == 1 and type(data_year_country[0]) != float:
            return year



def find_and_regres(dataset,label_column):

    for country in dataset.Country.unique():
        data_year_country=dataset[(dataset["Year"]==2019) & (dataset["Country"]==country)]["Education Ranking"].values
        if len(data_year_country)==1 and type(data_year_country[0])!=float:

            first_year=check_year_lr(dataset,country)
            print(first_year)
            arr_data=linear_regres(first_year,dataset,label_column)
            country_name=[country for c in range(1960,first_year)]
            year_name=[c for c in range(1960,first_year)]
            df_data=pd.DataFrame([country_name,year_name,arr_data],columns=["Country","Year","Education Ranking"])
            dataset = df_data.merge(dataset, on=['Year'], how='outer')

df=pd.read_csv(r"../CSV files/df_Full_DataBase.csv")

#print(check_year_lr(df,"Andorra"))

find_and_regres(df,None)