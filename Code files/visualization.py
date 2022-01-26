from imports import *

# Dictinary with countries and color (very pretty, much wow!)
Color_By_Country = {
    "United States": "b",
    "China": "r",
    "United Kingdom": "orchid",
    "Germany": "grey",
    "India": "orange",
    "France": "navy",
    "Japan": "firebrick",
    "Canada": "bisque",
    "Italy": "lime",
    "Australia": "indigo",
    "Sweden": "gold",
    "Others": "olive",
    "South Korea": "pink",
    "Brazil": "cyan",
    "South Sudan": "tan",
    "Turkey": "chocolate",
    "Mexico": "cyan",
    "Spain": "yellow",
    "Netherlands": "plum",
    "Russia": "wheat",
    "Indonesia": "darkgreen",
    "Switzerland": "darkblue",
    "Saudi Arabia": "darkred",
}

ARR_COLOR = [
    "red",
    "teal",
    "orange",
    "grey",
    "green",
    "yellow",
    "blue",
    "purple",
    "pink",
    "brown",
    "cyan",
    "darkgreen",
    "magenta",
    "tan",
    "aqua",
    "tomato",
    "chocolate",
    "olive",
    "gold",
    "plum",
    "wheat",
    "lime",
]

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


def GDP_pie_plot(df):

    # Create Subplot
    fig, axes = plt.subplots(1, 2, figsize=(20, 5))

    # Take relevant data and sort by gdp
    df_1960 = df[df["Year"] == 1960].sort_values(by=["GDP Total"], ascending=False)
    df_2020 = df[df["Year"] == 2020].sort_values(by=["GDP Total"], ascending=False)

    GDP_1960, list_of_labels_1960, GDP_2020, list_of_labels_2020 = []

    # Extract data from 15 top countries in 1960
    for c in df_1960.head(15):
        GDP_1960.append(c["GDP Total"])
        list_of_labels_1960.append(c["Country"])
    GDP_1960.append(df_1960["GDP Total"].sum() - df_1960.head(15)["GDP Total"].sum())
    list_of_labels_1960.append("Others")

    # Extract data from 15 top countries in 2020
    for c in df_2020.head(15):
        GDP_2020.append(c["GDP Total"])
        list_of_labels_2020.append(c["Country"])
    GDP_2020.append(df_2020["GDP Total"].sum() - df_2020.head(15)["GDP Total"].sum())
    list_of_labels_2020.append("Others")

    axes[0].pie(
        GDP_1960,
        labels=list_of_labels_1960,
        shadow=True,
        startangle=90,
        autopct="%1.1f%%",
        colors=[Color_By_Country[key] for key in list_of_labels_1960],
    )
    axes[0].legend(loc="best")
    axes[0].set_title("GDP in 1960")

    axes[1].pie(
        GDP_2020,
        labels=list_of_labels_2020,
        shadow=True,
        startangle=90,
        autopct="%1.1f%%",
        colors=[Color_By_Country[key] for key in list_of_labels_2020],
    )
    axes[1].legend(loc="best")
    axes[1].set_title("GDP in 2020")
    fig.suptitle("GDP in 1960 and 2020")
    plt.show()

    # Pie chart containt all other countries (not top 15)
    df_2020 = df_2020.tail(-15)
    sum_of_gdp_2020 = df_2020["GDP Total"].sum()
    df_2020 = df_2020[df_2020["GDP Total"] >= 300000]

    others_gdp, others_gdp_names = []

    # Extract data from 2020
    for c in df_2020:
        others_gdp.append(c["GDP Total"])
        others_gdp_names.append(c["Contry"])

    others_gdp.append(sum_of_gdp_2020 - df_2020["GDP Total"].sum())
    others_gdp_names.append("Others")

    plt.pie(
        others_gdp,
        labels=others_gdp_names,
        shadow=True,
        startangle=90,
        autopct="%1.1f%%",
        colors=ARR_COLOR,
    )
    plt.legend(loc="best")
    plt.title("GDP in 2020 (Others)")
    plt.show()


