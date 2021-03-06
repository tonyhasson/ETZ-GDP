import matplotlib.pyplot as plt

from imports import *


YEARS = [i for i in range(1960, 2021)]

# List of all countries that were in USSR
USSR_list = [
    "Armenia",
    "Azerbaijan",
    "Belarus",
    "Estonia",
    "Georgia",
    "Kazakhstan",
    "Kyrgyzstan",
    "Latvia",
    "Lithuania",
    "Moldova",
    "Russia",
    "Tajikistan",
    "Turkmenistan",
    "Ukraine",
    "Uzbekistan",
]

# List of all countries that had genocide
GENOCIDE_list = [
    "Afghanistan",
    "Angola",
    "Bangladesh",
    "Bosnia and Herzegovina",
    "Cambodia",
    "Democratic Republic of the Congo",
    "Eritrea",
    "Ethiopia",
    "Guatemala",
    "Iraq",
    "Lebanon",
    "Myanmar",
    "Nigeria",
    "Sierra Leone",
    "Sudan",
    "Timor-Leste",
    "Uganda",
    "Vietnam",
    "Yemen",
]


def Plot(df, col1, col2, data_title):
    """Function to print plot 2 columns

    Args:
        df (dataframe): Our dataframe containing the data.
        col1 (string): Target column to plot with.
        col2 (string): Target column to plot with.
        data_title (string): Data title for the plot.

    Returns:
        None
    """
    plt.scatter(df[col1], df[col2])
    plt.xlabel(col1)
    plt.ylabel(col2)
    plt.title("Correlations: %f" % data_title)
    # add line
    if data_title > 0.7:
        axes = plt.gca()
        x_vals = np.array(axes.get_xlim())
        y_vals = 0 + data_title * x_vals

        plt.plot(x_vals, y_vals, "--", color="Red")
    #
    plt.show()


def Correlations(df):
    """Check which columns are correlated

    Args:
        df (dataframe): Our dataframe containing the data

    Returns:
        None
    """
    # df.drop(["Country", "Year", "Continent"], axis=1, inplace=True)
    df.drop("Country", axis=1, inplace=True)
    cols = df.columns
    df_corr = df.corr().values
    for i in range(len(df_corr)):
        for j in range(len(df_corr[i])):
            if (df_corr[i][j] > 0.4 or df_corr[i][j] < -0.3) and i != j:
                Plot(df, cols[i], cols[j], df_corr[i][j])
    # ax = sns.heatmap(df.corr(),linewidths=1)
    # plt.show()


def USA_RUSS_CHINA(df, label):
    """Function to print plot between USA, Russia and China with the given label

    Args:
        df (dataframe): Our dataframe containing the data.
        col1 (string): Target column to plot with.

    Returns:
        None
    """
    plt.plot(
        df[df["Country"] == "United States"]["Year"],
        df[df["Country"] == "United States"][label],
        label="United States",
    )
    plt.plot(
        df[df["Country"] == "Russia"]["Year"],
        df[df["Country"] == "Russia"][label],
        label="Russia",
    )
    plt.plot(
        df[df["Country"] == "China"]["Year"],
        df[df["Country"] == "China"][label],
        label="China",
    )
    plt.xlabel("Year")
    plt.ylabel(label)
    plt.legend()
    plt.show()


