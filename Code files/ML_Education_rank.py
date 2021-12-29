import numpy

import numpy as np
import pandas as pd
import math
from imports import *
from subprocess import Popen

def load_dataset(df, label_column):

    TRAINING_FEATURES = df.columns[df.columns != label_column]
    TARGET_FEATURE = label_column

    X = df[TRAINING_FEATURES]
    y = df[TARGET_FEATURE]

    return X,y



def linear_regres(first_year,dataset,label_column):
    dataset =dataset[['Year', label_column]]
    X,y=load_dataset(dataset[(dataset['Year']>=first_year) & (dataset['Year']<=2019)],label_column)
    m=linear_model.LinearRegression().fit(X.values,y)
    arr_data=[]

    arr_year = [[year] for year in range(1960, first_year)]
    arr_year.append([2020])
    arr_data.append(m.predict(arr_year))

    return arr_data

def check_year_lr(dataframe, country):
    for year in range(1990,2020):
        data_year_country = dataframe[(dataframe["Year"] == year) & (dataframe["Country"] == country)]["Education Ranking"].values

        if data_year_country[0]!=0:
            return year



def find_and_regres(dataset,label_column):
    NO_INFO_countries = []
    dataset[label_column].fillna(0, inplace=True)
    for country in dataset.Country.unique():
        try:
            data_year_country=dataset[(dataset["Year"]==2019) & (dataset["Country"]==country)][label_column]

            if data_year_country.values[0]!=0:

                first_year=check_year_lr(dataset,country)

                arr_data=linear_regres(first_year,dataset[dataset['Country']==country],label_column)
                arr_data=list(arr_data[0])
                for i in range(len(arr_data)):
                    if arr_data[i] < 0:
                        arr_data[i] = 0


                year_2020 = arr_data.pop() # store the last year
                for i in range(first_year, 2020):
                    arr_data.append(0)
                arr_data.append(float(year_2020))

                dataset.loc[(dataset['Country']==country) & (dataset['Year']>=1960) & (dataset['Year']<=2020),label_column]+=arr_data
            else:
                NO_INFO_countries.append(country)



        except:
            dataset.loc[(dataset['Country'] == country) & (dataset['Year'] >= 1960) & (dataset['Year'] <= 2020), label_column] = 9 #Explain pls
            NO_INFO_countries.append(country)

# Fill in countries with no information with the minimum value for that year
    for country in NO_INFO_countries:
        for year in range(1960, 2021):
            dataset.loc[(dataset['Country'] == country) & (dataset['Year'] == year), label_column] = min(i for i in dataset[(dataset['Year'] == year)][label_column] if i > 0)


    dataset.to_csv(r"../CSV files/df_Full_DataBase.csv", index=False)
    f=Popen("../CSV files/df_Full_DataBase.csv",shell=True)


df=pd.read_csv(r"../CSV files/df_Full_DataBase.csv")

#print(check_year_lr(df,"Andorra"))

find_and_regres(df,'Education Ranking')