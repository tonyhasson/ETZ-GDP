from imports import *
from Merge import Run as Run_Merge
from ML_Algo import Run as Run_ML


if __name__ == "__main__":
    DF_FULL, DF_SCRAPE = Run_Merge()
    #DF_FULL, DF_SCRAPE = Run_ML()
    # df= pd.read_csv('../CSV files/df_Full_DataBase.csv')