def Continent_VS(df, label):
    """Plot the giving label for each continent.

    Args:
        df (dataframe): dataframe containing our data.
        label (string): The target label.

    Returns:
        None
    """

    # Continents Initialized as:
    # dict = {
    #     "Asia": 0,
    #     "Europe": 1,
    #     "Central America": 2,
    #     "North America": 3,
    #     "South America": 4,
    #     "Oceania": 5,
    #     "Africa": 6,
    # }

    year_Asia = []
    year_Europe = []
    year_Africa = []
    year_NorthAmerica = []
    year_SouthAmerica = []
    year_CentAmerica = []
    year_Oceania = []

    # Calculate data for each continent.
    for i in YEARS:
        year_Asia.append(
            df[(df["Year"] == i) & (df["Continent"] == 0)][label].values.mean()
        )
        year_Africa.append(
            df[(df["Year"] == i) & (df["Continent"] == 6)][label].values.mean()
        )
        year_Europe.append(
            df[(df["Year"] == i) & (df["Continent"] == 1)][label].values.mean()
        )
        year_NorthAmerica.append(
            df[(df["Year"] == i) & (df["Continent"] == 3)][label].values.mean()
        )
        year_CentAmerica.append(
            df[(df["Year"] == i) & (df["Continent"] == 2)][label].values.mean()
        )
        year_SouthAmerica.append(
            df[(df["Year"] == i) & (df["Continent"] == 4)][label].values.mean()
        )
        year_Oceania.append(
            df[(df["Year"] == i) & (df["Continent"] == 5)][label].values.mean()
        )

    # Adding each continent to the plot
    plt.plot(
        YEARS,
        year_Asia,
        label="Asia",
    )
    plt.plot(
        YEARS,
        year_Africa,
        label="Africa",
    )
    plt.plot(
        YEARS,
        year_Europe,
        label="Europe",
    )
    plt.plot(
        YEARS,
        year_NorthAmerica,
        label="North America",
    )
    plt.plot(
        YEARS,
        year_CentAmerica,
        label="Central America",
    )
    plt.plot(
        YEARS,
        year_SouthAmerica,
        label="South America",
    )
    plt.plot(
        YEARS,
        year_Oceania,
        label="Oceania",
    )
    plt.xlabel("Year")
    plt.ylabel(label)
    plt.legend()
    plt.show()


def world_leaders(df, label, country_list):
    """Plot the giving label for each continent.

    Args:
        df (dataframe): dataframe containing our data.
        label (string): The target label.
        country_list (list): List of countries to plot.

    Returns:
        None
    """
    for c in country_list:
        plt.plot(
            YEARS,
            df[df["Country"] == c][label],
            label=c,
        )

    plt.xlabel("Year")
    plt.ylabel(label)
    plt.legend()
    plt.show()


def pop_show(df):
    """Plot the population of each country.

    Args:
        df (dataframe): dataframe containing our data.

    Returns:
        None
    """
    countries_name = df["Country"].unique()
    above_100 = below_100 = 0
    for c in countries_name:
        if (
            float(df[(df["Country"] == c) & (df["Year"] == 2020)]["Population Total"])
            > 0.1
        ):
            above_100 += 1
        else:
            below_100 += 1

    plt.pie([above_100, below_100], labels=["Above", "Below"])
    plt.show()


def Cont_expectancy(df, cont):
    """Plot continent life expectancy per year

    Args:
        df (dataframe): Dataframe containing our data.
        cont (string): The target continent.

    Returns:
        None
    """
    ocan_list = df[df["Continent"] == cont]["Country"].unique()

    for indx, c in enumerate(ocan_list):
        plt.plot(
            YEARS,
            df[df["Country"] == c]["Life expectancy at birth"],
            label=c,
        )
        if indx % 5 == 0:
            plt.xlabel("Year")
            plt.ylabel("Life expectancy")
            plt.legend()
            plt.show()
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")
    plt.legend()
    plt.show()


def Ussr(df, label):
    """plot Ussr data using the list declared above.

    Args:
        df (dataframe): Dataframe containing our data.
        label (string): The target label.

    Returns:
        None
    """
    country_list = df[df["Country"].isin(USSR_list)]["Country"].unique()
    for c in country_list:
        plt.plot(
            YEARS,
            df[df["Country"] == c][label],
            label=c,
        )

    plt.xlabel("Year")
    plt.ylabel(label)
    plt.legend()
    plt.show()


def Genocide(df, label):
    """Plotting countries from the Genocide list.

    Args:
        df (DataFrame): Dataframe containing our data.
        label (string): The target label.

    Returns:
        None
    """
    country_list = df[df["Country"].isin(GENOCIDE_list)]["Country"].unique()
    for i, c in enumerate(country_list):
        plt.plot(
            YEARS,
            df[df["Country"] == c][label],
            label=c,
        )
        if i % 5 == 0:
            plt.xlabel("Year")
            plt.ylabel(label)
            plt.legend()
            plt.show()

    plt.xlabel("Year")
    plt.ylabel(label)
    plt.legend()
    plt.show()


