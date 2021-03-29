from flask import Flask, session, request, jsonify
import requests
import json
from flask_cors import CORS, cross_origin
app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/restdb'

import pymongo
from pymongo import MongoClient

client = MongoClient()
client = MongoClient('localhost',27017) 

cors = CORS(app, resources={r"/add_user": {"origins": "http://localhost:5000"}})
cors = CORS(app, resources={r"/get_user": {"origins": "http://localhost:5000"}})
cors = CORS(app, resources={r"/update_user": {"origins": "http://localhost:5000"}})
cors = CORS(app, resources={r"/delete_user": {"origins": "http://localhost:5000"}})
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/add_user/", methods=["POST"])
@cross_origin(origin='localhost',headers=['Content-Type'])
def addUser():
    db = client['user_info']
    users = db.user_info
    name = request.json.get('name')
    user_id = request.json.get('id')

    new_list = {'name':name,'id':user_id}
    db_query = users.insert_one(new_list)

    result = {'result' : 'user is added successfully'}

    return result

@app.route("/get_user/", methods=["GET"])
@cross_origin(origin='localhost',headers=['Content-Type'])
def getUser():

    db = client['user_info']
    users = db.user_info

    result = []
    for user in users.find():
        result.append({'name' : user['name'], 'id' : user['id']})
    return jsonify({'results' : result})


@app.route("/update_user/", methods=["PUT"])
@cross_origin(origin='localhost',headers=['Content-Type'])
def updateUser():
    db = client['user_info']
    users = db.user_info

    name = request.json.get('name')
    user_id = request.json.get('id')

    updated_list = {"$set": {'id' : user_id}}
    edit_info = {'name' : name}
    users.update_one(edit_info, updated_list)
    result = {'result' : 'Updated successfully'}
    return result

@app.route('/delete_user/', methods=['DELETE'])
@cross_origin(origin='localhost',headers=['Content-Type'])
def deleteUser():
    db = client['user_info']
    users = db.user_info    
    user_id = request.json.get('id')

    delete_data = {'id' : user_id}
    todolist.delete_one(delete_data)
    result = {'result' : 'Deleted successfully'}
    return result

if __name__ == '__main__':
    app.run()
