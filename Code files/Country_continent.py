from imports import *

 #https://stackoverflow.com/questions/5815747/beautifulsoup-getting-href
 #https://realpython.com/beautiful-soup-web-scraper-python/
 #https://www.dataquest.io/blog/web-scraping-tutorial-python/

def load_soup_object():
    
    url = "https://en.wikipedia.org/w/index.php?title=List_of_countries_by_continent&oldid=251930515"
    resp = requests.get(url)
    soup = bs4.BeautifulSoup(resp.text, 'html.parser')

    return soup

# < span = class"mw-headline" to get continent # till Antartica 9/35
# <b> <a href> to get country name "title"

def scrap_country():
    continents = []
    countries_list = []
    soup = load_soup_object()
    
    # Getting the continent Name
    continents_items = soup.find_all(class_ = "mw-headline")
    
    for cnt,item in enumerate(continents_items):
        continents.append(item.get_text().strip())
        if cnt == 8: break # Wiki start giving info we don't need after that

    ul_list = soup.find_all("ul")

    for cnt,i in enumerate(ul_list): # Getting the countries List
        if cnt >= 13:
            print (i.get_text()) 
        #countries_list.append(i.get_text().strip())   

   
        
    # Creating DataFrame to return
    
    
scrap_country()