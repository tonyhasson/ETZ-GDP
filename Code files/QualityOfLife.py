import os

from bs4 import BeautifulSoup
import pandas
import pandas as pd
import requests
#import imports
# Made By Eytan

def load_soup_object(URL,year):
    url = URL + str(year)
    content = requests.get(url)
    r =BeautifulSoup(content.text,'html.parser')
    return r



def create_dataframe(URL,yearStart,yearEnd,drop_columns,CSV_name):
    html_file = load_soup_object(URL,yearStart)
    column = []
    table = html_file.find('table', id='t2')
    for th in table.findAll('th'):
        column.append(th.text)
    column[0]='Year'
    items = []
    for i in range(yearStart,yearEnd+1):
        html_file = load_soup_object(URL,i)
        row=[]
        flag=0
        for tr in html_file.findAll('tbody'):
            for td in tr.findAll('td'):
                if td.text !='':
                    row.append(td.text)
                    flag=1
                elif flag==1:
                    row.insert(0,i)
                    items.append(row)
                    row =[]
    df = pd.DataFrame(items, columns=column)
    df.drop(drop_columns,axis=1,inplace=True)
    path = os.path.dirname(__file__)
    df.to_csv(os.path.join( path,r"..\CSV files\\" + r"\\"+ CSV_name+".csv"))


#create_dataframe("https://www.numbeo.com/quality-of-life/rankings_by_country.jsp?title=",2014,2021,['Cost of Living Index','Property Price to Income Ratio'], 'QualityOfLife')


def reformatCSV(CSV_location,CSV_name,Start_year,End_year):
    columns=['Country','Year',CSV_name]
    df = pd.read_csv(CSV_location + CSV_name + '.csv')
    newrow =[]
    for row in df.iterrows():
        for i in range(Start_year,End_year+1):
            newrow.append([row[1]['Country'],i,row[1][str(i)]])

    reformated= pd.DataFrame(newrow,columns=columns)
    reformated.to_csv(CSV_location + CSV_name + 'REFORMAT.csv')

#reformatCSV(r"..\CSV files\Education Ranking\\","Education Ranking",1990,2019)
reformatCSV(r"..\CSV files\GDP\\","GDP Growth",1960,2020)
reformatCSV(r"..\CSV files\GDP\\","GDP Total",1960,2020)
reformatCSV(r"..\CSV files\Health\\","Life expectancy at birth",1960,2020)
reformatCSV(r"..\CSV files\High-Tech\\","High Tech Exports(% of total)",2007,2020)
reformatCSV(r"..\CSV files\High-Tech\\","High Tech Exports(total)",2007,2020)
reformatCSV(r"..\CSV files\Household\\","Final consumption expenditure",1960,2020)
reformatCSV(r"..\CSV files\Population\\","Population Growth pace",1960,2020)
reformatCSV(r"..\CSV files\Population\\","Population Total",1960,2020)