def comp(df_full, df_scrap):
    """Function to compare columns from df_full and df_scrape and create correlations between them
    Args:
        df_full (Data Frame): Data Frame with the csv data
        df_scrap (Data Frame): Data Frame with the scraping data
    Returns:
        None (*Optionally Opens the CSV)
    """
    # Create lists of columns to go compare between
    col_full = list(
        df_full.columns[
            (df_full.columns != "Country")
            & (df_full.columns != "Year")
            & (df_full.columns != "Continent")
        ]
    )

    col_scrap = list(
        df_scrap.columns[
            (df_scrap.columns != "Country")
            & (df_scrap.columns != "Year")
            & (df_scrap.columns != "Continent")
        ]
    )

    for i in col_full:
        for j in col_scrap:

            # Get countries from df_scrap
            countries_scrap = df_scrap["Country"].unique()

            # Get countries from df_full that are also in df_scrap
            ser1_countries = df_full[
                (df_full["Year"] >= 2009)
                & (df_full["Year"] <= 2020)
                & (df_full["Country"].isin(countries_scrap))
            ]["Country"]

            # Create Data Frame out of df_full with column i
            ser1 = df_full[
                (df_full["Year"] >= 2009)
                & (df_full["Year"] <= 2020)
                & (df_full["Country"].isin(countries_scrap))
            ][i]

            # Create Data Frame out of df_scrap with column j
            ser2 = df_scrap[
                (df_scrap["Year"] >= 2009)
                & (df_scrap["Year"] <= 2020)
                & (df_scrap["Country"].isin(ser1_countries.unique()))
            ][j]

            # Create dictionary with details about the new Data Frame
            details = {
                "Country": list(ser1_countries.values),
                i: list(ser1.values),
                j: list(ser2.values),
            }

            # Create Data Frame with selected data,create correlations and create scatter plot
            new_df = pd.DataFrame(details)
            Correlations(new_df)


df_full = pd.read_csv(FULL_DB_PATH)
df_scrap = pd.read_csv(SCRAP_DB_PATH)

labels = df_full.columns

# > Driver Code for the functions above:

# comp(df_full, df_scrap)
# Correlations(df_full)
# Correlations(df_scrap)


# Edu rank (1990+) | Total Consumption | GDP total | Life Expectancy | Population total |
# USA Russ China code:
# for label in labels:
#     USA_RUSS_CHINA(df_full,label)

# Continent mean values:
# TODO - this for loop starts automatically, maybe move to function?
# for label in labels:
#     if label in [
#         "Country",
#         "Year",
#         "Continent",
#         "GDP Growth",
#         "Government expenditure (% of GDP)",
#         "Total government Expenses (% of GDP)",
#         "Military expenditure (% of GDP)",
#         "Population Growth pace",
#     ]:
#         continue
#     Continent_VS(df_full, label)

# LIFE expectancy
# Cont_expectancy(df_full, "Europe")

# USSR | Genocide
# for label in labels:
#     if label in [
#         "Country",
#         "Education Ranking",
#         "Year",
#         "Continent",
#         "Government expenditure (% of GDP)",
#         "Total government Expenses (% of GDP)",
#         "Total consumption ($)",
#         "Least Developed Country",
#         "Third World",
#     ]:
#         continue
#     #Ussr(df_full, label)
#     Genocide(df_full, label)

## Pop show
# pop_show(df_full)

# leaders_list = [
#     "United States",
#     "Russia",
#     "United Kingdom",
#     "Germany",
#     "China",
#     "Israel",
# ]
# world leaders
# for label in labels:
#     if label in [
#         "Country",
#         "Year",
#         "Continent",
#         "Government expenditure (% of GDP)",
#         "Total government Expenses (% of GDP)",
#         "Total consumption ($)",
#         "Least Developed Country",
#         "Third World",
#     ]:
#         continue
#     world_leaders(df_full, label, leaders_list)


##
if __name__ == "__main__":
    Correlations(df_full)
    pass
