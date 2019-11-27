from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from json import dumps, dump
import json as json

app = Flask(__name__)
api = Api(app)

class MyServer(Resource):
    def post(self):
        print(request.json)
        filename=str(request.json['transactionId'])+".json"
        json.dump(request.json, open(filename, "w"))
        return {'status':'success'}


api.add_resource(MyServer, '/notifications')

if __name__ == '__main__':
    app.run(port=8000)