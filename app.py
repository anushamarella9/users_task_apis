from flask import Flask, session, request, jsonify
import requests
import json
from flask_cors import CORS, cross_origin
app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/restdb'

import pymongo
from pymongo import MongoClient
from datetime import datetime
from bson import ObjectId

client = MongoClient()
client = MongoClient('localhost',27017)

#cors = CORS(app, resources={r"/add_user": {"origins": "http://localhost:5000"}})
cors = CORS(app, resources={r"/add_task": {"origins": "http://localhost:5000"}})
cors = CORS(app, resources={r"/get_all_tasks": {"origins": "http://localhost:5000"}})
cors = CORS(app, resources={r"/update_task/<task_id>": {"origins": "http://localhost:5000"}})
cors = CORS(app, resources={r"/delete_task/<id>": {"origins": "http://localhost:5000"}})

app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/add_task", methods=["POST"])
@cross_origin(origin='localhost',headers=['Content-Type'])
def addTask():
    db = client['task_info']
    tasks = db.task_info

    task = request.json.get('task')
    id = request.json.get('id')
    added_on = str(datetime.now())

    new_list = {'task':task,'added_on':added_on,'id':id}
    db_query = tasks.insert_one(new_list)

    result = {'message' : 'task is added successfully','status_code':1}

    return result


@app.route("/get_all_tasks", methods=["GET"])
@cross_origin(origin='localhost',headers=['Content-Type'])
def getTasks():
    db = client['task_info']
    tasks = db.task_info
    result = []
    for task in tasks.find():
        print("!!!!!!!!",task)
        result.append({'task' : task['task'],'added_on':task[str('added_on')],'id':task['id']})
    return jsonify({'results' : result,'status_code':1})


@app.route("/update_task/<task_id>", methods=["PUT"])
@cross_origin(origin='localhost',headers=['Content-Type'])
def updateTask(task_id):
    db = client['task_info']
    tasks = db.task_info
    task = request.json.get('task')

    tasks.update_one({"id":task_id}, {"$set": {"task": task}})

    result = {'result' : 'Updated successfully','status_code':1}
    return result


@app.route('/delete_task/<id>', methods=["DELETE"])
@cross_origin(origin='localhost',headers=['Content-Type'])
def deleteTask(id):
    db = client['task_info']
    tasks = db.task_info

    delete_data = {"id":id}
    tasks.delete_one(delete_data)
    result = {'result' : 'Deleted successfully','status_code':1}
    return result

if __name__ == '__main__':
    app.run()
