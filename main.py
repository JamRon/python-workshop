from flask import Flask
from flask import request
from flask import render_template
from flask_restful import Api, Resource, reqparse

#Creating an Application
app = Flask(__name__)

#Attaching an API to the Application
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument("data",location='json')

@app.route("/")
def hello():
    return render_template('home.html')


class RouteOne(Resource):
    def get(self):
        return "You Successfully Got information from route 1"
    def post(self):
        return "You Successfully Posted information to route 1"

class RouteTwo(Resource):
    def get(self):
        return "You Successfully Got information from route 2"
    def post(self):
        data = parser.parse_args()

        return "You Successfully Posted information to route 2 and the data is: " + data["data"]

api.add_resource(RouteOne, '/api/one')
api.add_resource(RouteTwo, '/api/two')

if __name__=="__main__":
    app.run(debug=True)



