from flask import Flask, escape, request
from node_connection import node_connection
from congestion import congestion

app = Flask(__name__)

# Register blueprints
app.register_blueprint(node_connection)
app.register_blueprint(congestion)