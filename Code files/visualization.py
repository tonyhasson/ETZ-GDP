import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

ARR_COLOR = ["red", "black", "orange", "grey", "green", "yellow", "blue"]

# TODO check life expectancy at 1960 and 2020 calc diff
# TODO

# def plot_frequent_elements(df, df_in_params):
#     col_amount = df_in_params.shape[0]
#     fig, axes = plt.subplots(1, col_amount, figsize=(20, 5))
#
#     for i in range(col_amount):
#         sr = get_frequent_elements(df,df_in_params['col_name'][i],df_in_params['num_top_elements'][i])
#         one_dim_plot(sr,df_in_params['plot_type'][i],axes[i])


##line plot
def line_plot(df):
    # fig, axes = plt.subplots(1, 1, figsize=(20, 5))

    x = df[df["Country"] == "Israel"]["GDP Total"]

    arr = list(x)
    plt.plot(arr, linestyle="dotted")
    plt.show()


##pie chart
def mix_plot(df):

    # ##check third_world vs other
    #
    # countries_name=df["Country"].unique()
    # third_world=not_third_world=0
    # for c in countries_name:
    #     if df[df["Country"]==c]["Third World"].unique()[0]:
    #         third_world+=1
    #     else:
    #         not_third_world+=1
    #
    # plt.pie([third_world,not_third_world],labels=["Third World","Other"])
    # plt.show()
    #
    # ##check third_world vs other
    #
    # countries_name = df["Country"].unique()
    # least_dev = not_least_dev = 0
    # for c in countries_name:
    #     if df[df["Country"] == c]["Least Developed Country"].unique()[0]:
    #         least_dev += 1
    #     else:
    #         not_least_dev += 1
    #
    # plt.pie([least_dev, not_least_dev], labels=["Least Developed Country", "Other"])
    # plt.show()
    #
    #
    # ## bar plot check how much of third_world is least developed countries
    # x=np.array([least_dev, third_world])
    # plt.bar(["Least Developed Country", "Total Third World"],x)
    # plt.show()
    #
    #
    #

    x = list(df[df["Year"] == 2020]["Population Total"])  ## Population
    y = list(df[df["Year"] == 2020]["GDP Total"])  ## GDP

    i = 0
    for continent in df["Continent"].unique():
        x = list(
            df[(df["Continent"] == continent) & (df["Year"] == 2020)][
                "Population Total"
            ]
        )
        y = list(df[(df["Continent"] == continent) & (df["Year"] == 2020)]["GDP Total"])
        plt.scatter(x, y, color=ARR_COLOR[i])

        i += 1
    plt.title("GDP/Population in 2020 With Continents")
    plt.xlabel("Population")
    plt.ylabel("GDP")
    plt.legend(df["Continent"].unique(), loc="upper left")
    plt.show()

    i = 0
    for contint in df["Continent"].unique():
        x = []
        y = []
        for year in range(
            min(df[df["Continent"] == contint]["Year"]),
            max(df[df["Continent"] == contint]["Year"]),
        ):
            x.append(
                (
                    df[(df["Continent"] == contint) & (df["Year"] == year)][
                        "GDP Total"
                    ].median()
                )
            )
            y.append(year)
        plt.plot(y, x, color=ARR_COLOR[i])
        i += 1
    plt.title("AVG GDP per continent along 1960-2020")
    plt.show()


if __name__ == "__main__":

    df = pd.read_csv(r"..\CSV files\df_Full_DataBase.csv")
    df=df.fillna(0)
    line_plot(df)
    mix_plot(df)
