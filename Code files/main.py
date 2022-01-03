from imports import *
from Merge import Run as MergeRun
from ML_Education_rank import Run as Run_ML_Education_rank
##############################################################################
##################                TO DO LIST                ##################
##############################################################################
#   1. Clean the data                                                        #                       
#   2. Analyze the data                                                      #                       
#   3. Correlation between different things                                   #
#   4. Make plots                                                            #                   
#   5.                                                                       #       
#   6.                                                                       #       
#   7.                                                                       #
#   8.                                                                       #
#   9.                                                                       #
#   10.                                                                      #       
##############################################################################

if __name__ == "__main__":
    MergeRun()
    df=Run_ML_Education_rank()
    #df= pd.read_csv('../CSV files/df_Full_DataBase.csv')