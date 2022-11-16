from geopy.geocoders import Nominatim
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
import googletrans
import pandas as pd
import housingDataCollector
import os
import logging
import re

class Playground:
    def __init__(self):
        # geolocator = Nominatim(user_agent='Srealty')
        # location = geolocator.geocode('Teplá - Babice, okres Cheb')
        # if not location:
        #     location = self.__findSimplifiedLocationCoordinates('Teplá - Babice, okres Cheb', geolocator)
        # print(location.latitude)
        self.__makeDataFolder()
        self.__goToFreshDataFolder()
        with open('test.txt', mode="w") as file:
            file.write('fileHeading')


    def __findSimplifiedLocationCoordinates(self, locationString, geolocator):
        if ' ' not in locationString:
            return geolocator.geocode(locationString)
        locationList = locationString.split(' ')
        locationString = " ".join([word for word in locationList[1:] if '-' not in word])
        print(locationString)
        location = geolocator.geocode(locationString)
        if location:
            return location
        else:
            return self.__findSimplifiedLocationCoordinates(locationString, geolocator)

    def __makeDataFolder(self):
        try:
            directory = f'{self.__goToRootDir()}/data/DataFolder11'
            if not os.path.exists(directory):
                os.mkdir(directory)
                return directory
        except OSError:
            logging.error('Error: Creating a new directory')

    def __goToRootDir(self):
        directory = os.getcwd()
        print(directory)
        try:
            while not re.search('srealtyAnalysis$', directory):
                os.chdir(directory + '/..')
                directory = os.getcwd()
            return directory
        except OSError:
            logging.error('Error: Creating Directory' + directory)

    def __goToFreshDataFolder(self):
        try:
            os.chdir(f'{self.__goToRootDir()}/data')
            allSubDirs = [d for d in os.listdir('.') if os.path.isdir(d)]
            os.chdir(max(allSubDirs, key=os.path.getmtime))
        except OSError:
            logging.error('Error: Finding')