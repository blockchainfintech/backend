from flask import Flask, escape, request, Blueprint
from database import Node, db

# Initialise blueprint
node_connection = Blueprint("node_connection", __name__)

@node_connection.route('/push_congestion', methods=['POST'])
def push_congestion():
	if not request.is_json:
		print("Got a request to /push_congestion that wasn't a JSON response") # TODO handle properly

	# Get and update database row
	data = request.get_json()
	node = Node.query.filter_by(nodeId = data["nodeId"]).first()
	node.count = data["count"]
	if node.count > node.maxCount:
		node.maxCount = node.count
	db.session.commit()
	return ''

#location = Node(name='', latitude='', longitude='',nodeId='')
#db.session.add(location)

