
from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from bson.json_util import dumps



app = Flask(__name__)

# app.config['MONGO_DBNAME'] = 'school'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/TestUsers'

mongo = PyMongo(app)

@app.route('/getAllRecords', methods=['GET'])
def getAllDocuments():
    results = mongo.db.users.find()
    response = dumps(results)
    return response


@app.route('/addRecords', methods=['POST'])
def addDocuments():
    jsonRequest = request.json
    name = jsonRequest['name']
    email = jsonRequest['email']

    if name and email and request.method == 'POST':
        id = mongo.db.users.insert({
            'name': name,
            'email': email
        })
        resp = jsonify("User Added Successfully")
        resp.status_code = 200
        return resp
    else:
        not_found()
@app.errorhandler(404)
def not_found(error=None):
    message: {
        'status': 404,
        'message': 'Not Found' + request.url
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp


if __name__ == '__main__':
    app.run(debug=True)
