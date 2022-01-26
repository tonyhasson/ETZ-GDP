# To Do List:

## Data

- ~~SCARPING data from various sources~~
- ~~Analyze the data~~
- ~~Cleaning data and outliers (Cleaned all countries with population lower than 100K)~~
- ~~Check the values before inserting our default '0' | some may need negative value~~
- ~~lower the dimension for ML and clusters~~
- ~~Delete Health CareEXp && Cost of living+rent~~
- Check life expectancy at 1960 and 2020 calc diff ?

## Visuals

- ~~Visually show the Clusters~~
- ~~Visually show the correlation between different variables | plots and so~~
- ~~Add title to plot in corrs for better readability and info~~
- ~~CORR: price to rent USA 2008-2009~~
- ~~Add Comments~~
- > Presentation
- > Remove unused code (functions, comments, returns etc...) | (Merge L: 448-460) (Visualization L: 55-60 | L: 153-193 | L: 233-251 | L: 264-288)
- > Prediction on which countries has positive growth and which negative one
## Clustering

- > plot and list of countries in each cluster
- > Compare clusters of scrape_DB With full_DB
- > Comparison between different algorithms Kmeans DBscan
- Comparison between strong countries and WEST vs EAST ?
- Clustering file > KMeans and DBscan got duplicated code, do we rework it? (137-325)

## ML

- ~~Check our Linear regression model~~
- ~~Using ML, with supervised and unsupervised learning to make models and clusters~~
- > Using our models make predictions for the future (Year 2030) (MUST: China Suppress USA)

## General

- ~~Work on SCARPING DB (EDA - clusters, scatters, lower dimension, confusion matrix etc...)~~
- ~~Insert default value the mean of the continent (or possibly based on K neighboring countries)~~
- ~~Check for correlations between vals~~

### NOT MANDATORY

- ~~Change some cols name to something better~~
- ~~Globalize the DB names~~
- reduce run time for functions

## TLDR Legend:

- Price to Rent Ratio: כלל שיותר גבוה רוצים להשכיר וככל שנמוך רוצים לקנות בית
