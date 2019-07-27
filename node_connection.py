from flask import Flask, escape, request, Blueprint
from database import Node

# Initialise blueprint
node_connection = Blueprint("node_connection", __name__)

@node_connection.route('/push_congestion', methods=['POST'])
def push_congestion():
	if not request.is_json:
		print("Got a request to /push_congestion that wasn't a JSON response") # TODO handle properly
	data = request.get_json()
	print(data)

#location = Location(name='', latitude='', longitude='',nodeId='')
#db.session.add(location)

#db.session.commit