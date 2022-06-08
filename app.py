from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy as alchemy
from sqlalchemy import Integer, String, DateTime, Column
import datetime, json

#init of flask app
app = Flask(__name__)
api = Api(app)

#database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = alchemy(app)
#init marshmallow
ma = Marshmallow(app)
# db.drop_all()
#Model
class LogDetails(db.Model):
    id = Column(Integer, primary_key = True)
    body = Column(String(1000), nullable = True)
    args = Column(String(1000), nullable = True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow )
    def __init__(self, body, args):
        self.body = json.dumps(body)
        self.args = json.dumps(args)
    def __repr__(self):
        return f"Id : {self.id}, Body : {self.body}, args = {self.args}, created_at = {self.created_at}"

#Schema
class LogSchema(ma.Schema):
    class Meta:
        fields=("id", "body", "args", "created_at")
log_schema = LogSchema()
log_schema = LogSchema(many=True)

db.create_all()

class Apii(Resource):
    def get(self):
        return jsonify({'args' : request.args})
    def post(self):
        LogDetail = LogDetails(request.json, request.args)
        db.session.add(LogDetail)
        db.session.commit()
        return request.json
api.add_resource(Apii, '/api')

@app.route('/api/data', methods=['GET'])
def get():
    data = LogDetails.query.all()
    return log_schema.jsonify(data)
#Hoist Server
if __name__=="__main__":
    app.run(debug=True)