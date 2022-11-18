from geopy.geocoders import Nominatim
from FileNavigator import FileNavigator
import googletrans
import pandas as pd


class DataPreprocessor:
    def __init__(self, path):
        self.PATH = path
        self.fileNavigator = FileNavigator()
        self.fileNavigator.goToDir("".join([c for c in path.split('/')][:-1]))
        self.__df = pd.read_csv(path)

    def setUpData(self):
        #self.translateColumns()
        #self.findCoordinates()
        self.findPrice()

    def translateColumns(self):
        translator = googletrans.Translator()
        self.__df.columns = [translator.translate(colName).text for colName in self.__df.columns]
        self.__df.to_csv(f'{self.PATH} translated.csv')

    def findCoordinates(self):
        self.__df['locationLat'] = ""
        self.__df['locationLong'] = ""
        geolocator = Nominatim(user_agent='Srealty')
        for index in self.__df.index:
            try:
                location = geolocator.geocode(self.__df['location'][index])
                if not location:
                    location = self.__findSimplifiedLocationCoordinates(self.__df['location'][index], geolocator)
                self.__df.loc[index, 'locationLat'] = location.latitude
                self.__df.loc[index, 'locationLong'] = location.longitude
            except:
                self.__df.loc[index, 'locationLat'] = "Unknown"
                self.__df.loc[index, 'locationLong'] = "Unknown"
        self.__df.to_csv(f'{self.PATH} translatedWithCoord.csv')

    def findPrice(self):
        self.__df['price'] = ""
        self.__df['total price'] = self.__df['total price'].fillna(self.__df['Discounted'])
        for index in self.__df.index:
            try:
                self.__df.loc[index, 'price'] = self.extractPrice(self.__df.loc[index, 'total price'])
            except TypeError:
                self.__df.loc[index, 'price'] = 0
        self.__df.to_csv(f'{self.PATH} translatedWithCoordAndPrice.csv')

    def extractPrice(self, priceString):
        charArray = []
        for c in priceString:
            if c == '(':
                break
            if c.isdigit():
                charArray.append(c)
        if charArray:
            return int(''.join(charArray))
        else:
            return 0

    def __findSimplifiedLocationCoordinates(self, locationString, geolocator):
        if ' ' not in locationString:
            return geolocator.geocode(locationString)
        locationList = locationString.split(' ')
        locationString = " ".join([word for word in locationList[1:] if '-' not in word])
        location = geolocator.geocode(locationString)
        if location:
            return location
        else:
            return self.__findSimplifiedLocationCoordinates(locationString, geolocator)

