from imports import *

# https://stackoverflow.com/questions/5815747/beautifulsoup-getting-href
# https://realpython.com/beautiful-soup-web-scraper-python/
# https://www.dataquest.io/blog/web-scraping-tutorial-python/
# https://www.askpython.com/python/string/remove-character-from-string-python


def load_soup_object():
    """load soup object from hardcoded url.
    Args:
        None
    Returns:
        soup: soup object for the hardcoded url.
    """
    url = "https://en.wikipedia.org/w/index.php?title=List_of_countries_by_continent&oldid=251930515"
    resp = requests.get(url)
    soup = bs4.BeautifulSoup(resp.text, "html.parser")

    return soup


def beautiful_data(country):
    """function to make the data better and more relevant.

    Args:
        country (string): giving dirty country string.

    Returns:
        string: clean country name.
    """
    country_name, sep, capital = country.partition(" – ")
    country_name = country_name.replace("\xa0", "")
    country_name = country_name.replace("[", "")
    country_name = country_name.replace("]", "")
    if country_name[0] == " ":
        country_name = country_name.replace(" ", "", 1)
    if country_name[-1] == " ":
        country_name = country_name[0 : len(country_name) - 2]
    country_name = re.sub("[0-9]", "", country_name)
    country_name = country_name.split(", ")
    country_name[0] = country_name[0].split(" (")

    return country_name[0][0]


def scrap_country():
    """scrapper that gets each continent's country names.

    Args:
        None

    Returns:
        dictionary: dict containing country names and their corresponding continent.
    """
    continents = []
    name_dict = {}

    soup = load_soup_object()
    continents_items = soup.find_all(class_="mw-headline")

    # Getting the continent Name
    for cnt, item in enumerate(continents_items):
        continents.append(item.get_text().strip())
        if cnt == 8:
            break  # Wiki start giving info we don't need after that

    # remove irrelevant data - not real continents or not helpful for us.
    continents.remove("Eurasia")
    continents.remove("Americas")

    ul_list = soup.find_all("ul")

    append_cnt = 0
    for cnt, i in enumerate(ul_list):  # Getting the countries List
        if cnt >= 14:
            countries_list = []  # new list for each continent
            name = i.get_text().splitlines()
            for country in name:  # each country in continents
                country_name_to_enter = beautiful_data(country)
                if country_name_to_enter not in countries_list:
                    countries_list.append(country_name_to_enter)
            if append_cnt == 7:
                break  # stops the loop when finished looping through the continents
            name_dict[continents[append_cnt]] = countries_list
            append_cnt += 1

    return name_dict


scrap_country()
