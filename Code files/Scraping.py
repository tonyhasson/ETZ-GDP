from imports import *


def load_soup_object(URL,year):
    url = URL + str(year)
    content = requests.get(url)
    r =BeautifulSoup(content.text,'html.parser')
    return r


def create_dataframe(URL,yearStart,yearEnd,drop_columns,CSV_name=None):
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
                    row.append(td.text.lstrip())
                    flag=1
                elif flag==1:
                    row.insert(0,i)
                    items.append(row)
                    row =[]
    df = pd.DataFrame(items, columns=column)
    df.drop(drop_columns,axis=1,inplace=True)

    df.to_csv(r"..\CSV files\Scraping CSV\df"+str(CSV_name) +".csv")
    return df

df1=create_dataframe("https://www.numbeo.com/quality-of-life/rankings_by_country.jsp?title=",2014,2021,['Cost of Living Index','Property Price to Income Ratio','Health Care Index'],1)
df2=create_dataframe("https://www.numbeo.com/property-investment/rankings_by_country.jsp?title=",2009,2021,[],2)
df3=create_dataframe("https://www.numbeo.com/cost-of-living/rankings_by_country.jsp?title=",2009,2021,[],3)
df4=create_dataframe("https://www.numbeo.com/health-care/rankings_by_country.jsp?title=",2014,2021,[],4)