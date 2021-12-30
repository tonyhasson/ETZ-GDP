from imports import *

def load_soup_object():
    """load soup object from hardcoded url.

    Returns:
        soup: soup object for the hardcoded url.
    """
    url = "https://www.burningcompass.com/countries/third-world-countries.html"
    resp = requests.get(url)
    soup = bs4.BeautifulSoup(resp.text, 'html.parser')

    return soup


def scrap_third():
    """scrapper that gets all third world countries.

    Returns:
        list: list containing country names.
    """
    names = []
    
    soup = load_soup_object()
    table_items = soup.find("tbody")    
    
    for row in table_items:
        if row != '\n' and row != '':
            for indx,col in enumerate(row):
                if row != '\n' and row != '':
                    country_name = col
                    if indx == 1:
                        break
            if country_name != '' and country_name != '\n' and country_name != None:
                names.append(country_name.text)
                
    return names
    
country_list = scrap_third()

third_world_countries = pd.DataFrame(country_list,columns=['Country'])
Name = "third_world_countries"
third_world_countries.to_csv(r"..\CSV files\\"+ Name +".csv")