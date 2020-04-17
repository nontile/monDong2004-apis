from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

list = {}

class SimpleApis(Resource):
  def get(self, id):
    return {id: list[id]}

  def put(self, id):
    list[id] =  request.form['data']
    return {id: list[id]}


class List(Resource):
  def get(self):
    return list, 201, {'securekey': 'xe12'}

api.add_resource(SimpleApis, '/<string:id>')
api.add_resource(List, '/list')


if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=8080)

