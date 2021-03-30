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
cors = CORS(app, resources={r"/add_task": {"origins": "http://localhost:5000"}})
cors = CORS(app, resources={r"/update_user": {"origins": "http://localhost:5000"}})
cors = CORS(app, resources={r"/delete_user": {"origins": "http://localhost:5000"}})

cors = CORS(app, resources={r"/get_user": {"origins": "http://localhost:5000"}})
cors = CORS(app, resources={r"/get_tasks_for_user/<username>": {"origins": "http://localhost:5000"}})
cors = CORS(app, resources={r"/update_task": {"origins": "http://localhost:5000"}})
cors = CORS(app, resources={r"/delete_task": {"origins": "http://localhost:5000"}})

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

@app.route("/add_task/", methods=["POST"])
@cross_origin(origin='localhost',headers=['Content-Type'])
def addTask():
    db = client['user_info']
    users = db.user_info

    name = request.json.get('name')

    task = request.json.get('task')

    new_list = {'username':name,'task':task}
    db_query = users.insert_one(new_list)

    result = {'result' : 'task is added successfully','status_code':1}

    return result


@app.route("/get_user/", methods=["GET"])
@cross_origin(origin='localhost',headers=['Content-Type'])
def getUser():
    
    db = client['user_info']
    users = db.user_info
    result = []
    for user in users.find():
        result.append({'name' : user['name'], 'id' : user['id']})
    return jsonify({'results' : result,'status_code':1})


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
    result = {'result' : 'Updated successfully','status_code':1}
    return result

@app.route("/delete_user/", methods=["DELETE"])
@cross_origin(origin='localhost',headers=['Content-Type'])
def deleteUser():
    db = client['user_info']
    users = db.user_info
    user_id = request.json.get('id')

    delete_data = {'id' : user_id}
    users.delete_one(delete_data)
    result = {'result' : 'Deleted successfully','status_code':1}
    return result

@app.route("/get_tasks_for_user/<username>/", methods=["GET"])
@cross_origin(origin='localhost',headers=['Content-Type'])
def getTasks(username):

    db = client['user_info']
    users = db.user_info
    username = 'username'

    result = []
    for task in users.find():
        result.append({'task' : task['name'], 'id' : task['id'],'username':username})
    return jsonify({'results' : result,'status_code':1})


@app.route("/update_task/", methods=["PUT"])
@cross_origin(origin='localhost',headers=['Content-Type'])
def updateTask():
    db = client['user_info']
    users = db.user_info

    name = request.json.get('name')
    task_id = request.json.get('id')

    updated_list = {"$set": {'id' : task_id}}
    edit_info = {'name' : name}
    users.update_one(edit_info, updated_list)
    result = {'result' : 'Updated successfully','status_code':1}
    return result


@app.route('/delete_task/', methods=['DELETE'])
@cross_origin(origin='localhost',headers=['Content-Type'])
def deleteTask:
    db = client['user_info']
    users = db.user_info
    user_id = request.json.get('id')

    delete_data = {'id' : user_id}
    users.delete_one(delete_data)
    result = {'result' : 'Deleted successfully','status_code':1}
    return result

if __name__ == '__main__':
    app.run()

