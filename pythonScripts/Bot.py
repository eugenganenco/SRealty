from housingDataCollector import housingDataCollector
from DataPreprocessor import DataPreprocessor
import pandas as pd

class Bot:
    def __init__(self):
        self.__dataCollector = housingDataCollector()


    def start(self):
        #self.__dataCollector.saveLinks()
        self.__dataCollector.readLinks()
        #df = pd.read_csv('/Users/eugenganenco/Desktop/srealtyAnalysis/housesDf_23_10_2022_05_13_29.csv')
        #dataPreProcessor = DataPreprocessor(df)
        #dataPreProcessor.setUpData()



