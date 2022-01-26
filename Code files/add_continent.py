from Country_continent import *


arr_countries = scrap_country()


def return_cont(country_name):
    """Extract country's continent name from list

    Args:
        country_name (list): list of country names

    Returns:
        String: Country's continent name
    """
    key_list = list(arr_countries.keys())
    val_list = list(arr_countries.values())

    for i in range(len(val_list)):
        try:
            position = val_list[i].index(country_name)
            return key_list[i]
        except:
            continue

    return None


df_test = pd.read_csv(r"..\CSV files\df_test.csv")
country_list = [c for c in df_test["Country"].unique()]
continent_list = map(return_cont, country_list)
continent_list = list(continent_list)

new_df = pd.DataFrame(
    data={"Country": country_list, "Continent": continent_list},
    columns=["Country", "Continent"],
)

new_df.to_csv(r"..\CSV files\df_Continent.csv")
