from imports import *
#### tony improved this for eytan

## create column names list
def create_list(txt):
    col_names=txt.splitlines()
    new_col = []
    for i in col_names:
        if i != '':
            new_col.append(i)

    return new_col


def list_split(listA, n):
    """https://appdividend.com/2021/06/15/how-to-split-list-in-python/"""
    arr_save=[]
    for x in range(0, len(listA), n):
        every_chunk = listA[x: n+x]

        if len(every_chunk) < n:
            every_chunk = every_chunk + \
                [None for y in range(n-len(every_chunk))]
        yield every_chunk
        arr_save.append(list(every_chunk))
    return arr_save


def parse_page():
    ## first time getting col_names:
    url="https://www.numbeo.com/quality-of-life/rankings_by_country.jsp?title=2014"


    resp = requests.get(url)  ##scrapping for col names
    soup = bs4.BeautifulSoup(resp.text, 'html.parser')


    table = soup.find("table", attrs={"id": "t2"})

    col_names=create_list(table.thead.text) ## get col_names
    col_names.remove('Rank') ## doesn't download the data for it and not so important

    arr_years=[date for date in range(2014,2022)] ## get years
    total_data=[] ## here I save all of the data of the countries

    ## now running according to years
    for d in arr_years:
        url = "https://www.numbeo.com/quality-of-life/rankings_by_country.jsp?title="
        url+=str(d)
        resp = requests.get(url)
        soup = bs4.BeautifulSoup(resp.text, 'html.parser')
        table = soup.find("table", attrs={"id": "t2"})
        data_by_year = create_list(table.tbody.text)
        print(data_by_year)
        ## splitting list according to amount of columns per country
        total_data.append(list(list_split(data_by_year,len(col_names))))

    """https://stackoverflow.com/questions/952914/how-to-make-a-flat-list-out-of-a-list-of-lists"""
    ## take the list 1D lower
    flat_list = [item for sublist in total_data for item in sublist]

    df=pd.DataFrame(data=flat_list,columns=col_names)
    print(df)


parse_page()