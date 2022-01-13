from imports import *
from Merge import Run as Run_Merge
from ML_Algo import Run as Run_ML

FULL_DB_PATH = r"../CSV files/df_Full_DataBase.csv"


def clean_DF(df):
    arr_not = df[(df["Year"] == 2019) & (df["Population Total"] >= 0.1)][
        "Country"
    ].unique()
    df = df[df["Country"].isin(arr_not)]

    df.to_csv(FULL_DB_PATH, index=False)


if __name__ == "__main__":
    Run_Merge()
    Run_ML()
    DF_FULL_P = pd.read_csv(FULL_DB_PATH)
    clean_DF(DF_FULL_P)
    # df= pd.read_csv('../CSV files/df_Full_DataBase.csv')