def pie_plot_2030(df):
    df.drop(columns=["Third World", "Least Developed Country"], inplace=True)
    df = df[["Year", "Country", "GDP Total"]]

    arr_data = []
    for country in df["Country"].unique():
        df_a = df[df["Country"] == country].copy()
        df_a.drop(columns=["Country"], inplace=True)

        X, y = load_dataset(df_a, "GDP Total")

        lr = linear_model.LinearRegression()

        x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

        lr.fit(x_train.values, y_train)

        tonyCalc = abs(df_a[df_a["Year"] == 1960]["GDP Total"] - lr.predict(X.values)[0])
        arr_data.append(lr.predict([[2030]])[0])

    df_3030 = pd.DataFrame(data={"Country": df["Country"].unique(), "GDP Prediction": arr_data},
                           columns=['Country', 'GDP Prediction'])
    GDP_2030 = []
    list_of_labels_2030 = []
    df_3030 = df_3030.sort_values(by=["GDP Prediction"], ascending=False)
    print(df_3030)
    # Extract data from 15 top countries in 2030
    for c in df_3030.head(15).values:
        GDP_2030.append(c[1])
        list_of_labels_2030.append(c[0])
    GDP_2030.append(df_3030["GDP Prediction"].sum() - df_3030.head(15)["GDP Prediction"].sum())
    list_of_labels_2030.append("Others")

    plt.pie(
        GDP_2030,
        labels=list_of_labels_2030,
        shadow=True,
        startangle=90,
        autopct="%1.1f%%",
        colors=[Color_By_Country[key] for key in list_of_labels_2030],
    )
    plt.legend(loc="best")
    plt.title("GDP in 2030")
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
    # plt.pie([(least_dev/(least_dev+not_least_dev))*100, (not_least_dev/(least_dev+not_least_dev))*100], labels=["Least Developed Country", "Other"], autopct='%1.1f%%')
    # plt.title("Least developed countries VS rest of the world")
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

    # show continent pie

    dict = {
        "Asia": 0,
        "Europe": 0,
        "Oceania": 0,
        "Africa": 0,
        "Central America": 0,
        "North America": 0,
        "South America": 0,
    }
    total = 0
    for c in df["Country"].unique():
        dict[df[df["Country"] == c]["Continent"].unique()[0]] += 1
        total += 1

    plt.pie(
        [
            (dict["Asia"] / total) * 100,
            (dict["Europe"] / total) * 100,
            (dict["Oceania"] / total) * 100,
            (dict["Africa"] / total) * 100,
            (dict["Central America"] / total) * 100,
            (dict["North America"] / total) * 100,
            (dict["South America"] / total) * 100,
        ],
        labels=[
            "Asia",
            "Europe",
            "Oceania",
            "Africa",
            "Central America",
            "North America",
            "South America",
        ],
        autopct="%1.1f%%",
    )
    plt.title("Countries distribution between continents")
    plt.show()

    # x = list(df[df["Year"] == 2020]["Population Total"])  ## Population
    # y = list(df[df["Year"] == 2020]["GDP Total"])  ## GDP
    #
    # i = 0
    # for continent in df["Continent"].unique():
    #     x = list(
    #         df[(df["Continent"] == continent) & (df["Year"] == 2020)][
    #             "Population Total"
    #         ]
    #     )
    #     y = list(df[(df["Continent"] == continent) & (df["Year"] == 2020)]["GDP Total"])
    #     plt.scatter(x, y, color=ARR_COLOR[i])
    #
    #     i += 1
    # plt.title("GDP/Population in 2020 With Continents")
    # plt.xlabel("Population")
    # plt.ylabel("GDP")
    # plt.legend(df["Continent"].unique(), loc="upper left")
    # plt.show()

    # Create GDP vs continents bar
    list_gdp = []
    for c in df["Continent"].unique():
        list_gdp.append(df[df["Continent"] == c]["GDP Total"].mean())

    plt.bar(df["Continent"].unique(), list_gdp, color=ARR_COLOR)
    plt.xlabel("Continents")
    plt.ylabel("GDP Total")
    plt.title("Continents vs GDP")
    plt.show()

    #
    # i = 0
    # for contint in df["Continent"].unique():
    #     x = []
    #     y = []
    #     for year in range(
    #         min(df[df["Continent"] == contint]["Year"]),
    #         max(df[df["Continent"] == contint]["Year"]),
    #     ):
    #         x.append(
    #             (
    #                 df[(df["Continent"] == contint) & (df["Year"] == year)][
    #                     "GDP Total"
    #                 ].median()
    #             )
    #         )
    #         y.append(year)
    #     plt.plot(y, x, color=ARR_COLOR[i])
    #     i += 1
    #
    # plt.xlabel("Year")
    # plt.ylabel("GDP")
    # plt.legend(df["Continent"].unique(), loc="upper left")
    # plt.title("AVG GDP per continent along 1960-2020")
    # plt.show()


