from dao.astro_dao import AstroDao

class AstroModel:
    def __init__(self, collection):
        self.id = str(collection['_id'])
        self.name = collection['name']
        self.spacecraft = collection['craft']

    @staticmethod
    def findAstronautById(self):
        DAO = AstroDao()

        #call the DAO to find findAstronautByName

    @staticmethod
    def getAllAstronauts(self):
        DAO = AstroDao()

    @staticmethod
    def createAstronaut(self):
        DAO = AstroDao()

    @staticmethod
    def update
