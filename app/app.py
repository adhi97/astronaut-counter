from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse, request
from model.astro_model import AstroModel

app = Flask(__name__)
api = Api(app)

class Astronauts(Resource):
    def get(self):
        print "getting all astros"
        astros = AstroModel.getAllAstronauts()
        data = jsonify(astros.__dict__)
        return data

    def post(self):
        print "posting an astronaut"
        payload = request.get_json()
        astro = AstroModel.createAstronaut(payload)
        data = jsonify(astro.__dict__)
        return data

    def delete(self):
        print "deleting all astronauts"
        #implement later

class Astronaut(Resource):
    def get(self, astroId):
        print "getting information about 1 Astronaut"
        astronaut = AstroModel.findAstronautById(astroId)
        if astronaut:
            return astronaut
        else return None

    def delete(self, astroId):
        print "deleting an Astronaut with ID: " + repr(astroId)
        deletedAstro = AstroModel.deleteAstronaut(astroId)
        if deletedAstro:
            return deletedAstro
        else return None #possibly replace with a validator

    def post(self):
        print "posting an astronaut"
        payload = request.get_json()
        astro = AstroModel.createAstronaut(payload)
        data = jsonify(astro.__dict__)
        return data

    def put(self, astroId):
        print "updating an Astronaut with ID: " + repr(astroId)
        payload = request.get_json()
        astro = AstroModel.updateAstronaut(astroId, payload)
        data = jsonify(astro.__dict__)
        return data

api.add_resource(Astronauts, '/astronauts')
api.add_resource(Astronaut, '/astronauts/<string:astroId>')

if __name__ == '__main__':
    app.run(host=0.0.0.0, port=5000, debug=True)
