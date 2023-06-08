# SRealty
## The goal of this project is to collect and analyze the data from https://www.sreality.cz/.

## The project is tructured in 3 parts:
1. Web scraper
2. Jupyter Notebooks analyzing the data
3. telegram bot that is supposed to notify its users about new houses on the market based on their querries and suggestion algorithm trained on the collected data. (not finished)

### Web scraper
  The web scraper collects the data about the houses on the market from srealty.cz and saves this information in csv files. Because srealty.cz has periodic updates, for the webscraper to run - it should be updated as well every time site significantly modifies its HTML code. Also, to run the webscraper, the user needs to install chrome web driver and input their authenitfication credentials in the constructor housingDataCollector class. 
  
  The main class for the webscraper is Bot.py. This class outlines the overarching logic behind this webscraper, which is the following:
a) collect every link associated with every house listed on the site and save the links in a csv file
b) go through each link and extract the relevant data about each house and save it in a csv file, where each row is a house and each column - some useful parameter about it
c) DataPreprocessor class mofifies the final csv file by finding the geografic coordinates for each house, can translate the column names, and finds the price of the house when the posting does not use the conventional way to inform the user about the price.

  There is also a FileNavigator class that streamelines and assists in the creation of new files and folders when collecting the data.
  
  The user can view and download some of the collected data by the webscraper from the 'data' and 'oldData' folders of this project. The only difference between these two data folders is that the 'data' folder was created with the help of the FileNavigator class, so, as a consequence, it is better organised.
  
### Jupyter Notebooks
There are two jupyter notebooks in the jupyterNotebooks folder: SrealtyDataAnalysis.ipynb and Modeling.ipynb. 

SrealtyDataAnalysis.ipynb analyzes the collected data using pandas and data visualization libraries such as matplotlib and seaborn. In this document the user can find: plots displaying relationship between the dependent variable 'price' and independent variables, what are the largest real estate companies in Czech Republic and what their market share is, what are the least competitive real estate markets by type of house and location, and much more. There is also an interctive map of showing the average price of houses for every NUTS4 region in Czech Republic, but the user would have to run the notebook on their machine to see this map (GitHub file veiwer may not display this map).

Modeling.ipynb trains an XGBRegressor model using the scraped data combined with some data found on wikipedia. The goal of this model is to predict the price of houses given various parameters.

### Telegram bot
  The telegram bot should be a way for users to both interact with the data and be get notified about relevant listings collected by the webscraper based on their querries. The bot runs on aiogram library and has database functionality to store the data about its subscribers and uses webhook for receiving updates and messages from the server. The telegram bot is not finished. 


  

