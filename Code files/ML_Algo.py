from imports import *

# Columns that cant be negative
CANT_BE_NEG_FULL = [
    "Education Ranking",
    "GDP Total",
    "Government expenditure (% of GDP)",
    "Total government Expenses (% of GDP)",
    "Total consumption ($)",
    "Life expectancy at birth",
    "Population Total",
    "Military Spendings ($)",
    "Military expenditure (% of GDP)",
]

CANT_BE_NEG_SCRAP = [
    "Health Care Index",
    "High Tech Exports(% of total)",
    "High Tech Exports(total)",
    "Price To Income Ratio",
    "Gross Rental Yield City Centre",
    "Gross Rental Yield Outside of Centre",
    "Price To Rent Ratio City Centre",
    "Price To Rent Ratio Outside Of City Centre",
    "Mortgage As A Percentage Of Income",
    "Affordability Index",
    "Cost of Living Index",
    "Rent Index",
    "Groceries Index",
    "Restaurant Price Index",
    "Local Purchasing Power Index",
]


def load_dataset(df, label_column):
    """Loading the data set and return the Training features and target for the model.

    Args:
        df (Pandas DataFrame): Dataset for the features.
        label_column (string): The label to target.

    Returns:
        [type]: TRAINING_FEATURES and TARGET_FEATURES
    """
    TRAINING_FEATURES = df.columns[df.columns != label_column]
    TARGET_FEATURE = label_column

    X = df[TRAINING_FEATURES]
    y = df[TARGET_FEATURE]

    return X, y


def linear_regres(arr_year_data, dataset, label_column, Type):
    """Linear Regression for training.

    Args:
        arr_year_data (string):  years we got data.
        dataset (Dataset): the dataset for the training.
        label_column (string): The Target column for the regression model.

    Returns:
        arr_data: Array with new data used by the regression model.
    """
    # Set The start and last year
    StartYear = 1960
    LastYear = 2021
    if Type == "scrape":  # if we are on scrape dataset change the start and last year
        StartYear = 2009
        LastYear = 2021
    arr_year = []
    dataset = dataset[["Year", label_column]]
    X, y = load_dataset(
        dataset[
            (dataset["Year"] >= min(arr_year_data))
            & (dataset["Year"] <= max(arr_year_data))
        ],
        label_column,
    )
    # Create the linear regression object
    m = linear_model.LinearRegression().fit(X.values, y)
    arr_data = []
    for year in range(StartYear, LastYear + 1):
        if year not in arr_year_data:
            arr_year.append([year])

    arr_data.append(m.predict(arr_year))

    return arr_data


def check_year_lr(dataframe, country, label_col):
    """Check which years we got data from.

    Args:
        dataframe ([type]): the main dataframe.
        country (String): the current country to check.
        label_col(String): the label column to check.
    Returns:
        arr_year: arr containing the year we have data on
    """
    arr_year = []
    StartYear = int((min(dataframe[dataframe["Country"] == country]["Year"])))
    LastYear = int((max(dataframe[dataframe["Country"] == country]["Year"])))
    for year in range(StartYear, LastYear + 1):
        data_year_country = dataframe[
            (dataframe["Year"] == year) & (dataframe["Country"] == country)
        ][label_col].values
        if data_year_country[0] != 0:
            arr_year.append(year)
    return arr_year


def find_and_regres(PATH, Type):
    """Function to replace missing values with the linear regression.
    Args:
        PATH (String): the path to the dataset.(Also the path the save the new dataset)
        Type (String): the type of dataset we are working with.(full or scrape)
    Returns:
        None (Open CSV in Excel)
    """

    if Type == "full":
        CANT_BE_NEG = CANT_BE_NEG_FULL
    elif Type == "scrape":
        CANT_BE_NEG = CANT_BE_NEG_SCRAP

    # Loading the dataset
    dataset = pd.read_csv(PATH)

    dataset_columns = list(dataset.columns)
    columns_to_remove = [
        "Country",
        "Year",
        "Continent",
        "Third World",
        "Least Developed Country",
    ]

    # Getting the relevant columns
    dataset_columns = [c for c in dataset_columns if c not in columns_to_remove]

    for label_column in dataset_columns:
        # Array containing all countries we don't have info on in the column (save for later)
        NO_INFO_countries = []
        dataset[label_column].fillna(0, inplace=True)

        # Progress bar
        pbar_country = tqdm(
            total=len(dataset.Country.unique()),
            smoothing=0.8,
            ncols=120,
            unit=" Operations",
        )

        pbar_country.set_description(f"Processing '{label_column}'")

        for country in dataset.Country.unique():
            # Years To Work on
            StartYear = int((min(dataset[dataset["Country"] == country]["Year"])))
            LastYear = int((max(dataset[dataset["Country"] == country]["Year"])))

            # Progress bar
            pbar_country.update()

            Dataframe = list(dataset[(dataset["Country"] == country)][label_column])

            """3 Possible cases:
            1.We Have Data on all the years
            2.We Have Data on some years
            3.We Don't have any data."""

            # Case: 3
            if all(x == 0 for x in Dataframe):
                NO_INFO_countries.append(country)

            # Case: 2
            elif 0 in Dataframe:
                arr_year = check_year_lr(dataset, country, label_column)

                arr_data = linear_regres(
                    arr_year, dataset[dataset["Country"] == country], label_column, Type
                )
                arr_data = list(arr_data[0])
                if label_column in CANT_BE_NEG:
                    for i in range(len(arr_data)):
                        if arr_data[i] < 0:
                            arr_data[i] = 0

                arr_final_data = []
                indx = 0

                for i in range(StartYear, LastYear + 1):
                    if i in arr_year:
                        arr_final_data.append(0)
                    else:
                        arr_final_data.append(arr_data[indx])
                        indx += 1

                arr_data = arr_final_data

                dataset.loc[
                    (dataset["Country"] == country)
                    & (dataset["Year"] >= StartYear)
                    & (dataset["Year"] <= LastYear),
                    label_column,
                ] += arr_data

            # Case: 1
            else:
                continue

        # Fill in countries with no information with the minimum value for that year (later)
        for country in NO_INFO_countries:
            for year in range(StartYear, LastYear + 1):
                dataset.loc[
                    (dataset["Country"] == country) & (dataset["Year"] == year),
                    label_column,
                ] = min(
                    i for i in dataset[(dataset["Year"] == year)][label_column] if i > 0
                )

        pbar_country.close()

    dataset.to_csv(PATH, index=False)
    # Automated CSV opener for faster validation
    # Popen(PATH, shell=True)


def Run():
    find_and_regres(FULL_DB_PATH, "full")
    find_and_regres(SCRAP_DB_PATH, "scrape")
