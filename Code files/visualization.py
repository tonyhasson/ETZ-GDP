import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

Color_By_Country = {
    "United States": "b",
    "China": "r",
    "United Kingdom": "w",
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
    "Mexico": "fuchsia",
    "Spain": "yellow",
    "Netherlands": "plum",
    "Russia": "wheat",
    "Indonesia": "darkgreen",
    "Switzerland": "darkblue",
    "Saudi Arabia": "darkred",


}

ARR_COLOR = ["red", "teal", "orange", "grey", "green", "yellow", "blue", "purple", "pink", "brown", "cyan"]

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


def GDP_pie_plot(df):
    fig, axes = plt.subplots(1, 2, figsize=(20, 5))
    df_1960 = df[df["Year"] == 1960].sort_values(by=['GDP Total'], ascending=False)
    df_2020 = df[df["Year"] == 2020].sort_values(by=['GDP Total'], ascending=False)

    GDP_1960= [c for c in df_1960.head(15)["GDP Total"]]
    GDP_1960.append(df_1960["GDP Total"].sum()-df_1960.head(15)["GDP Total"].sum())
    list_of_labels_1960 = [c for c in df_1960.head(15)["Country"]]
    list_of_labels_1960.append("Others")
    GDP_2020= [c for c in df_2020.head(15)["GDP Total"]]
    GDP_2020.append(df_2020["GDP Total"].sum()-df_2020.head(15)["GDP Total"].sum())
    list_of_labels_2020 = [c for c in df_2020.head(15)["Country"]]
    list_of_labels_2020.append("Others")


    axes[0].pie(
        GDP_1960,
        labels=list_of_labels_1960,
        shadow=True,
        startangle=90,
        autopct="%1.1f%%",
        colors=[Color_By_Country[key] for key in list_of_labels_1960]
    )
    axes[0].legend(loc="best")
    axes[0].set_title("GDP in 1960")

    axes[1].pie(
        GDP_2020,
        labels=list_of_labels_2020,
        shadow=True,
        startangle=90,
        autopct="%1.1f%%",
        colors=[Color_By_Country[key] for key in list_of_labels_2020]
    )
    axes[1].legend(loc="best")
    axes[1].set_title("GDP in 2020")
    fig.suptitle("GDP in 1960 and 2020")
    plt.show()


    df_2020 = df_2020.tail(-15)
    sum_of_gdp_2020= df_2020["GDP Total"].sum()
    df_2020 = df_2020[df_2020["GDP Total"]>=300000]
    others_gdp = [c for c in df_2020["GDP Total"]]
    others_gdp_names = [c for c in df_2020["Country"]]
    others_gdp.append(sum_of_gdp_2020-df_2020["GDP Total"].sum())
    others_gdp_names.append("Others")
    plt.pie(others_gdp,
            labels=others_gdp_names,
            shadow=True,
            startangle=90,
            autopct="%1.1f%%",
            colors=ARR_COLOR
            )
    plt.legend(loc="best")
    plt.title("GDP in 2020 (Others)")
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





    ##create gdp vs continents bar

    list_gdp=[]
    for c in df["Continent"].unique():
        list_gdp.append(df[df["Continent"]==c]["GDP Total"].mean())

    plt.bar(df["Continent"].unique(),list_gdp,color=ARR_COLOR)
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


    labels = ['1960' , '2020']
    fig, ax = plt.subplots()

    # 1960
    df_1960 = df[df["Year"] == 1960].sort_values(by=['GDP Total'], ascending=False)
    df_2020 = df[df["Year"] == 2020].sort_values(by=['GDP Total'], ascending=False)
    gdp_sum_1960=0
    gdp_sum_2020=0
    i=0

    for c in df_1960["Country"].head(10).unique():
        ax.bar(labels[0], df_1960[df_1960["Country"] == c]["GDP Total"],bottom=gdp_sum_1960, color=Color_By_Country[c], label=c)
        gdp_sum_1960 += df_1960[df_1960["Country"] == c]["GDP Total"].sum()

        i+=1
    ax.bar(labels[0], df_1960["GDP Total"].sum()-gdp_sum_1960,bottom=gdp_sum_1960, color=Color_By_Country[c], label='Others')

    ax.set_ylabel('GDP')
    ax.set_title('GDP in 1960\n%.02f$'%df_1960["GDP Total"].sum())
    ax.legend()
    plt.show()
    fig, ax = plt.subplots()
    i=0
    for c in df_2020["Country"].head(10).unique():
        ax.bar(labels[1], df_2020[df_2020["Country"] == c]["GDP Total"],bottom=gdp_sum_2020, color=Color_By_Country[c], label=c )
        gdp_sum_2020 += df_2020[df_2020["Country"] == c]["GDP Total"].sum()
        i+=1
    ax.bar(labels[1], df_2020["GDP Total"].sum()-gdp_sum_2020,bottom=gdp_sum_2020, color=Color_By_Country[c], label='Others')


    ax.set_ylabel('GDP')
    ax.set_title('GDP in 2020\n%.02f$'%df_2020["GDP Total"].sum())
    ax.legend()
    plt.show()



def GDP_total_world_graph(df):

    GDP_total_world= [df[df["Year"]==c]["GDP Total"].sum() for c in df["Year"].unique()]
    df_2020=df[df["Year"]==2020].sort_values(by=['GDP Total'], ascending=False)
    arr=[]
    country_list=[]

    for c in df_2020["Country"].head(10).unique():
        arr.append([df[(df["Country"]==c) & (df["Year"]==year)]["GDP Total"].sum() for year in df["Year"].unique()])
        country_list.append(c)
    i=0
    plt.plot(df["Year"].unique(),GDP_total_world, label="World")
    for j in arr:
        plt.plot(df["Year"].unique(),j, label=df_2020.head(10)["Country"].unique()[i] , color= Color_By_Country[country_list[i]])
        i+=1
    plt.xlabel("Year")
    plt.ylabel("World GDP Total")
    plt.title("World GDP Growth")
    plt.legend()
    plt.show()


if __name__ == "__main__":

    df = pd.read_csv(r"..\CSV files\df_Full_DataBase.csv")
    df = df.fillna(0)
    # line_plot(df)
    # mix_plot(df)
    GDP_pie_plot(df)
    #sum_of_gdp_bar_graph(df)
    #GDP_total_world_graph(df)
