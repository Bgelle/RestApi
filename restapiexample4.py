from flask_restful import Resource,Api
from flask import Flask
app=Flask(__name__)
api=Api(app)
class Area(Resource):
    def post(self,a):
        return {'area of square':a*a}
    def post(self,a1):
         return {'area of circle':3.17*a1*a1}
#api.add_resource(Area,'/squarearea/<int:a>')
api.add_resource(Area,'/circlearea/<int:a1>')
if __name__=='__main__':
    app.run(debug=True)