from flask import Flask, escape, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.sqlite3'
db = SQLAlchemy(app)


class Nodes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    latitude = db.Column(db.String(80), unique=True, nullable=False)
    longitude = db.Column(db.String(120), unique=True, nullable=False)
    nodeId = db.Column(db.Integer, unique=True, nullable=False)
    
    def __repr__(self):
        return '<name %r>' % self.name

def __init__(self, name, latitude, longitude,nodeId):
	self.name = name
	self.longitude = longitude
	self.latitude = latitude
	self.nodeId = nodeId


#>>> from database import db
#>>> db.create_all()
