class URL_helper:
    def __init__(self):
        self.__HOUSE_TYPES_LIST = ['rodinne-domy', 'vily', 'chalupy', 'chaty', 'projekty-na-klic', 'zemedelske-usedlosti',
                                        'pamatky-jine', 'vicegeneracni-domy']
        self.__HOUSE_LOCATIONS_DICT = {'Karlovarsky': ['cheb', 'karlovy-vary','sokolov'],
                                       'Plzensky': ['tachov', 'rokycany', 'plzen-sever', 'plzen', 'plzen-jih', 'klatovy', 'domazlice'],
                                       'Ustecky': ['usti-nad-labem', 'teplice', 'most', 'louny', 'litomerice', 'decin', 'chomutov'],
                                       'Stredocesky': ['benesov', 'beroun', 'kladno', 'kolin', 'kutna-hora', 'melnik', 'mlada-boleslav', 'nymburk', 'praha-vychod', 'praha-zapad', 'pribram', 'rakovnik'],
                                       'Praha': ['praha-1', 'praha-2', 'praha-3', 'praha-4', 'praha-5', 'praha-6', 'praha-7', 'praha-8', 'praha-9', 'praha-10'],
                                       'Jihocesky': ['ceske-budejovice', 'cesky-krumlov', 'jindrichuv-hradec', 'pisek', 'prachatice', 'strakonice', 'tabor'],
                                       'Vysocine': ['havlickuv-brod', 'jihlava', 'pelhrimov', 'trebic', 'zdar-nad-sazavou'],
                                       'Pardubicky': ['chrudim', 'pardubice', 'svitavy', 'usti-nad-orlici'],
                                       'Kralovehradecky': ['hradec-kralove', 'jicin', 'nachod', 'rychnov-nad-kneznou', 'trutnov'],
                                       'Liberecky': ['ceska-lipa', 'jablonec-nad-nisou', 'liberec', 'semily'],
                                       'Jihomoravsky': ['blansko', 'breclav', 'brno', 'brno-venkov', 'hodonin', 'vyskov', 'znojmo'],
                                       'Olomoucky': ['olomouc', 'prerov', 'jesenik', 'prostejov', 'sumperk'],
                                       'Zlinsky': ['kromeriz', 'uherske-hradiste', 'vsetin', 'zlin'],
                                       'Moravskoslezsky': ['bruntal', 'frydek-mistek', 'karvina', 'novy-jicin', 'opava', 'ostrava']}

        self.__ENGLISH_NAME_TO_CZECH = {'Praha': 'Prague', 'benesov': 'Benešov', 'beroun': 'Beroun', 'kladno': 'Kladno', 'kolin': 'Kolín',
                                       'kutna-hora': 'Kutná Hora', 'melnik': 'Mělník', 'mlada-boleslav': 'Mladá Boleslav', 'nymburk': 'Nymburk',
                                       'praha-vychod': 'Prague-East', 'praha-zapad': 'Prague-West', 'pribram': 'Příbram', 'rakovnik': 'Rakovník',
                                       'ceske-budejovice': 'České Budějovice','cesky-krumlov': 'Český Krumlov','jindrichuv-hradec': 'Jindřichův Hradec',
                                       'pisek': 'Písek', 'prachatice': 'Prachatice', 'strakonice': 'Strakonice', 'tabor': 'Tábor', 'domazlice': 'Domažlice',
                                       'klatovy': 'Klatovy', 'plzen': 'Plzeň-City', 'plzen-jih': 'Plzeň-South', 'plzen-sever': 'Plzeň-North',
                                       'rokycany': 'Rokycany', 'tachov': 'Tachov', 'cheb': 'Cheb', 'karlovy-vary': 'Karlovy Vary', 'sokolov': 'Sokolov',
                                       'chomutov': 'Chomutov', 'decin': 'Děčín', 'litomerice': 'Litoměřice', 'louny': 'Louny', 'most': 'Most', 'teplice': 'Teplice',
                                       'usti-nad-labem': 'Ústí nad Labem', 'ceska-lipa': 'Česká Lípa', 'jablonec-nad-nisou': 'Jablonec nad Nisou',
                                       'liberec': 'Liberec', 'semily': 'Semily', 'hradec-kralove': 'Hradec Králové', 'jicin': 'Jičín', 'nachod': 'Náchod',
                                       'rychnov-nad-kneznou': 'Rychnov nad Kněžnou', 'trutnov': 'Trutnov', 'chrudim': 'Chrudim', 'pardubice': 'Pardubice',
                                       'svitavy': 'Svitavy', 'usti-nad-orlici': 'Ústí nad Orlicí', 'havlickuv-brod': 'Havlíčkův Brod', 'jihlava': 'Jihlava',
                                       'pelhrimov': 'Pelhřimov', 'trebic': 'Třebíč', 'zdar-nad-sazavou': 'Žďár nad Sázavou', 'blansko': 'Blansko',
                                       'breclav': 'Břeclav', 'brno': 'Brno-City', 'brno-venkov': 'Brno-Country', 'hodonin': 'Hodonín', 'vyskov': 'Vyškov',
                                       'znojmo': 'Znojmo', 'jesenik': 'Jeseník', 'olomouc': 'Olomouc', 'prerov': 'Přerov', 'prostejov': 'Prostějov',
                                       'sumperk': 'Šumperk', 'kromeriz': 'Kroměříž', 'uherske-hradiste': 'Uherské Hradiště', 'vsetin': 'Vsetín',
                                        'zlin': 'Zlín', 'bruntal': 'Bruntál', 'frydek-mistek': 'Frýdek-Místek', 'karvina': 'Karviná', 'novy-jicin': 'Nový Jičín',
                                        'opava': 'Opava', 'ostrava': 'Ostrava-City'}

    def getEnglishNameToCzechDict(self):
        return self.__ENGLISH_NAME_TO_CZECH

    def getHouseTypesList(self):
        return self.__HOUSE_TYPES_LIST

    def getHouseLocationsDict(self):
        return self.__HOUSE_LOCATIONS_DICT

    def getLocationsSet(self):
        regionsSet = set()
        for region in self.__HOUSE_LOCATIONS_DICT:
            if region == 'Praha':
                regionsSet.add('praha')
            else:
                regionsSet = regionsSet.union(set(self.__HOUSE_LOCATIONS_DICT[region]))
        return regionsSet

    def getLen(self):
        return len(self.getLocationsSet())
