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