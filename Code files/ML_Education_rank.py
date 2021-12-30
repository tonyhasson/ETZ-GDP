from imports import *
from subprocess import Popen

def load_dataset(df, label_column):
    """Loading the data set and return the Traning features and target for the model.

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

    return X,y


def linear_regres(arr_year_data,dataset,label_column):
    """Linear Regression for training.

    Args:
        arr_year_data (string):  years we got data.
        dataset (Dataset): the dataset for the training.
        label_column (string): The Target column for the regression model.

    Returns:
        arr_data: Array with new data used by the regression model.
    """
    arr_year=[]
    dataset =dataset[['Year', label_column]]
    X,y=load_dataset(dataset[(dataset['Year']>=min(arr_year_data)) & (dataset['Year']<=max(arr_year_data))],label_column)
    m=linear_model.LinearRegression().fit(X.values,y)
    arr_data=[]
    for year in range(1960,2021):
        if year not in arr_year_data:
            arr_year.append([year])

    #arr_year = [[year] for year in range(1960, min(arr_year_data))]

    #if (label_column == "Education Ranking"):
        #arr_year.append([2020])

    #check if every number in y <0



    #if label_column=='Final consumption expenditure' or 'GDP Total' or 'Military expenditure (1914-2007, real prices) (Correlates of War: National Material Capabilities (v4.0))':
    #    arr_data.append(np.minimum(sys.maxsize, np.maximum(0., m.predict(arr_year))))
    #else:
    #    arr_data.append(m.predict(arr_year))
    arr_data.append(m.predict(arr_year))


    return arr_data

def check_year_lr(dataframe, country,label_col):
    """Checking for the first year we got data from.

    Args:
        dataframe ([type]): the main dataframe.
        country (String): the current country to check.

    Returns:
        year: the corresponding year
    """

    # for year in range(1990,2020):
    #     data_year_country = dataframe[(dataframe["Year"] == year) & (dataframe["Country"] == country)]["Education Ranking"].values
    #
    #     if data_year_country[0]!=0:
    #         return year

    arr_year=[]
    for year in range(1960,2021):
        data_year_country = dataframe[(dataframe["Year"] == year) & (dataframe["Country"] == country)][label_col].values
        if data_year_country[0] != 0:
             arr_year.append(year)
    return arr_year


def find_and_regres(dataset):

    dataset_columns =list(dataset.columns)
    columns_to_remove=["Country","Year","Continent"]

    dataset_columns =[c for c in dataset_columns if c not in columns_to_remove]
    for label_column in dataset_columns:

        print(label_column)
        NO_INFO_countries = []
        dataset[label_column].fillna(0, inplace=True)
        for country in dataset.Country.unique():

            try:
                # data_year_country=dataset[(dataset["Year"]==2019) & (dataset["Country"]==country)][label_column]
                Dataframe = list(dataset[(dataset["Country"]==country)][label_column])
                if all(x == 0 for x in Dataframe):
                    NO_INFO_countries.append(country)
                elif 0 in Dataframe:
                    arr_year = check_year_lr(dataset,country,label_column)
                    first_year=min(arr_year)

                    arr_data=linear_regres(arr_year,dataset[dataset['Country']==country],label_column)
                    arr_data=list(arr_data[0])
                    for i in range(len(arr_data)):
                        if arr_data[i] < 0:
                            arr_data[i] = 0

                    arr_final_data = []
                    indx = 0
                    # year_2020 = arr_data.pop() # store the last year values
                    for i in range(1960, 2021):
                        if i in arr_year:
                            arr_final_data.append(0)
                        else:
                            arr_final_data.append(arr_data[indx])
                            indx += 1

                    arr_data = arr_final_data
                    #arr_data.append(float(year_2020))

                    dataset.loc[(dataset['Country']==country) & (dataset['Year']>=1960) & (dataset['Year']<=2020),label_column]+=arr_data

                else:
                    continue


            except Exception as e:
                dataset.loc[(dataset['Country'] == country) & (dataset['Year'] >= 1960) & (dataset['Year'] <= 2020), label_column] = sys.maxsize#Explain pls
                print(e, country)
                NO_INFO_countries.append(country)

    # Fill in countries with no information with the minimum value for that year
        if label_column=="Education Ranking":
            for country in NO_INFO_countries:
                for year in range(1960, 2021):
                    dataset.loc[(dataset['Country'] == country) & (dataset['Year'] == year), label_column] = min(i for i in dataset[(dataset['Year'] == year)][label_column] if i > 0)

    # If Military expenditure
        if label_column == "Military Expenditure":
            pass
    # If GDP Total
        if label_column == "GDP Total":
            pass
    # If GDP Growth
        if label_column == "GDP Growth":
            pass

    dataset.to_csv(r"../CSV files/df_Full_DataBase.csv", index=False)
    Popen("../CSV files/df_Full_DataBase.csv",shell=True)


def Run():
    df=pd.read_csv(r"../CSV files/df_Full_DataBase.csv")
    find_and_regres(df)