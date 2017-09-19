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
            return AstroModel(astronaut)
        else: return None

    @staticmethod
    def getAllAstronauts():
        DAO = AstroDao()
        allAstros = DAO.getAstronauts()
        astronauts = []
        for astronaut in allAstros.find():
            astronauts.append(AstroModel(astronaut))
        return repr(astronauts) #check to see why it doesnt work without repr()

    @staticmethod
    def createAstronaut(astroInfo):
        DAO = AstroDao()
        newAstro = DAO.createAstronaut(astroInfo)
        
        if newAstro:
            return AstroModel(newAstro)
        else: return None

    @staticmethod
    def updateAstronaut(astroId, astroInfo):
        DAO = AstroDao()
        updatedAstro = DAO.updateAstronaut(astroId, astroInfo)
       
        if updatedAstro:
            return AstroModel(updatedAstro)
        else: 
            return None

#    @staticmethod
#    def deleteAll():
        #implement later

    @staticmethod
    def deleteAstronaut(astroId):
        DAO = AstroDao()
        if astroId:
            return DAO.deleteAstronautById(astroId)
        else: 
            return None

    @staticmethod
    def postMulipleAstros(astroInfo):
        DAO = AstroDao()
        postedAstros = DAO.createManyAstronauts(astroInfo)

        astronauts = []

        if postedAstros:
            for astronaut in postedAstros:
                astronauts.append(AstroModel(astronaut))
            return astronauts
        else: 
            return None
