from dao.astro_dao import AstroDao

class AstroModel:
    def __init__(self, collection):
        self.id = str(collection['_id'])
        self.name = collection['name']
        self.spacecraft = collection['craft']

    @staticmethod
    def findAstronautById(astroId):
        DAO = AstroDao()
        astronaut = DAO.getAstroById(astroId)

        if astronaut:
            return AstroModel(astronaut).__dict__
        else: return None

    @staticmethod
    def getAllAstronauts():
        DAO = AstroDao()
        allAstros = DAO.getAstronauts()
        astronauts = []
        for astronaut in allAstros.find():
            astronauts.append(astronaut)
        return repr(astronauts)

    @staticmethod
    def createAstronaut(astroInfo):
        DAO = AstroDao()
        if astroInfo:
            return DAO.createAstronaut(astroInfo)
        else: return None

    @staticmethod
    def updateAstronaut(astroId, astroInfo):
        DAO = AstroDao()
        if astroId and astroInfo:
            return DAO.updateAstronaut(astroId, astroInfo)
        else: return None

#    @staticmethod
#    def deleteAll():
        #implement later

    @staticmethod
    def deleteAstronaut(astroId):
        DAO = AstroDao()
        if astroId:
            return DAO.deleteAstronautById(astroId)
        else: return None

    @staticmethod
    def postMulipleAstros(astroInfo):
        DAO = AstroDao()
        if astroInfo:
            return DAO.createManyAstronauts(astroInfo)
        else: return None
