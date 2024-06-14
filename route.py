from flask import Flask, request , Blueprint

api = Blueprint('/api/v1' , __name__ , url_prefix='/api/v1')

@api.route('/add' , methods=['POST'])
def add():
    requestData = request.get_json()
    return {
        "func" : "add"
    }

@api.route('/get-all' , methods=['POST'])
def getAll():
    requestData = request.get_json()
    return {
        "func" : "get-all"
    }


@api.route('/get-one' , methods=['GET'])
def getOne():
    requestData = request.get_json()
    return {
        "func" : "get-one"
    }


@api.route('/update' , methods=['PUT'])
def update():
    requestData = request.get_json()
    return {
        "func" : "update"
    }


@api.route('/delete' , methods=['DELETE'])
def delete():
    requestData = request.get_json()
    return {
        "func" : "delete"
    }
