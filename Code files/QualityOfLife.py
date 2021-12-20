import bs4
import pandas
import pandas as pd
import requests
import imports
# Made By Eytan

def load_soup_object(year):
    url = 'https://www.numbeo.com/quality-of-life/rankings_by_country.jsp?title=' + str(year)
    content = requests.get(url)
    r =bs4.BeautifulSoup(content.text,'html.parser')
    return r

def create_col_list(txt):

    col_names = txt.split("\n")
    new_col = []
    for i in col_names:
        if i != '':
            new_col.append(i)
    col_names=[]
    for j in new_col:
        if len(j)!=1:
            col_names.append(j)
    return col_names


def create_dataframe():
    for i in range(2021,2022):
        column=[]
        html_file=load_soup_object(i)
        items=[]
        row=[]
        table =html_file.find('table',id='t2')
        for th in table.findAll('th'):
            column.append(th.text)

        for tr in html_file.find('tbody'):
            text=create_col_list(tr.text)
            row.append(text)
        print(row)
        #df = pd.DataFrame(items, columns=column)
        #print(df)

create_dataframe()
