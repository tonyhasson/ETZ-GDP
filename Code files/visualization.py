import matplotlib.pyplot as plt
from imports import *
from Correlations import GENOCIDE_list

# from GDPlinearregres import GDP_estimated

df = pd.read_csv(FULL_DB_PATH)
df_total = pd.read_csv(r"..\CSV files\df_total.csv")
GDP_est = pd.read_csv(r"..\CSV files\GDP est.csv")

# Dictionary with countries and color (very pretty, much wow!)
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
    "Zimbabwe": "darkorange",
    "Zambia": "darkgreen",
    "Kenya": "darkcyan",
    "Thailand": "darkgoldenrod",
    "Philippines": "darkkhaki",
    "South Africa": "darkolivegreen",
    "Argentina": "darkseagreen",
    "Yemen": "black",
    "Nigeria": "darkorchid",
    "Vietnam": "darkviolet",
    "Venezuela": "lightyellow",
    "Finland": "lightblue",
    "Denmark": "lightgreen",
    "Belgium": "lightpink",
    "Norway": "lightgrey",
    "Poland": "lightcyan",
    "Ireland": "orange",
    "Ivory Coast": "darkorange",
    "Tanzania": "teal",
    "Somalia": "darkturquoise",
    "Ethiopia": "darkseagreen",
    "Egypt": "darkkhaki",
    "Uganda": "gold",
    "Belarus": "red",
    "Hungary": "darkred",
    "Malta": "purple",
    "Kuwait": "darkblue",
    "Greece": "brown",
    "Cyprus": "pink",
    "Singapore": "darkgreen",
    "Bahrain": "lightpink",
    "Mozambique": "fuchsia",
    "Cameroon": "darkcyan",
    "Oman": "aqua",
    "Qatar": "darkcyan",
    "Lebanon": "aquamarine",
    "Malaysia": "azure",
    "Sri Lanka": "darkgoldenrod",
    "Syria": "ivory",
    "Cambodia": "coral",
    "Laos": "orangered",
    "Ghana": "olive",
    "Fiji": "lavender",
    "Mauritius": "magenta",
    "Guinea": "salmon",
    "Libya": "lime",
    "Belize": "red",
    "Mali": "darkgreen",
    "United Arab Emirates": "green",
    "Iceland": "darkblue",
    "Luxembourg": "darkgreen",
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


def pie_per_year(ax, df, year):
    GDP = []
    labels = []
    df = df[df["Year"] == year]
    df = df.sort_values(by="GDP Total", ascending=False)
    df = df[["Country", "GDP Total"]]
    for c in df.head(15).values:
        GDP.append(c[1])
        labels.append(c[0])
    GDP.append(df["GDP Total"].sum() - df.head(15)["GDP Total"].sum())
    labels.append("Others")
    ax.pie(
        GDP,
        labels=labels,
        shadow=True,
        startangle=90,
        autopct="%1.1f%%",
        colors=[Color_By_Country[key] for key in labels],
    )

    ax.set_title("GDP in %d" % year)
    return ax


def GDP_pie_plot():
    """Displays GDP plot pie
    Args:
        None
    Returns:
        None
    """
    # Create Subplot
    fig, ax = plt.subplots(1, 3, figsize=(20, 5))

    # Get GDP estimates
    df_2030 = GDP_estimated()

    index = 0
    for i in [1960, 2020]:
        ax[index] = pie_per_year(ax[index], df[df["Year"] == i], i)
        index += 1

    ax[index] = pie_per_year(ax[index], df_2030, 2030)
    fig.suptitle("GDP in 1960 VS 2020 VS 2030")
    plt.show()

    # Pie chart contains all other countries (not top 15)
    df_2020 = df[df["Year"] == 2020].sort_values(by="GDP Total", ascending=False)
    df_2020 = df_2020[["Country", "GDP Total"]]
    df_2020 = df_2020.tail(-15)
    sum_of_gdp_2020 = df_2020["GDP Total"].sum()

    df_2020 = df_2020[df_2020["GDP Total"] >= 250000000000]

    others_gdp = []
    others_gdp_names = []

    # Extract data from 2020
    for c in df_2020.values:
        others_gdp.append(c[1])
        others_gdp_names.append(c[0])

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
    # plt.legend(loc="best")
    plt.title("GDP in 2020 (Others)")
    plt.show()


