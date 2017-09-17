from pymongo import MongoClient
import traceback
from util.config import db_name, db_host
from pymongo import ObjectId

collectionName = 'astronauts'

class AstroDao:
    def __init__(self):
        self.connection = MongoClient(db_host)
        self.db = self.connection[db_name]
        self.collection = self.db[collectionName]

    def getAstroById(self, astroId):
        if astroId:
            return self.collection.find_one({'_id': ObjectId(astroId)})
        else return None

    def getAllAstronauts(self):
        astronauts = []
        for astronaut in self.collection.find():
            astronauts.append(AstroModel(astronaut).__dict__)
        return astronauts

    def deleteAstronautById(self, astroId):
        astronaut = self.collection.find_one({'_id:': ObjectId(astroId)})
        if not astronaut:
            return None
        else deletedAstro = self.collection.delete_one({"_id": ObjectId(astroId)})
        return deletedAstro

    def deleteAllAstronauts(self):
        #implement later

    def updateAstronaut(self, astroId, astroData):
        astronaut = self.collection.find_one({'_id': ObjectId(astroId)})
        if not astronaut:
            return None
        else updatedAstro = self.collection.update_one({"_id": ObjectId(astroId)}, {"$set": astroData}, upsert = False)
        return updatedAstro

    def createAstronaut(self, astroData):
        postId = self.collection.insert_one(astroData).inserted_id
        if postId is not None:
            return postId
        else return None

    def createManyAstronauts(self, astroData):
        result = self.collection.insert_many(astroData)
        if len(result.inserted_ids) > 1:
            return result.inserted_ids
        else return None
