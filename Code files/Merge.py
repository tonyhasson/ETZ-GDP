from imports import *


CSV_FILES = [
    "Education RankingREFORMAT",
    "Final consumption expenditureREFORMAT",
    "GDP GrowthREFORMAT",
    "GDP TotalREFORMAT",
    "Government ExpenditureREFORMAT",
    "Government Expense(of total GDP)REFORMAT",
    "Life expectancy at birthREFORMAT",
    "Population Growth paceREFORMAT",
    "Population TotalREFORMAT",
    "Military Expenditure totalREFORMAT",
    "Military Expenditure(% of GDP)REFORMAT",
    "df_Continent",
]
SCRAP_CSV_FILES = [
    "High Tech Exports(% of total)REFORMAT",
    "High Tech Exports(total)REFORMAT",
    "Scraping CSV\df2",
    "Scraping CSV\df3",
    "Scraping CSV\df4",
    "df_Continent",
]
List_Of_Countries = [
    "Republic of the Congo",
    "Democratic Republic of the Congo",
    "Afghanistan",
    "Albania",
    "Algeria",
    "Andorra",
    "Angola",
    "Antigua and Barbuda",
    "Aruba",
    "Argentina",
    "Armenia",
    "Australia",
    "Austria",
    "Azerbaijan",
    "Bahrain",
    "Bangladesh",
    "Barbados",
    "Belarus",
    "Belgium",
    "Belize",
    "Benin",
    "Bhutan",
    "Bolivia",
    "Bosnia and Herzegovina",
    "Botswana",
    "Brazil",
    "Bulgaria",
    "Burkina Faso",
    "Burundi",
    "Ivory Coast",
    r"Cote d'Ivoire",
    "Cabo Verde",
    "Cambodia",
    "Cameroon",
    "Canada",
    "Central African Republic",
    "Chad",
    "Chile",
    "China",
    "Colombia",
    "Comoros",
    "Congo",
    "Costa Rica",
    "Croatia",
    "Cuba",
    "Cyprus",
    "Czech Republic",
    "Democratic Republic of the Congo",
    "Denmark",
    "Djibouti",
    "Dominica",
    "Dominican Republic",
    "Ecuador",
    "Egypt",
    "El Salvador",
    "Equatorial Guinea",
    "Eritrea",
    "Estonia",
    "Eswatini",
    "Ethiopia",
    "Fiji",
    "Finland",
    "France",
    "Gabon",
    "Georgia",
    "Germany",
    "Ghana",
    "Greece",
    "Grenada",
    "Guatemala",
    "Guinea",
    "Guinea-Bissau",
    "Guyana",
    "Haiti",
    "Holy See",
    "Honduras",
    "Hungary",
    "Iceland",
    "India",
    "Indonesia",
    "Iran",
    "Iraq",
    "Ireland",
    "Israel",
    "Italy",
    "Jamaica",
    "Japan",
    "Jordan",
    "Kazakhstan",
    "Kenya",
    "Kiribati",
    "Kuwait",
    "Laos",
    "Latvia",
    "Lebanon",
    "Lesotho",
    "Liberia",
    "Libya",
    "Liechtenstein",
    "Lithuania",
    "Luxembourg",
    "Madagascar",
    "Malawi",
    "Malaysia",
    "Maldives",
    "Mali",
    "Malta",
    "Marshall Islands",
    "Mauritania",
    "Mauritius",
    "Mexico",
    "Micronesia",
    ",Moldova",
    "Monaco",
    "Mongolia",
    "Montenegro",
    "Morocco",
    "Mozambique",
    "Myanmar",
    "Namibia",
    "Nauru",
    "Nepal",
    "Netherlands",
    "New Zealand",
    "Nicaragua,",
    "Niger",
    "Nigeria",
    "North Macedonia",
    "Norway",
    "Oman",
    "Pakistan",
    "Palau",
    "Palestine State",
    "Panama",
    "Papua New Guinea",
    "Paraguay",
    "Peru",
    "Philippines",
    "Poland",
    "Portugal",
    "Qatar",
    "Romania",
    "Russia",
    "Rwanda",
    "Samoa,",
    "San Marino",
    "Sao Tome and Principe",
    "Saudi Arabia",
    "Senegal",
    "Serbia",
    "Seychelles",
    "Sierra Leone",
    "Singapore",
    "Slovakia",
    "Slovenia",
    "Solomon Islands",
    "Somalia",
    "South Africa",
    "South Korea",
    "South Sudan",
    "Spain",
    "Sri Lanka",
    "Sudan",
    "Suriname",
    "Sweden",
    "Switzerland",
    "Syria",
    "Tajik,istan",
    "Tanza,nia",
    "Thailand",
    "Timor-Leste",
    "Togo",
    "Tonga",
    "Trinidad and Tobago",
    "Tunisia",
    "Turkey",
    "Turkmenistan",
    "Tuvalu",
    "Uganda",
    "Ukraine",
    "United Arab Emirates",
    "United Kingdom",
    "United States",
    "Uruguay",
    "Uzbekistan",
    "Vanuatu",
    "Venezuela",
    "Vietnam",
    "Yemen",
    "Zambia",
    "Zimbabwe",
]


