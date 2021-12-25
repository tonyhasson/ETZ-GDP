from imports import *

def clean_full_database():
    df=pd.read_csv('../CSV files/df_Full_DataBase.csv')
    #check if there are duplicates
    print(df.drop_duplicates( keep='first', inplace=True))
    #drop all the rows with NaN values
    df.dropna(inplace=True)
    print(df)


clean_full_database()