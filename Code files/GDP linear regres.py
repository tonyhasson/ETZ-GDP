import numpy as np

from imports import *
from ML_Algo import load_dataset
df = pd.read_csv(r"../CSV files/df_Full_DataBase.csv")





def GDP_estimated(df,R):
    """Regres and calcuate the GDP in the next decade
    Args:
        df: dataframe (full_db)
        R: testing purposes
    Returns:
        None ()
    """

    df.drop(columns=["Third World","Least Developed Country"], inplace=True)

    for country in df["Country"].unique():

        df_a = df[df["Country"] == country].copy()
        df_a.drop(columns=["Country"], inplace=True)


        X,y = load_dataset(df_a,"GDP Total")

        lr = linear_model.LinearRegression()

        lr.fit(X.values,y)

        x_train, x_test, y_train, y_test = train_test_split(X,y,test_size=0.1,random_state=1)

        lr.fit(x_train,y_train)
        x_test = x_test.append({"Year":2021},ignore_index=True)
        x_test.replace(np.NaN,0,inplace=True)
        x_test = x_test.tail(1)

        #print(x_test)
        y_pred = lr.predict(x_test)
        if country == "Israel":
            print(y_pred)
        #R.append(r2_score(y_test,y_pred))

        #print("r2 score: ",r2_score(y_test,y_pred))


        #Medubbeg with print
        # print(country)
        # R.append(lr.score(X,y))
        # print("R:%f"%lr.score(X,y))
        # print("coef:",lr.coef_)
        # print("intercept:",lr.intercept_)
        # print("\n")
        #end Debbug with prints






R=[]
GDP_estimated(df,R)
# print("AVG score for GDP estimation:",sum(R)/len(R))
# print("AVG r2 score:",sum(R)/len(R))