def sum_of_gdp_bar_graph(df):

    labels = ["1960", "2020"]
    fig, ax = plt.subplots(1, 2, figsize=(20, 5))

    # 1960
    df_1960 = df[df["Year"] == 1960].sort_values(by=["GDP Total"], ascending=False)
    df_2020 = df[df["Year"] == 2020].sort_values(by=["GDP Total"], ascending=False)
    gdp_sum_1960 = 0
    gdp_sum_2020 = 0

    # Sum up the top 10 countries in 1960 (According to GDP)
    for c in df_1960["Country"].head(10).unique():
        ax[0].bar(
            labels[0],
            df_1960[df_1960["Country"] == c]["GDP Total"],
            width=0.1,
            bottom=gdp_sum_1960,
            color=Color_By_Country[c],
            label=c,
        )
        # Add text to each stack
        ax[0].text(
            labels[0],
            gdp_sum_1960 + 100,
            "%.02f" % df_1960[df_1960["Country"] == c]["GDP Total"].sum(),
            ha="center",
            va="bottom",
        )
        gdp_sum_1960 += df_1960[df_1960["Country"] == c]["GDP Total"].sum()

    # Sum up the other countries (not in top 10)
    ax[0].bar(
        labels[0],
        df_1960["GDP Total"].sum() - gdp_sum_1960,
        width=0.1,
        bottom=gdp_sum_1960,
        color=Color_By_Country["Others"],
        label="Others",
    )
    ax[0].text(
        labels[0],
        gdp_sum_1960 + 100,
        "%.02f" % (df_1960["GDP Total"].sum() - gdp_sum_1960),
        ha="center",
        va="bottom",
    )

    ax[0].set_ylabel("GDP")
    ax[0].set_title("GDP in 1960\n%.02f$" % df_1960["GDP Total"].sum())
    ax[0].legend()

    # Sum up the top 10 countries in 2020 (According to GDP)
    for c in df_2020["Country"].head(10).unique():
        ax[1].bar(
            labels[1],
            df_2020[df_2020["Country"] == c]["GDP Total"],
            width=0.1,
            bottom=gdp_sum_2020,
            color=Color_By_Country[c],
            label=c,
        )
        ax[1].text(
            labels[1],
            gdp_sum_2020 + 100,
            "%.02f" % (df_2020[df_2020["Country"] == c]["GDP Total"].sum()),
            ha="center",
            va="bottom",
        )
        gdp_sum_2020 += df_2020[df_2020["Country"] == c]["GDP Total"].sum()
    # Sum up the other countries (not in top 10)
    ax[1].bar(
        labels[1],
        df_2020["GDP Total"].sum() - gdp_sum_2020,
        width=0.1,
        bottom=gdp_sum_2020,
        color=Color_By_Country["Others"],
        label="Others",
    )
    ax[1].text(
        labels[1],
        gdp_sum_2020 + 100,
        "%.02f" % (df_2020["GDP Total"].sum() - gdp_sum_2020),
        ha="center",
        va="bottom",
    )

    ax[1].set_ylabel("GDP")
    ax[1].set_title("GDP in 2020\n%.02f$" % df_2020["GDP Total"].sum())
    ax[1].legend()
    plt.show()


def GDP_total_world_graph(df):
    """Display Graph Showing the total GDP of the world per year(line graph)

    Args:
        df
    Returns:
        displays graph
    """
    # Variable initialization
    arr, country_list = []
    i = 0

    # Summing up each year total GDP
    GDP_total_world = [
        df[df["Year"] == c]["GDP Total"].sum() for c in df["Year"].unique()
    ]

    # Extract year 2020 and sort by GDP
    df_2020 = df[df["Year"] == 2020].sort_values(by=["GDP Total"], ascending=False)

    # Extract the top 10 coutries
    for c in df_2020["Country"].head(10).unique():
        arr.append(
            [
                df[(df["Country"] == c) & (df["Year"] == year)]["GDP Total"].sum()
                for year in df["Year"].unique()
            ]
        )
        country_list.append(c)

    plt.plot(df["Year"].unique(), GDP_total_world, label="World")

    # Add the top countries in 2020 to graph
    for j in arr:
        plt.plot(
            df["Year"].unique(),
            j,
            label=df_2020.head(10)["Country"].unique()[i],
            color=Color_By_Country[country_list[i]],
        )
        i += 1
    plt.xlabel("Year")
    plt.ylabel("World GDP Total")
    plt.title("World GDP Growth")
    plt.legend()
    plt.show()


# Driver Code:
if __name__ == "__main__":
    df = pd.read_csv(r"..\CSV files\df_Full_DataBase.csv")
    df = df.fillna(0)
    # line_plot(df)
    # mix_plot(df)
    GDP_pie_plot(df)
    sum_of_gdp_bar_graph(df)
    GDP_total_world_graph(df)
    pie_plot_2030(df)  ##added by tony
