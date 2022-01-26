from imports import *
from ML_Algo import load_dataset

df = pd.read_csv(r"../CSV files/df_Full_DataBase.csv")


# def GDP_estimated(df, R):
#     """Regres and calculate the GDP in the next decade
#     Args:
#         df: dataframe (full_db)
#         R: testing purposes
#     Returns:
#         None ()
#     """
#
#     df.drop(columns=["Third World", "Least Developed Country"], inplace=True)
#     df = df[["Year", "Country", "GDP Total"]]
#
#     for country in df["Country"].unique():
#
#         df_a = df[df["Country"] == country].copy()
#         df_a.drop(columns=["Country"], inplace=True)
#
#         X, y = load_dataset(df_a, "GDP Total")
#
#         lr = linear_model.LinearRegression()
#
#         # lr.fit(X.values,y)
#
#         x_train, x_test, y_train, y_test = train_test_split(
#             X, y, test_size=0.2, random_state=0
#         )
#
#         lr.fit(x_train.values, y_train)
#
#         prediction_year = [[year] for year in range(2021, 2030)]
#         print("Value to add", lr.predict(X.values)[0])
#         tonyCalc = abs(
#             df_a[df_a["Year"] == 1960]["GDP Total"] - lr.predict(X.values)[0]
#         )
#
#         y_pred = lr.predict(prediction_year)
#
#         print(X)
#         print(y)
#
#         print(y_pred)
#
#         arr = [c + tonyCalc for c in lr.predict(X.values)]
#
#         plt.scatter(
#             x=df_a["Year"], y=df_a["GDP Total"], c="k", marker="*", label="Digital"
#         )
#         plt.plot(df_a["Year"], arr, "k", color="blue", linewidth=3)
#
#         plt.xlabel("Year")
#         plt.ylabel("GDP Total")
#         plt.show()
#
#         y_pred = lr.predict(x_test.values)
#         R.append(r2_score(y_test, y_pred))
#
#         print("r2 score: ", r2_score(y_test, y_pred))
#
#         # Medubbeg with print
#         # print(country)
#         # R.append(lr.score(X,y))
#         # print("R:%f"%lr.score(X,y))
#         # print("coef:",lr.coef_)
#         # print("intercept:",lr.intercept_)
#         # print("\n")
#         # end Debbug with prints


def GDP_estimated(df,R):
    """Regres and calcuate the GDP in the next decade
    Args:
        df: dataframe (full_db)
        R: testing purposes
    Returns:
        None ()
    """

    df.drop(columns=["Third World","Least Developed Country"], inplace=True)
    df = df[["Year","Country","GDP Total"]]

    for country in df["Country"].unique():

        df_a = df[df["Country"] == country].copy()
        df_a.drop(columns=["Country"], inplace=True)


        X,y = load_dataset(df_a,"GDP Total")

        lr = linear_model.LinearRegression()

        # lr.fit(X.values,y)

        x_train, x_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=0)

        lr.fit(x_train.values,y_train)

        prediction_year = [[year] for year in range(2021,2031)]
        print("Value to add",lr.predict(X.values)[0])
        tonyCalc = 0 #abs(df_a[df_a["Year"] == 1960]["GDP Total"] - lr.predict(X.values)[0])

        # Create 1960-2030 data array
        y_pred = lr.predict(prediction_year)
        fixed_predict_values=[c+tonyCalc for c in lr.predict(X.values)]
        total_values=[c for c in fixed_predict_values]
        for data in y_pred:
            total_values.append(data+tonyCalc)

        # Create 1960-2030 year array
        total_year=[year for year in range(1960,2031)]

        # plt.scatter(x=df_a['Year'], y=df_a['GDP Total'], c='k', marker='*', label='Digital')
        plt.plot(df_a['Year'], df_a['GDP Total'])
        plt.plot(total_year,total_values,'k' , color='red', linewidth=3)
        plt.title("Country: %s   Coef: %f"%(country,lr.coef_))
        plt.xlabel('Year')
        plt.ylabel('GDP Total')
        plt.show()



        y_pred = lr.predict(x_test.values)
        R.append(r2_score(y_test,y_pred))

        print("r2 score: ",r2_score(y_test,y_pred))

R = []
GDP_estimated(df, R)
# print("AVG score for GDP estimation:",sum(R)/len(R))
print("AVG r2 score:", sum(R) / len(R))
