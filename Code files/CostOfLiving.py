# DataFrames
import pandas as pd
# Network, Crawlling and Scraping
import requests
import bs4
from bs4 import BeautifulSoup
# # Visualization
# import matplotlib as mpl
# import matplotlib.pyplot as plt
# import seaborn as sns
# General
# import scipy as sc
# import numpy as np
# from collections import Counter
# # ML
# import sklearn
# from sklearn import linear_model, metrics, preprocessing
# from sklearn.preprocessing import StandardScaler, MinMaxScaler
# from sklearn.linear_model import LogisticRegression, LinearRegression
# from sklearn.metrics import r2_score, f1_score

####################
#### Ziv Did it ####
####################

def load_soup_object(year):
    prefix = "https://www.numbeo.com/cost-of-living/rankings_by_country.jsp?title="
    # making the url per year
    url = prefix + year
    resp = requests.get(url)
    soup = bs4.BeautifulSoup(resp.text, 'html.parser')

    return soup


def create_dataframe(page):
    cols = []      
    vals = []  
    table = page.find('table',id='t2')
    # getting table's cols
    for th in table.findAll('th'):
        cols.append(th.text)
    
    for tr in table.findAll('tr'):
        vals.append(tr.get_text().split())

    # removing the cols
    vals.pop(0)
    cols.pop(0)
    
    # fixing the data
    
    #########################################################################
    # If country's name got space inside need to make it one word as split  #
    # func splits it to multiple words                                      #
    #########################################################################
    
    # Creating DataFrame to return
    df = pd.DataFrame(columns=cols)
    for row in vals:
        df.add(row)
    
    return df

if __name__ == "__main__":
    years = [ str(i) for i in range(2009,2021)]
    for year in years:
        soup = load_soup_object(year)
        # Get the table
        table = soup.find("table", attrs={"id": "t2"})
        #print (f"Got: {year}")
        #print(table.thead.text) 
        
        # get cols
        # print (year)
        df = create_dataframe(soup)
        print (df)