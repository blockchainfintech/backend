from flask import Flask, escape, request, Blueprint
from database import Node
import json

congestion = Blueprint("congestion", __name__)

@congestion.route("/congestion")
def get_congestion():
	# TODO handle exceptions lul
	# Get coordinates
	tl_coord = (
		float(request.args.get("lat1")), 
		float(request.args.get("long1"))
	)

	br_coord = (
		float(request.args.get("lat2")), 
		float(request.args.get("long2"))
	)

	# Query database
	results = Node.query.filter(
		Node.latitude <= tl_coord[0], 
		Node.latitude >= br_coord[0], 
		Node.longitude >= tl_coord[1], 
		Node.longitude <= br_coord[1]).all()

	# ""normalise"" results
	for i in results:
		i.count = i.count / i.maxCount
	
	# Return results
	resObj = {"nodes": [i.toDict() for i in results]}

	return resObj