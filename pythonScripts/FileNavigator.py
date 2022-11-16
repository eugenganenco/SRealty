import glob
import logging
import re
import os
from datetime import datetime


class FileNavigator:
    pass

    def makeDataFolder(self):
        try:
            directory = f'{self.goToRootDir()}/data/DataFile {datetime.now().strftime("%d_%m_%Y_%H_%M")}'
            if not os.path.exists(directory):
                os.mkdir(directory)
                return directory
        except OSError:
            logging.error('Error: Creating a new directory')

    def goToRootDir(self):
        directory = os.getcwd()
        try:
            while not re.search('srealtyAnalysis$', directory):
                os.chdir(directory + '/..')
                directory = os.getcwd()
            return directory
        except OSError:
            logging.error('Error: Creating Directory' + directory)

    def goToFreshDataFolder(self):
        try:
            os.chdir(f'{self.goToRootDir()}/data')
            allSubDirs = [d for d in os.listdir('.') if os.path.isdir(d)]
            os.chdir(max(allSubDirs, key=os.path.getmtime))
        except OSError:
            logging.error('Error: Finding')

    def goToDir(self, name):
        try:
            os.chdir(name)
        except OSError:
            logging.error(f'Error: Finding {name}')

    def getLatestTxtFile(self):
        try:
            print(os.getcwd())
            list_of_files = glob.glob(f'{os.getcwd()}/*.txt')
            return max(list_of_files, key=os.path.getctime)
        except OSError:
            logging.error(f'Error: Finding the latest txt file')