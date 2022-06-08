from flask import Flask
from flask_restful import Api
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy as alchemy

#init of flask app
app = Flask(__name__)
api = Api(app)

#database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = alchemy(app)

#init marshmallow
ma = Marshmallow(app)
