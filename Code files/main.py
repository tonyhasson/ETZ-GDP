from imports import *
from Merge import Run as Run_Merge
from ML_Algo import Run as Run_ML
from visualization import Run as Run_Graphs
from Clustering import PCA_Cluster_Graph as Run_Cluster


def clean_DF(df):  # TODO move function to merge?
    arr_not = df[(df["Year"] == 2019) & (df["Population Total"] >= 100000)][
        "Country"
    ].unique()
    df = df[df["Country"].isin(arr_not)]

    df.to_csv(FULL_DB_PATH, index=False)


if __name__ == "__main__":
    UserInput = 1

    while int(UserInput) > 0 and int(UserInput) <= 4:
        UserInput = input(
            "Hello And Welcome ETZ-GDP!\n    Please enter a choice:\n    Press 1 to Merge Data\n    Press 2 to ML\n    Press 3 for Graphs\n    Press 4 to Clusters\n    Press 0 to Exit.\n-> "
        )
        if int(UserInput) == 1:
            Run_Merge()
            print("Merge Completed!\n")
        elif int(UserInput) == 2:
            Run_ML()
            print("ML Done!\n")
        elif int(UserInput) == 3:
            Run_Graphs()
        elif int(UserInput) == 4:
            Run_Cluster()

    print("Goodbye")
    DF_FULL_P = pd.read_csv(FULL_DB_PATH)
    clean_DF(DF_FULL_P)
    # df= pd.read_csv('../CSV files/df_Full_DataBase.csv')
