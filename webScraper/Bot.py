from HousingDataCollector import HousingDataCollector
from DataPreprocessor import DataPreprocessor

class Bot:
    def __init__(self):
        self.__dataCollector = housingDataCollector()
        self.PATH = ''

    def start(self):
        self.__dataCollector.saveLinks()
        self.__dataCollector.readLinks()
        dataPreProcessor = DataPreprocessor(self.PATH)
        dataPreProcessor.setUpData()



