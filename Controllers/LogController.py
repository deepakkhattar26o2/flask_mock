from flask import jsonify, request
from flask_restful import Resource
from init import db
from Models.Log import LogDetails

class Apii(Resource):
    def get(self):
        LogDetail = LogDetails(request.json, request.args)
        db.session.add(LogDetail)
        db.session.commit()
        return jsonify({'args' : request.args})
    def post(self):
        LogDetail = LogDetails(request.json, request.args)
        db.session.add(LogDetail)
        db.session.commit()
        return request.json