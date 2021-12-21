# DataFrames
import pandas as pd

# Network, Crawlling and Scraping
import requests
import bs4
from bs4 import BeautifulSoup

# Visualization
#import matplotlib as mpl
#import matplotlib.pyplot as plt
#import seaborn as sns

# General
#import re
#import os
#import scipy as sc
import numpy as np
from collections import Counter

# ML
#import sklearn
#from sklearn import linear_model, metrics, preprocessing
#from sklearn.preprocessing import StandardScaler, MinMaxScaler
#from sklearn.linear_model import LogisticRegression, LinearRegression
#from sklearn.metrics import r2_score, f1_score


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
    
    # Get the table
    table = page.find('table',id='t2')
    
    row = 0
    for tr in table.findAll('tr'):
        vals.append(tr.get_text().splitlines()) # just like split but for lines
        while vals[row][0] == '':
            vals[row].pop(0) # removing the blank spots ## usually just 2 blanks so its quite efficient
        row += 1
         
    cols = vals.pop(0) # Table's cols at vals[0]
    cols.pop(0) # poping out the rank cause its useless
    
    # Creating DataFrame to return
    return pd.DataFrame(data = vals,columns=cols)


if __name__ == "__main__":
    years = [ str(i) for i in range(2009,2021)]
    for year in years:
        # get an object and loading it
        df = create_dataframe(load_soup_object(year))
        print ("##########################")
        print (year)
        print (df)
        print ("##########################")