from imports import *

FULL_DB_PATH = r"../CSV files/df_Full_DataBase.csv"
SCRAP_DB_PATH = r"../CSV files/df_scrape.csv"
YEARS = [i for i in range(1960, 2021)]

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

GENOCIDE_list = [
    "Democratic Republic of the Congo",
    "Vietnam",
    "Nigeria",
    "Sudan",
    "Afghanistan",
    "Timor-Leste",
    "Ethiopia",
    "Eritrea",
    "Bangladesh",
    "Angola",
    "Iraq",
    "Yemen",
    "Uganda",
    "Lebanon",
    "Sierra Leone",
    "Cambodia",
    "Guatemala",
    "Myanmar",
    "Bosnia and Herzegovina",
]


# function to print plot 2 columns
def Plot(df, col1, col2, data_title):
    plt.scatter(df[col1], df[col2])
    plt.xlabel(col1)
    plt.ylabel(col2)
    plt.title("Correlations: %f" % data_title)
    plt.show()


# function to check which columns are correlated
def Correlations(df):
    # df.drop(["Country", "Year", "Continent"], axis=1, inplace=True)
    df.drop("Country", axis=1, inplace=True)
    cols = df.columns
    df_corr = df.corr().values
    for i in range(len(df_corr)):
        for j in range(len(df_corr[i])):
            if (df_corr[i][j] > 0.4 or df_corr[i][j] < -0.3) and i != j:
                Plot(df, cols[i], cols[j], df_corr[i][j])


#  in RUSS_CHINA_USA
# Edu rank (1990+) | Total Consumption | GDP total | Life Expectancy | Population total |
def USA_RUSS_CHINA(df, label):
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

    year_Asia = [
        df[(df["Continent"] == "Asia") & (df["Year"] == i)][label].values.mean()
        for i in range(1960, 2021)
    ]
    year_Africa = [
        df[(df["Continent"] == "Africa") & (df["Year"] == i)][label].values.mean()
        for i in range(1960, 2021)
    ]
    year_Europe = [
        df[(df["Continent"] == "Europe") & (df["Year"] == i)][label].values.mean()
        for i in range(1960, 2021)
    ]
    year_NorthAmerica = [
        df[(df["Continent"] == "North America") & (df["Year"] == i)][
            label
        ].values.mean()
        for i in range(1960, 2021)
    ]
    year_CentAmerica = [
        df[(df["Continent"] == "Central America") & (df["Year"] == i)][
            label
        ].values.mean()
        for i in range(1960, 2021)
    ]
    year_SouthAmerica = [
        df[(df["Continent"] == "South America") & (df["Year"] == i)][
            label
        ].values.mean()
        for i in range(1960, 2021)
    ]
    year_Oceania = [
        df[(df["Continent"] == "Oceania") & (df["Year"] == i)][label].values.mean()
        for i in range(1960, 2021)
    ]

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


# Tarbot bizbuz west VS east
def Big_spender(df):
    # https://stackabuse.com/seaborn-scatter-plot-tutorial-and-examples/
    # EU/ASIA -> minus russia
    WEST = ["Europe", "North America", "Central America", "Oceania"]
    EAST = ["Asia"]
    USELESS = ["Africa", "South America"]
    # grid = sns.FacetGrid(df, col="Continent", hue="Continent", col_wrap=2)
    ## East VS West
    # grid.map(
    #     sns.scatterplot,
    #     df[(df["Continent"] in  WEST) & (df["Government expenditure (% of GDP)"].mean())],
    #     df[(df["Continent"] ==  "Asia") & (df["Government expenditure (% of GDP)"].mean())],
    # )
    ## Year VS Population
    # grid.map(
    #     sns.scatterplot,
    #     "Year",
    #     "Population Total",
    # )
    ## Year VS Government expenses
    # grid.map(
    #     sns.scatterplot,
    #     "Year", # X
    #     "Government expenditure (% of GDP)",   # Y
    # )
    # grid.add_legend()
    # ocan_list = df[df["Continent"] == "Oceania"]["Country"].unique()


def world_leaders(df, label, country_list):
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
           None (Open CSV in Excel)
       """



    ##create lists of columns to go compare between

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

            ##get countries from df_scrap
            countries_scrap = df_scrap["Country"].unique()



            ##get countries from df_full that are also in df_scrap
            ser1_countries = df_full[
                (df_full["Year"] >= 2009)
                & (df_full["Year"] <= 2020)
                & (df_full["Country"].isin(countries_scrap))
            ]["Country"]

            ##create Data Frame out of df_full with column i
            ser1 = df_full[
                (df_full["Year"] >= 2009)
                & (df_full["Year"] <= 2020)
                & (df_full["Country"].isin(countries_scrap))
            ][i]

            ##create Data Frame out of df_scrap with column j
            ser2 = df_scrap[
                (df_scrap["Year"] >= 2009)
                & (df_scrap["Year"] <= 2020)
                & (df_scrap["Country"].isin(ser1_countries.unique()))
            ][j]

            ##create dictionary with details about the new Data Frame
            details = {
                "Country": list(ser1_countries.values),
                i: list(ser1.values),
                j: list(ser2.values),
            }

            ##create Data Frame with selected data,create correlations and create scatter plot
            new_df = pd.DataFrame(details)
            Correlations(new_df)



df_full = pd.read_csv(FULL_DB_PATH)
df_scrap = pd.read_csv(SCRAP_DB_PATH)

labels = df_full.columns

comp(df_full, df_scrap)


## USA Russ China code:
# for label in labels:
#     USA_RUSS_CHINA(df_full,label

## Continent mean values:
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

## LIFE expectancy
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


## TODO: Comparison between strong contries and WEST vs EAST
