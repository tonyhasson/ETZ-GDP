from imports import *


def clean_full_database():
    """Cleaning duplicates and Nan Values"""
    df = pd.read_csv("../CSV files/df_Full_DataBase.csv")
    print(df.drop_duplicates(keep="first", inplace=True))
    df.dropna(inplace=True)
    print(df)


clean_full_database()
