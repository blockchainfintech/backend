from flask import Flask, escape, request, Blueprint

congestion = Blueprint("congestion", __name__)