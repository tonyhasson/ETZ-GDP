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
    dataset =dataset[['Year', label_column]]
    X,y=load_dataset(dataset[(dataset['Year']>=first_year) & (dataset['Year']<=2019)],label_column)
    m=linear_model.LinearRegression().fit(X,y)
    arr_data=[]

    arr_year = [[year] for year in range(1960, first_year)]

    arr_data.append(m.predict(arr_year))

    return arr_data

def check_year_lr(dataframe, country):
    for year in range(1990,2020):
        data_year_country = dataframe[(dataframe["Year"] == year) & (dataframe["Country"] == country)]["Education Ranking"].values

        if not pd.isna(data_year_country[0]):
            return year



def find_and_regres(dataset,label_column):

    for country in dataset.Country.unique():
        try:
            data_year_country=dataset[(dataset["Year"]==2019) & (dataset["Country"]==country)]["Education Ranking"]

            if len(data_year_country.values) > 0  and not pd.isna(data_year_country.values[0]):

                first_year=check_year_lr(dataset,country)

                arr_data=linear_regres(first_year,dataset[dataset['Country']==country],label_column)
                country_name=[country for c in range(1960,first_year)]
                year_name=[c for c in range(1960,first_year)]

                df = pd.DataFrame({"Country": country_name, "Year": year_name, "Education Ranking": arr_data[0]})

                dataset = df.merge(dataset, on=['Year'], how='outer')
        except:
            continue
    dataset.to_csv(r"../CSV files/df_Full_DataBase.csv")

df=pd.read_csv(r"../CSV files/df_Full_DataBase.csv")

#print(check_year_lr(df,"Andorra"))

find_and_regres(df,'Education Ranking')