from imports import *

CSV_FILES=['Scraping CSV\df1','Scraping CSV\df2','Scraping CSV\df3','Scraping CSV\df4','Education RankingREFORMAT','Final consumption expenditureREFORMAT','GDP GrowthREFORMAT','GDP TotalREFORMAT','Government ExpenditureREFORMAT','Government Expense(of total GDP)REFORMAT','High Tech Exports(% of total)REFORMAT','High Tech Exports(total)REFORMAT','Life expectancy at birthREFORMAT','Population Growth paceREFORMAT','Population TotalREFORMAT','Military Expenditure totalREFORMAT','Military Expenditure(% of GDP)REFORMAT']
List_Of_Countries=['Aruba','Afghanistan','Albania','Algeria','Andorra','Angola','Antigua and Barbuda','Argentina','Armenia','Australia','Austria','Azerbaijan','Bahamas','Bahrain','Bangladesh','Barbados','Belarus','Belgium','Belize','Benin','Bhutan','Bolivia','Bosnia and Herzegovina','Botswana','Brazil','Brunei','Bulgaria','Burkina Faso','Burundi','Ivory Coast','Cabo Verde','Cambodia','Cameroon','Canada','Central African Republic','Chad','Chile','China','Colombia','Comoros','Congo (Congo-Brazzaville)','Costa Rica','Croatia','Cuba','Cyprus','Czechia (Czech Republic)','Democratic Republic of the Congo','Denmark','Djibouti','Dominica','Dominican Republic','Ecuador','Egypt','El Salvador','Equatorial Guinea','Eritrea','Estonia','Eswatini','Ethiopia','Fiji','Finland','France','Gabon','Gambia','Georgia','Germany','Ghana','Greece','Grenada','Guatemala','Guinea','Guinea-Bissau','Guyana','Haiti','Holy See','Honduras','Hungary','Iceland','India','Indonesia','Iran','Iraq','Ireland','Israel','Italy','Jamaica','Japan','Jordan','Kazakhstan','Kenya','Kiribati','Kuwait','Kyrgyzstan','Laos','Latvia','Lebanon','Lesotho','Liberia','Libya','Liechtenstein','Lithuania','Luxembourg','Madagascar','Malawi','Malaysia','Maldives','Mali','Malta','Marshall Islands','Mauritania','Mauritius','Mexico','Micronesia',',Moldova','Monaco','Mongolia','Montenegro','Morocco','Mozambique','Myanmar','Namibia','Nauru','Nepal','Netherlands','New Zealand','Nicaragua,','Niger','Nigeria','North Korea','North Macedonia','Norway','Oman','Pakistan','Palau','Palestine State','Panama','Papua New Guinea','Paraguay','Peru','Philippines','Poland','Portugal','Qatar','Romania','Russia','Rwanda','Saint Kitts and Nevis','Saint Lucia','Saint Vincent and the Grenadines','Samoa,','San Marino','Sao Tome and Principe','Saudi Arabia','Senegal','Serbia','Seychelles','Sierra Leone','Singapore','Slovakia','Slovenia','Solomon Islands','Somalia','South Africa','South Korea','South Sudan','Spain','Sri Lanka','Sudan','Suriname','Sweden','Switzerland','Syria','Tajik,istan','Tanza,nia','Thailand','Timor-Leste','Togo','Tonga','Trinidad and Tobago','Tunisia','Turkey','Turkmenistan','Tuvalu','Uganda','Ukraine','United Arab Emirates','United Kingdom','United States of America','Uruguay','Uzbekistan','Vanuatu','Venezuela','Vietnam','Yemen','Zambia','Zimbabwe']


#Function to reformat existing dataframe to [Country, Year, Value] format
def reformatCSV(CSV_location,CSV_name,Start_year,End_year):
    columns=['Country','Year',CSV_name]
    df = pd.read_csv(CSV_location + CSV_name + '.csv' , encoding="ISO-8859-1")
    newrow =[]
    for row in df.iterrows():
        for i in range(Start_year,End_year+1):
            newrow.append([row[1]['Country'].lstrip(),i,row[1][str(i)]])

    reformated= pd.DataFrame(newrow,columns=columns)
    reformated.to_csv(r"..\CSV files\\" + CSV_name + 'REFORMAT.csv')

#Merge all dataframes into one and clean it a bit.
def merge_and_clean(arr_df):

    ##merge
    for i in range(len(arr_df)-1):
        arr_df[i+1] = arr_df[i].merge(arr_df[i+1], on=['Year', 'Country'], how='outer')

    ##clean
    df=arr_df[len(arr_df)-1]
    df.sort_values(['Country','Year'], axis=0, ascending=True, inplace=True)
    df.drop(['Unnamed: 0_x', 'Unnamed: 0_y'], axis=1, inplace=True)
    #remove all rows where year<1960
    df=df[df['Year']>=1960]
    #remove all unknown and irrelevant countries
    df=df[df['Country'].isin(List_Of_Countries)]

    print(df.isnull().sum().sum())
    print(df.shape[0])
    return df

#Function to build Array of dataframes from CSV files
def arr_df_builder():
    path = os.path.dirname(__file__)
    arr_df=[]
    for i in range(len(CSV_FILES)):
        text=r"..\CSV files\\"
        text+=CSV_FILES[i]
        text+=".csv"
        arr_df.append(pd.read_csv(os.path.join(path, text)))
    return arr_df


# reformatCSV(r"..\CSV files\OLD\\","Education Ranking",1990,2019)
# reformatCSV(r"..\CSV files\OLD\\","GDP Growth",1960,2020)
# reformatCSV(r"..\CSV files\OLD\\","GDP Total",1960,2020)
# reformatCSV(r"..\CSV files\OLD\\","Life expectancy at birth",1960,2020)
# reformatCSV(r"..\CSV files\OLD\\","High Tech Exports(% of total)",2007,2020)
# reformatCSV(r"..\CSV files\OLD\\","High Tech Exports(total)",2007,2020)
# reformatCSV(r"..\CSV files\OLD\\","Final consumption expenditure",1960,2020)
# reformatCSV(r"..\CSV files\OLD\\","Population Growth pace",1960,2020)
# reformatCSV(r"..\CSV files\OLD\\","Population Total",1960,2020)

arr_df=arr_df_builder()
merge_and_clean(arr_df).to_csv(r"..\CSV files\df_Total.csv")


