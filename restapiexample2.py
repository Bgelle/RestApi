import flask
from flask import Flask, jsonify, request
from flask_restful import Resource, Api

app = Flask(__name__)
# creating an API object
api = Api(app)


class ArithmeticAdd(Resource):
    # @app.route('/add/<int:num1>/<int:num2>')
    def get(self, num1, num2):
        return flask.jsonify({'add': num1 + num2})


class ArithmeticSub(Resource):
    # @app.route('/add/<int:num1>/<int:num2>')
    def post(self, num1, num2):
        return flask.jsonify({'sub': num1 - num2})


api.add_resource(ArithmeticAdd, '/add/<int:num1>/<int:num2>')

api.add_resource(ArithmeticSub, '/sub/<int:num1>/<int:num2>')

if __name__ == '__main__':
    app.run(debug=True)
