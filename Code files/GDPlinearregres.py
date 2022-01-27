from imports import *
from ML_Algo import load_dataset

df = pd.read_csv(r"../CSV files/df_Full_DataBase.csv")


def GDP_estimated():
    """Regres and calcuate the GDP in the next decade
    Args:
        df: dataframe (full_db)
        R: testing purposes
    Returns:
        None ()
    """
    global df
    total_year = [year for year in range(1960, 2031)]
    prediction_year = [[year] for year in range(2021, 2031)]
    GDP_est_data = []

    # Drop all unnecessary columns
    df = df[["Year", "Country", "GDP Total"]]

    for country in df["Country"].unique():

        df_a = df[df["Country"] == country].copy()
        df_a.drop(columns=["Country"], inplace=True)

        # Split the data set
        X, y = load_dataset(df_a, "GDP Total")

        # OLD code
        # lr = linear_model.LinearRegression()

        # Polynomial and Linear Regression pipeline
        lr = make_pipeline(PolynomialFeatures(degree={2, 5}), LinearRegression())

        # Split the data
        x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

        # Fit the model
        lr.fit(x_train.values, y_train)

        # Merge all predicted data
        y_pred = lr.predict(prediction_year)
        fixed_predict_values = [c for c in lr.predict(X.values)]
        total_values = [c for c in fixed_predict_values]
        for data in y_pred:
            total_values.append(data)

        for year, pred in zip(prediction_year, y_pred):
            GDP_est_data.append([country, year[0], pred])

        # Create 1960-2030 year array

        ############################################# Plot the data
        # plt.plot(df_a['Year'], df_a['GDP Total'])
        # plt.plot(total_year,total_values, color='red', linewidth=1)
        # y_pred= lr.predict(x_test.values)
        # plt.title("Country: %s   R2: %.02f"%(country, r2_score(y_test,y_pred)))
        # plt.xlabel('Year')
        # plt.ylabel('GDP Total')
        # plt.show()
    GDP_est_df = pd.DataFrame(
        GDP_est_data,
        columns=["Country", "Year", "GDP Total"],
    )
    GDP_est_df.to_csv(r"../CSV FILES/GDP est.csv", index=False)
    return GDP_est_df


GDP_estimated()
