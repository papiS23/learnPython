from flask import Flask
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://scott:tiger@localhost/lotnisko"

names = {"bartek" : {"age" : 17, "gender" : "male"},
         "marysia" : {"age" : 18, "gender" : "female"}}

class getInfo(Resource):
    def get(self, name):

        return {"data" : names[name]}

api.add_resource(getInfo, "/getinfo/<string:name>")




if __name__ == "__main__":
    app.run(debug=True)