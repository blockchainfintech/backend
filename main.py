from flask import Flask, escape, request
from node_connection import node_connection
from congestion import congestion
from database import db

app = Flask(__name__)

# Initialise database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.sqlite3'
db.init_app(app)

# Register blueprints
app.register_blueprint(node_connection)
app.register_blueprint(congestion)