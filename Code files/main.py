from imports import *
from Merge import Run as Run_Merge
from ML_Algo import Run as Run_ML


def clean_DF(df):
    arr_not = df[(df["Year"] == 2019) & (df["Population Total"] >= 0.1)][
        "Country"
    ].unique()
    df = df[df["Country"].isin(arr_not)]

    # ## WORK
    # c_list = df["Country"].unique()
    # arr_not = []
    # for c in c_list:
    #
    #     if float(df[(df["Year"] == 2019) & (df["Country"] == c)]["Population Total"]) > 0.1:
    #         arr_not.append(c)
    #
    # # drop rows that contain any value in the list
    # df = df[df["Country"].isin(arr_not)]
    # ## WORK

    df.to_csv(r"..\CSV files\\" + "df_Full_DataBase.csv", index=False)


if __name__ == "__main__":
    Run_Merge()
    Run_ML()
    DF_FULL = pd.read_csv("../CSV files/df_Full_DataBase.csv")
    clean_DF(DF_FULL)
    # df= pd.read_csv('../CSV files/df_Full_DataBase.csv')
