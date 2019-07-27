from flask import Flask, escape, request
from database import Location
app = Flask(__name__)




@app.route('/congestion')
def congestion():
    name = request.args.get("name")
    return f'Hello, {escape(name)}!'



#location = Location(name='', latitude='', longitude='',nodeId='')
#db.session.add(location)

#db.session.commit