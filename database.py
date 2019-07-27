from flask_sqlalchemy import SQLAlchemy

# Initialise database
db = SQLAlchemy()

class Node(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    latitude = db.Column(db.String(80), unique=True, nullable=False)
    longitude = db.Column(db.String(120), unique=True, nullable=False)
    nodeId = db.Column(db.Integer, unique=True, nullable=False)
    
    def __repr__(self):
        return '<name %r>' % self.name

#>>> from database import db
#>>> db.create_all()