def merge_third_world(df):
    """Function To merge {0 if not in third world else 1} to df

    Args:
        df (DataFrame): DataFrame to be merged
    Returns:
        df with another columns of third world
    """

    df_third = pd.read_csv(r"..\CSV files\Scraping CSV\third_world_countries.csv")
    arr_c = [c for c in df_third["Country"]]
    df["Third World"] = 0
    for c in arr_c:
        df.loc[df["Country"] == c, "Third World"] = 1
    return df


def reformatCSV(CSV_location, CSV_name, Start_year, End_year):
    """Function to reformat existing dataframe to [Country, Year, Value] format.

    Args:
        CSV_location (string): The path for the CSV file.
        CSV_name (string): The Name for the CSV file.
        Start_year (int): year to start format from.
        End_year (int): year to end format at.
    """
    columns = ["Country", "Year", CSV_name]
    df = pd.read_csv(CSV_location + r"\\" + CSV_name + ".csv")
    newrow = []
    for row in df.iterrows():
        for i in range(Start_year, End_year + 1):
            newrow.append([row[1]["Country"].lstrip(), i, row[1][str(i)]])

    reformated = pd.DataFrame(newrow, columns=columns)
    reformated.to_csv(r"..\CSV files\\" + CSV_name + "REFORMAT.csv", index=False)


