from housingDataCollector import housingDataCollector
from DataPreprocessor import DataPreprocessor

class Bot:
    def __init__(self):
        self.__dataCollector = housingDataCollector()
        self.PATH = '/Users/eugenganenco/Desktop/srealtyAnalysis/data/DataFile 16_11_2022_22_43/housesDf_17_11_2022_00_06_15.csv translatedWithCoord.csv'

    def start(self):
        self.__dataCollector.saveLinks()
        self.__dataCollector.readLinks()
        dataPreProcessor = DataPreprocessor(self.PATH)
        dataPreProcessor.setUpData()



