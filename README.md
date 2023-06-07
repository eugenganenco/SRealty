# SRealty
## The goal of this project is to collect and analyze the data from https://www.sreality.cz/.

## The project is tructured in 3 parts:
1. Web scraper
2. Jupyter Notebooks analyzing the data
3. telegram bot that is supposed to notify its users about new houses on the market based on their querries and suggestion algorithm trained on the collected data. (not finished)

### Web scraper
  The web scraper collects the data about the houses on the market from srealty.cz and saves this information in csv files. Because srealty.cz has periodic updates, for the webscraper to run - it should be updated as well with every update on the site that significantly modifies the HTML code. Also, to run the webscraper, the user needs to install chrome web driver and input their authenitfication credentials in the constructor housingDataCollector class. 
  
  The main class for the webscraper is Bot.py. This class outlines the overarching logic behind this webscraper, which is the following:
a) collect every link associated with every house listed on the site and save the links in a csv file
b) go through each link and extract the relevant data about each house and save it in a csv file, where each row is a house and each column some useful parameter about it
c) DataPreprocessor class mofifies the final csv file by finding the geografic coordinates for each house, can translate the column names, and finds the price of the house when the posting does not use the conventional way to inform the user about it.

  There is also a FileNavigator class that streamelines and assists in the creation of new files and folders when collection the data.
