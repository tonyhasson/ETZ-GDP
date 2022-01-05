from imports import *
from Merge import Run as Run_Merge
from ML_Algo import Run as Run_ML


##############################################################################
##################                TO DO LIST                ##################
##############################################################################
#   1. Clean the data                                                        #
#   2. Analyze the data                                                      #
#   3. Correlation between different things                                  #
#   4. Make plots                                                            #
#   5.                                                                       #
#   6.                                                                       #
#   7.                                                                       #
#   8.                                                                       #
#   9.                                                                       #
#   10.                                                                      #
##############################################################################

if __name__ == "__main__":
    DF_FULL,DF_SCRAPE=Run_Merge()
    DF_FULL,DF_SCRAPE =Run_ML()
    # df= pd.read_csv('../CSV files/df_Full_DataBase.csv')
