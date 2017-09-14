from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

class Weather(Resource):
    def get(self):
        print "getting weather data"
        return #to be implemented (DAO class)

    def post(self):
        print "posting weather data"
        parser = reqparse.RequestParser()
        return #success or failure


api.add_resource(Weather, '/')

if __name__ == '__main__':
    app.run(debug=True)
