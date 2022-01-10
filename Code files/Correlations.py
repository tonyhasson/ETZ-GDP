from imports import *
FULL_DB_PATH = r"../CSV files/df_Full_DataBase.csv"
SCRAP_DB_PATH = r"../CSV files/df_scrape.csv"

#TODO function to check which columns are correlated
def Correlations(df):
    df.drop(["Country", "Year"], axis=1, inplace=True)
    df=df.corr().values
    for i in range(len(df)):
        for j in range(len(df[i])):
            if (df[i][j]>0.4 or df[i][j]<-0.3) and i!=j:
                Plot(df,df.columns[i],df.columns[j])




#TODO function to print plot 2 columns
def Plot(df,col1,col2):
    df.plot(df[col1],df[col2])
    plt.show()
