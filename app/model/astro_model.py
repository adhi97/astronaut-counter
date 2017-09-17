from dao.astro_dao import AstroDao

class AstroModel:
    def __init__(self, collection):
        self.id = str(collection['_id'])
        self.name = collection['name']
        self.spacecraft = collection['craft']

    @staticmethod
    def findAstronautById(self, astroId):
        DAO = AstroDao()
        #call the DAO to find findAstronautByName

    @staticmethod
    def getAllAstronauts(self):
        DAO = AstroDao()
        #second get functionality

    @staticmethod
    def createAstronaut(self, astroInfo):
        DAO = AstroDao()
        #for post function

    @staticmethod
    def updateAstronaut(self, astroId):
        DAO = AstroDao()
        #for put function

    @staticmethod
    def deleteAstronaut(self, astroId):
        DAO = AstroDao()
        #for delete function