def country_cont_dist():
    # show continent pie

    # dict = {
    #     0: "Asia",
    #     1: "Europe",
    #     5: "Oceania",
    #     6: "Africa",
    #     2: "Central America",
    #     3: "North America",
    #     4: "South America",
    # }

    dict = {
        "0": 0,
        "1": 0,
        "5": 0,
        "6": 0,
        "2": 0,
        "3": 0,
        "4": 0,
    }
    total = 0

    for c in df["Country"].unique():

        dict[str(df[df["Country"] == c]["Continent"].unique()[0])] += 1
        total += 1

    plt.pie(
        [
            (dict["0"] / total) * 100,
            (dict["1"] / total) * 100,
            (dict["5"] / total) * 100,
            (dict["6"] / total) * 100,
            (dict["2"] / total) * 100,
            (dict["3"] / total) * 100,
            (dict["4"] / total) * 100,
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
    plt.legend([dict[i] for i in dict], loc="upper left")
    plt.show()


def scatter_gdp_conts():

    ##displays the countries according to gdp in scatter in year 2020

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


def GDP_vs_Cont_Bar():

    # Create GDP vs continents bar
    list_gdp = []
    for c in df["Continent"].unique():
        list_gdp.append(df[df["Continent"] == c]["GDP Total"].mean())

    plt.bar(df["Continent"].unique(), list_gdp, color=ARR_COLOR)
    plt.xlabel("Continents")
    plt.ylabel("GDP Total")
    plt.title("Continents vs GDP")
    plt.show()


def Stack_GDP(ax, df):
    """Stack GDP inorder to show stacked bar chart
    Args:
        ax: ax of the plot
        df: dataframe
    Returns:
        ax: ax of the plot
    """
    gdp_sum = 0
    for c in df["Country"].head(10).unique():
        ax.bar(
            df["Year"].unique(),
            df[df["Country"] == c]["GDP Total"],
            width=0.1,
            bottom=gdp_sum,
            color=Color_By_Country[c],
            label=c,
        )
        # Add text to each stack
        ax.text(
            df["Year"].unique(),
            gdp_sum + 100,
            "%ldm" % (df[df["Country"] == c]["GDP Total"].sum() / 1000000),
            ha="center",
            va="bottom",
        )
        gdp_sum += df[df["Country"] == c]["GDP Total"].sum()

    # Sum up the other countries (not in top 10)
    ax.bar(
        df["Year"].unique(),
        df["GDP Total"].sum() - gdp_sum,
        width=0.1,
        bottom=gdp_sum,
        color=Color_By_Country["Others"],
        label="Others",
    )
    ax.text(
        df["Year"].unique(),
        gdp_sum + 100,
        "%ldm" % ((df["GDP Total"].sum() - gdp_sum) / 1000000),
        ha="center",
        va="bottom",
    )

    ax.set_ylabel("GDP")
    ax.set_title(
        "GDP in %d\n%ldB$" % (df["Year"].unique(), (df["GDP Total"].sum() / 1000000000))
    )
    ax.legend()
    return ax


def sum_of_gdp_bar_graph():
    """displays GDP stacked bar graph
    Args:
        None
    Returns:
        None  - displays graph
    """

    labels = ["1960", "2020", "2030"]  # ? we dont use it?
    fig, ax = plt.subplots(1, 3, figsize=(20, 5))

    index = 0
    for i in [1960, 2020]:
        ax[index] = Stack_GDP(
            ax[index],
            df[df["Year"] == i].sort_values(by=["GDP Total"], ascending=False),
        )
        index += 1
    ax[index] = Stack_GDP(
        ax[index],
        GDP_est[GDP_est["Year"] == 2030].sort_values(by=["GDP Total"], ascending=False),
    )

    plt.show()


def GDP_total_world_graph():
    """Display Graph Showing the total GDP of the world per year(line graph)

    Args:
        None
    Returns:
        None - displays graph
    """
    # Variable initialization
    arr = []
    country_list = []
    i = 0

    # Summing up each year total GDP
    GDP_total_world = [
        df[df["Year"] == year]["GDP Total"].sum() for year in df["Year"].unique()
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

    fig, ax = plt.subplots(1, 1, figsize=(20, 5))
    ax.plot(df["Year"].unique(), GDP_total_world, label="World")
    # Add the top countries in 2020 to graph
    for j in arr:
        ax.plot(
            df["Year"].unique(),
            j,
            label=df_2020.head(10)["Country"].unique()[i],
            color=Color_By_Country[country_list[i]],
        )
        i += 1

    plt.xlabel("Year")
    plt.ylabel("World GDP Total")
    plt.title("World GDP Growth")
    ax.legend()
    plt.show()


def Genocide_Plots():
    """Display Graph Showing the total GDP of the 'Genocide List' countries per year (line graph)

    Args:
        None
    Returns:
        None - displays graph
    """
    for label in df.columns:
        if label in [  # label we don't want to see:
            "Country",
            "Year",
            "Continent",
            "Government expenditure (% of GDP)",
            "Military expenditure (% of GDP)",
            "Total government Expenses (% of GDP)",
            "Total consumption ($)",
            "Least Developed Country",
            "Third World",
        ]:
            continue
        # else:
        i = 0
        for country in GENOCIDE_list:
            x = []
            y = []
            for year in range(1960, 2021):
                x.append((df[(df["Country"] == country) & (df["Year"] == year)][label]))
                y.append(year)
            plt.plot(y, x, color=ARR_COLOR[i])
            i += 1

        plt.xlabel("Year")
        plt.ylabel(label)
        plt.legend(GENOCIDE_list, loc="upper left")
        plt.title(f"{label} per 'Genocide & Wars' List along 1960-2020")
        plt.show()


def top5bottom5countries():

    Column_list = list(df_total.columns)
    Column_list.remove("Year")
    Column_list.remove("Country")
    Column_list.remove("Third World")
    Column_list.remove("Least Developed Country")
    Column_list.remove("Continent")

    for column in Column_list:
        fig, ax = plt.subplots(1, 1, figsize=(20, 5))
        df = df_total[df_total["Year"] == 2020].sort_values(by=column, ascending=False)
        for country in df["Country"].head(5).unique():
            ax.plot(
                df_total[(df_total["Country"] == country) & (df_total["Year"] >= 2009)][
                    "Year"
                ],
                df_total[df_total["Country"] == country][column],
                label=country,
                color=Color_By_Country[country],
            )

        i = 0
        for country in df["Country"].tail(5).unique():

            ax.plot(
                df_total[(df_total["Country"] == country) & (df_total["Year"] >= 2009)][
                    "Year"
                ],
                df_total[df_total["Country"] == country][column],
                label=country,
                color=ARR_COLOR[i],
            )
            i += 1
        ax.set_title(f"Top 5 and last 5 Countries by {column}")
        ax.set_ylabel(column)
        ax.legend()
        plt.show()


# Driver Code:
def Run():
    UserInput = 1
    while int(UserInput) > 0 and int(UserInput) <= 4:
        UserInput = input(
            "Welcome to the visualization tool.\n    Please enter a choice\n    Press 1 for GDP pie plot\n    Press 2 for GDP bar plot\n    Press 3 for GDP total world graph\n    Press 4 for 'Genocide & Wars' labels Graphs\n    Press 5 for Top 5 and worst 5 in each column\n    Press 6 for distribution of countries in each continent\n    Press 7 for scatter plot of the countries in 2020 according to GDP\n    Press 8 for bar plot of Continents and GDP\n    Press 0 for main menu\n-> "
        )

        if int(UserInput) == 1:
            GDP_pie_plot()
        elif int(UserInput) == 2:
            sum_of_gdp_bar_graph()
        elif int(UserInput) == 3:
            GDP_total_world_graph()
        elif int(UserInput) == 4:
            Genocide_Plots()
        elif int(UserInput) == 5:
            top5bottom5countries()
        elif int(UserInput) == 6:
            country_cont_dist()
        elif int(UserInput) == 7:
            scatter_gdp_conts()
        elif int(UserInput) == 8:
            GDP_vs_Cont_Bar()
        else:
            break
