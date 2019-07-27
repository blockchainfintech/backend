from flask_sqlalchemy import SQLAlchemy
import json

# Initialise database
db = SQLAlchemy()

class Node(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    nodeId = db.Column(db.String(80), unique=True, nullable=False)
    count = db.Column(db.Integer)
    maxCount = db.Column(db.Integer)
    
    def __repr__(self):
        return '<name %r>' % self.name

    def toDict(self):
        return {
            "id":        self.id,
            "name":      self.name,
            "latitude":  self.latitude,
            "longitude": self.longitude,
            "nodeId":    self.nodeId,
            "count":     self.count,
            "maxCount":  self.maxCount
        }

#>>> from database import db
#>>> db.create_all()
