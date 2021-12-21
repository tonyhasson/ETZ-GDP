def reformatCSV(CSV_location,CSV_name,Start_year,End_year):
    columns=['Country','Year',CSV_name]
    df = pd.read_csv(CSV_location + CSV_name + '.csv')
    newrow =[]
    for row in df.iterrows():
        for i in range(Start_year,End_year+1):
            newrow.append([row[1]['Country'],i,row[1][str(i)]])

    reformated= pd.DataFrame(newrow,columns=columns)
    reformated.to_csv(CSV_location + CSV_name + 'REFORMAT.csv')