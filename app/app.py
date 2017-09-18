from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse, request
from model.astro_model import AstroModel

app = Flask(__name__)
api = Api(app)

class Astronauts(Resource):
    def get(self):
        print "getting all astros"
        try:
            astros = AstroModel.getAllAstronauts()
        except Exception:
            #do something: return
        data = jsonify(astros.__dict__)
        return data

    def post(self):
        print "posting an astronaut"
        payload = request.get_json()

        try:
            astro = AstroModel.createAstronaut(payload)
        except Exception:
            return #return an error

        data = jsonify(astro.__dict__)
        return data

    def delete(self):
        print "deleting all astronauts"
        #implement deletion of the entire database

class Astronaut(Resource):
    def get(self, astroId):
        print "getting information about 1 Astronaut"

        try:
            astronaut = AstroModel.findAstronautById(astroId)
        except Exception:
            #return an error

        if astronaut: #might be redundant
            return astronaut
        else return None

    def delete(self, astroId):
        print "deleting an Astronaut with ID: " + repr(astroId)

        try:
            deletedAstro = AstroModel.deleteAstronaut(astroId)
        except Exception:
            # return error

        if deletedAstro:
            return deletedAstro
        else return None #possibly replace with a validator

    def post(self):
        print "posting an astronaut"
        payload = request.get_json()

        try:
            astro = AstroModel.createAstronaut(payload)
        except Exception:
            # return error

        data = jsonify(astro.__dict__)
        return data

    def put(self, astroId):
        print "updating an Astronaut with ID: " + repr(astroId)
        payload = request.get_json()

        try:
            astro = AstroModel.updateAstronaut(astroId, payload)
        except Exception:
            #return

        data = jsonify(astro.__dict__)
        return data

api.add_resource(Astronauts, '/astronauts')
api.add_resource(Astronaut, '/astronauts/<string:astroId>')

if __name__ == '__main__':
    app.run(host=0.0.0.0, port=5000, debug=True)
