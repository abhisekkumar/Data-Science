from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)



users = [
{
  "name" : "Abhisek",
  "age" : 27,
  "occupation" : "Artificial Intelligence Engineer"
},
{
  "name": "Emma",
  "age" : 28,
  "occupation": "Actress & Philanthropist"
  },
  {
  "name": "Kumar",
  "age": 28,
  "occupation": "Entrepreneur"
  }
]

class User(Resource):
    def get(self, name):
        for user in users:
            if(name == user["name"]):
                return user, 200
        return "User not found", 404

    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        for user in users:
            if(name == user["name"]):
                return "User with name {} already exists".format(name), 400

        user = {
        "name": name,
        "age": args["age"],
        "occupation": args["occupation"]
        }

        users.append(user)
        return user, 201

    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        for user in users:
            if(name == user["name"]):
                user["age"] = args["age"]
                user["occupation"] = args["occupation"]
                return user, 200
        user = {
        "name": name,
        "age": args["age"],
        "occupation": args["occupation"]
        }
        users.append(user)
        return user, 201

    def delete(self, name):
        global users
        users = [user for user in users if user["name"] != name]
        return "{} is deleted.".format(name), 200

api.add_resource(User, "/user/<string:name>")

if __name__== '__main__':
    app.run(host = 'localhost',debug=True, port = 4996)