def weird_names(arr_df):
    """Function to correct to names of countries

    Args:
        arr_df (list): list of dataframes to be corrected
    """
    for DataFrameIterator in arr_df:
        DataFrameIterator.loc[
            DataFrameIterator["Country"] == "Cote d'Ivoire", "Country"
        ] = "Ivory Coast"
        DataFrameIterator.loc[
            DataFrameIterator["Country"] == "Slovak Republic", "Country"
        ] = "Slovakia"
        DataFrameIterator.loc[
            DataFrameIterator["Country"] == "Yemen, Rep.", "Country"
        ] = "Yemen"
        DataFrameIterator.loc[
            DataFrameIterator["Country"] == "Egypt, Arab Rep.", "Country"
        ] = "Egypt"
        DataFrameIterator.loc[
            DataFrameIterator["Country"] == "Korea, Dem. Rep.", "Country"
        ] = "North Korea"
        DataFrameIterator.loc[
            DataFrameIterator["Country"] == "Korea, Dem. People's Rep.", "Country"
        ] = "North Korea"
        DataFrameIterator.loc[
            DataFrameIterator["Country"] == "Korea, Rep.", "Country"
        ] = "South Korea"
        DataFrameIterator.loc[
            DataFrameIterator["Country"] == "North Macedonia", "Country"
        ] = "Macedonia"
        DataFrameIterator.loc[
            DataFrameIterator["Country"] == "Russian Federation", "Country"
        ] = "Russia"
        DataFrameIterator.loc[
            DataFrameIterator["Country"] == "Syrian Arab Republic", "Country"
        ] = "Syria"
        DataFrameIterator.loc[
            DataFrameIterator["Country"] == "Congo", "Country"
        ] = "Republic of the Congo"
        DataFrameIterator.loc[
            DataFrameIterator["Country"] == "Congo, Dem. Rep.", "Country"
        ] = "Democratic Republic of the Congo"
        DataFrameIterator.loc[
            DataFrameIterator["Country"] == "Congo, Rep.", "Country"
        ] = "Republic of the Congo"
        DataFrameIterator.loc[
            DataFrameIterator["Country"] == "Venezuela, RB", "Country"
        ] = "Venezuela"
        DataFrameIterator.loc[
            DataFrameIterator["Country"] == "Bolivia (Plurinational State of)",
            "Country",
        ] = "Bolivia"
        DataFrameIterator.loc[
            DataFrameIterator["Country"] == "Congo (Democratic Republic of the)",
            "Country",
        ] = "Democratic Republic of the Congo"
        DataFrameIterator.loc[
            DataFrameIterator["Country"] == "C׳₪te d'Ivoire", "Country"
        ] = "Ivory Coast"
        DataFrameIterator.loc[
            DataFrameIterator["Country"] == "Eswatini (Kingdom of)", "Country"
        ] = "Eswatini"
        DataFrameIterator.loc[
            DataFrameIterator["Country"] == "Hong Kong, China (SAR)", "Country"
        ] = "Hong Kong"
        DataFrameIterator.loc[
            DataFrameIterator["Country"] == "Hong Kong SAR, China", "Country"
        ] = "Hong Kong"
        DataFrameIterator.loc[
            DataFrameIterator["Country"] == "Iran (Islamic Republic of)", "Country"
        ] = "Iran"
        DataFrameIterator.loc[
            DataFrameIterator["Country"] == "Iran, Islamic Rep.", "Country"
        ] = "Iran"
        DataFrameIterator.loc[
            DataFrameIterator["Country"] == "Korea (Republic of)", "Country"
        ] = "South Korea"
        DataFrameIterator.loc[
            DataFrameIterator["Country"] == "Lao People's Democratic Republic",
            "Country",
        ] = "Laos"
        DataFrameIterator.loc[
            DataFrameIterator["Country"] == "Lao PDR", "Country"
        ] = "Laos"
        DataFrameIterator.loc[
            DataFrameIterator["Country"] == "Micronesia (Federated States of)",
            "Country",
        ] = "Micronesia"
        DataFrameIterator.loc[
            DataFrameIterator["Country"] == "Moldova (Republic of)", "Country"
        ] = "Moldova"
        DataFrameIterator.loc[
            DataFrameIterator["Country"] == "Tanzania (United Republic of)", "Country"
        ] = "Tanazania"
        DataFrameIterator.loc[
            DataFrameIterator["Country"] == "Viet Nam", "Country"
        ] = "Vietnam"
        DataFrameIterator.loc[
            DataFrameIterator["Country"] == "Egypt, Arab Rep.", "Country"
        ] = "Egypt"
        DataFrameIterator.loc[
            DataFrameIterator["Country"] == "Czechia", "Country"
        ] = "Czech Republic"
        DataFrameIterator.loc[
            DataFrameIterator["Country"] == "Micronesia, Fed. Sts.", "Country"
        ] = "Micronesia"


