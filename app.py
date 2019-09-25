import os
from flask import Flask, request, json
from flask_restful import Resource, Api 
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)
api = Api(app)
db = SQLAlchemy(app)

from models import Result


polls = {}
hasil = []



class PollSimple(Resource):
    def get(self, poll_id):
        return polls

    def post (self, poll_id):
        data = request.get_json(force=True)
        data = json.dumps(data)
        hasil.append(data)
        polls[poll_id] = hasil
        print(polls)
        return {poll_id: data}

api.add_resource(PollSimple, '/<string:poll_id>')

if __name__ == '__main__':
    app.run(debug=True)
