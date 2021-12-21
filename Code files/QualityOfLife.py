from bs4 import BeautifulSoup
import pandas
import pandas as pd
import requests
#import imports
# Made By Eytan

def load_soup_object(year):
    url = 'https://www.numbeo.com/quality-of-life/rankings_by_country.jsp?title=' + str(year)
    content = requests.get(url)
    r =BeautifulSoup(content.text,'html.parser')
    return r



def create_dataframe():
    for i in range(2012,2022):
        column=[]
        if i != 2013 & i != 2014:
            html_file=load_soup_object(i)
        else:
            html = open(r'C:\Users\eytan\PycharmProjects\ETZ-GDP\Quality of Life Index by Country '+ str(i)+'.html' ,encoding='utf-8')
            html_file=BeautifulSoup(html.read(), 'html.parser')
        items=[]
        row=[]
        table =html_file.find('table',id='t2')
        for th in table.findAll('th'):
            column.append(th.text)
        flag=0
        column.pop(0)
        for tr in html_file.findAll('tbody'):
            for td in tr.findAll('td'):
                if td.text !='':
                    row.append(td.text)
                    flag=1
                elif flag==1:
                    items.append(row)
                    row =[]
        df = pd.DataFrame(items, columns=column)
        df.drop(['Cost of Living Index','Property Price to Income Ratio'],axis=1,inplace=True)
        df.to_csv(r'C:\Users\eytan\PycharmProjects\ETZ-GDP\CSV files\QualityOfLife\'' + str(i) + '.csv')
        if i == 2012:
            print(df)

create_dataframe()