def merge_and_clean(arr_df, Name):
    """Merge all dataframes into one and clean it a bit.

    Args:
        Name (string): The name of the dataframe.
        arr_df (array): array of dataframes to manipulate.add()

    Returns:
        Dataframe: Merged dataframe of all the dataframes from the given array.
    """
    ## change name of weird countries
    weird_names(arr_df)

    ## merge
    for i in range(len(arr_df) - 1):
        if i < len(arr_df) - 2:
            arr_df[i + 1] = arr_df[i].merge(
                arr_df[i + 1], on=["Year", "Country"], how="outer"
            )
        else:  ##merge with the Continent CSV
            arr_df[i + 1] = arr_df[i].merge(arr_df[i + 1], on=["Country"], how="outer")

    # Assign the last position of arr_df to df (the merged dataframe)
    df = arr_df[len(arr_df) - 1]

    # Sort The DF (for the sake of the visualization)
    df.sort_values(["Country", "Year"], axis=0, ascending=True, inplace=True)

    ## Add third world column to df
    df = merge_third_world(df)

    ## remove all unknown and irrelevant countries
    df = df[df["Country"].isin(List_Of_Countries)]

    # Keep only the relevant data according to DF
    if Name == "df_scrape":

        # Keep year 2009 onward
        df = df[df["Year"] >= 2009]

        # load df to take countries from
        SCRAP_Countries = pd.read_csv("..\CSV files\Scraping CSV\df3.csv")

        # Keep only the countries that are in the df
        df = df[df["Country"].isin(SCRAP_Countries["Country"].unique())]

    # Nirmul Arahim High & Change Columns names for full database
    else:

        df = df[df["Year"] >= 1960]
        df["Final consumption expenditure"] = (
            df["Final consumption expenditure"] / 1000000
        )
        df["GDP Total"] = df["GDP Total"] / 1000000
        df["Population Total"] = df["Population Total"] / 1000000
        df[
            "Military expenditure (1914-2007, real prices) (Correlates of War: National Material Capabilities (v4.0))"
        ] = (
            df[
                "Military expenditure (1914-2007, real prices) (Correlates of War: National Material Capabilities (v4.0))"
            ]
            / 1000000
        )
        df = df.rename(
            columns={
                "Final consumption expenditure": "Total consumption ($)",
                "Government Expenditure (IMF based on Mauro et al. (2015))": "Government expenditure (% of GDP)",
                "Military expenditure (1914-2007, real prices) (Correlates of War: National Material Capabilities (v4.0))": "Military Spendings ($)",
                "Expense (% of GDP)": "Total government Expenses (% of GDP)",
            }
        )
    df.to_csv(r"..\CSV files\\" + Name + ".csv", index=False)
    return df


def arr_df_builder(CSV_FILES):
    """Function to build Array of dataframes from CSV files.

    Returns:
        DataFrame Array: array of dataframes to be manipulated in the future.
    """
    path = os.path.dirname(__file__)
    arr_df = []

    for i in range(len(CSV_FILES)):
        text = r"..\CSV files\\"
        text += CSV_FILES[i]
        text += ".csv"
        arr_df.append(pd.read_csv(os.path.join(path, text)))
    return arr_df


# reformatCSV(r"..\CSV files\OLD","Education Ranking",1990,2019)
# reformatCSV(r"..\CSV files\OLD","GDP Growth",1960,2020)
# reformatCSV(r"..\CSV files\OLD","GDP Total",1960,2020)
# reformatCSV(r"..\CSV files\OLD","Life expectancy at birth",1960,2020)
# reformatCSV(r"..\CSV files\OLD","High Tech Exports(% of total)",2007,2020)
# reformatCSV(r"..\CSV files\OLD","High Tech Exports(total)",2007,2020)
# reformatCSV(r"..\CSV files\OLD","Final consumption expenditure",1960,2020)
# reformatCSV(r"..\CSV files\OLD","Population Growth pace",1960,2020)
# reformatCSV(r"..\CSV files\OLD","Population Total",1960,2002)


def Run():
    arr_df = arr_df_builder(CSV_FILES)
    scrap_arr_df = arr_df_builder(SCRAP_CSV_FILES)
    DF_FULL = merge_and_clean(arr_df, "df_Full_DataBase")
    DF_SCRAPE = merge_and_clean(scrap_arr_df, "df_scrape")
    return DF_FULL, DF_SCRAPE
