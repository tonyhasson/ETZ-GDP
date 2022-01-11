from imports import *

FULL_DB_PATH = r"../CSV files/df_Full_DataBase.csv"
SCRAP_DB_PATH = r"../CSV files/df_scrape.csv"
YEARS = [i for i in range(1960, 2021)]

# function to print plot 2 columns
def Plot(df, col1, col2):
    plt.scatter(df[col1], df[col2])
    plt.xlabel(col1)
    plt.ylabel(col2)
    plt.show()


# function to check which columns are correlated
def Correlations(df):
    df.drop(["Country", "Year", "Continent"], axis=1, inplace=True)
    cols = df.columns
    df_corr = df.corr().values
    for i in range(len(df_corr)):
        for j in range(len(df_corr[i])):
            if (df_corr[i][j] > 0.4 or df_corr[i][j] < -0.3) and i != j:
                Plot(df, cols[i], cols[j])


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
    year_Europe = [
        df[(df["Continent"] == "Europe") & (df["Year"] == i)][label].values.mean()
        for i in range(1960, 2021)
    ]
    year_Africa = [
        df[(df["Continent"] == "Africa") & (df["Year"] == i)][label].values.mean()
        for i in range(1960, 2021)
    ]
    year_SouthAmerica = [
        df[(df["Continent"] == "South America") & (df["Year"] == i)][
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
    year_NorthAmerica = [
        df[(df["Continent"] == "North America") & (df["Year"] == i)][
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
        year_Europe,
        label="Europe",
    )
    plt.plot(
        YEARS,
        year_Africa,
        label="Africa",
    )
    plt.plot(
        YEARS,
        year_SouthAmerica,
        label="South America",
    )
    plt.plot(
        YEARS,
        year_CentAmerica,
        label="Central America",
    )
    plt.plot(
        YEARS,
        year_NorthAmerica,
        label="North America",
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
    WEST = ["Europe", "North America", "South America"]
    EAST = ["Asia", "Oceania"]
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
    plt.legend()
    plt.show()


df_full = pd.read_csv(FULL_DB_PATH)
df_scrap = pd.read_csv(SCRAP_DB_PATH)

labels = df_full.columns
## USA Russ China code:
# for label in labels:
#     USA_RUSS_CHINA(df_full,label

# Continent mean values:
for label in labels:
    if label in [
        "Country",
        "Year",
        "Continent",
        "GDP Growth",
        "Government expenditure (% of GDP)",
        "Total government Expenses (% of GDP)",
        "Military expenditure (% of GDP)",
        "Population Growth pace",
    ]:
        continue
    Continent_VS(df_full, label)

## LIFE expectancy
# Cont_expectancy(df_full, "Asia")

## TODO: Spikes in aaaaaa asia and oceania
## TODO: Idea: show country at war in years | Genocide
## TODO: Comparison between strong contries and WEST vs EAST
## ! life expectancy does problems in and north america (Israel got 3 years fucked upp)
## !North america is Shady with the numbers, must check her
